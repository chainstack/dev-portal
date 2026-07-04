#!/usr/bin/env python3
"""Generate a nested llms.txt for the Chainstack docs (Mintlify).

Why nested: Mintlify's auto llms.txt is a single flat file listed alphabetically and
truncated near 100K chars, which silently drops our highest-traffic protocols from the
index. A custom file at the repo root overrides the auto one. To get BOTH a small root
(AFDocs passes <50K) AND high page coverage, we use the progressive-disclosure pattern
(Cloudflare/QuickNode/Alchemy): a tiny root llms.txt that links to per-section sub-index
llms.txt files, each listing that section's pages as Markdown (.md) links. Mintlify serves
a file named `llms.txt` at any sub-path, so the sub-indexes are reachable.

Source of truth: the page list is read from docs.json navigation (deterministic; matches
the published sitemap). Run this whenever pages are added/removed/retitled:

    python3 scripts/generate_llms_txt.py        # writes llms.txt + <section>/llms.txt
    python3 scripts/generate_llms_txt.py --check # exit 1 if committed files are stale (CI)

Output is deterministic, so `--check` can gate freshness in CI.
"""
import json, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # dev-portal/
DOCS_JSON = os.path.join(REPO, "docs.json")

# Highest-traffic / highest-AI protocols lead the index (Mintlify: "first 20% of the file").
CROWN = ["ethereum", "solana", "hyperliquid", "ton", "tron"]
PROTO = CROWN + ["base", "bnb", "polygon-zkevm", "polygon", "arbitrum", "optimism",
                 "avalanche", "bitcoin", "gnosis", "fantom", "cronos", "ronin",
                 "zksync", "starknet", "monad", "plasma", "tempo", "aptos"]


def nav_leaves(node, acc):
    """Collect every page-path string from docs.json navigation."""
    if isinstance(node, dict):
        for v in node.values():
            nav_leaves(v, acc)
    elif isinstance(node, list):
        for v in node:
            if isinstance(v, str):
                acc.append(v)
            else:
                nav_leaves(v, acc)


def title_of(page):
    """Frontmatter title for a page path, else a slug fallback."""
    f = os.path.join(REPO, page + ".mdx")
    if os.path.exists(f):
        head = open(f, encoding="utf-8", errors="ignore").read(1500)
        m = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', head, re.M)
        if m:
            return m.group(1).strip().strip('"').strip("'")
    return page.rstrip("/").split("/")[-1] or "Home"


def proto_of(slug):
    for pr in PROTO:
        if slug == pr or slug.startswith(pr + "-"):
            return pr
    return None


def classify(page):
    """Return (section_key, sub_index_path, label, priority) for a page path."""
    seg = page.strip("/").split("/")
    top = seg[0] if seg and seg[0] else ""
    slug = seg[-1]
    if top == "reference":
        pr = proto_of(slug)
        if pr:
            prio = CROWN.index(pr) if pr in CROWN else 10 + PROTO.index(pr)
            return (f"ref:{pr}", f"reference/{pr}/llms.txt", f"{pr.capitalize()} node API", prio)
        return ("ref:other", "reference/other/llms.txt", "API reference (other)", 90)
    if top == "docs":
        return ("docs", "docs/llms.txt", "Guides", 100)
    if top == "recipes":
        return ("recipes", "recipes/llms.txt", "Recipes", 101)
    if top == "changelog":
        return ("changelog", "changelog/llms.txt", "Changelog", 110)
    if top:
        return (f"top:{top}", f"{top}/llms.txt", top.capitalize(), 105)
    return ("_root", None, "Overview", -1)


def build():
    docs = json.load(open(DOCS_JSON, encoding="utf-8"))
    leaves = []
    nav_leaves(docs["navigation"], leaves)
    # internal page paths only, de-duplicated, order preserved
    seen, pages = set(), []
    for lf in leaves:
        if lf.startswith("http") or lf in seen:
            continue
        seen.add(lf)
        pages.append(lf)

    sections, meta, root_pages = {}, {}, []
    for p in pages:
        key, subpath, label, prio = classify(p)
        if key == "_root":
            root_pages.append(p)
            continue
        sections.setdefault(key, []).append(p)
        meta[key] = (subpath, label, prio)

    files = {}  # repo-relative path -> content

    # per-section sub-index files
    for key, ps in sections.items():
        subpath, label, _ = meta[key]
        lines = [f"# {label}\n",
                 f"\n> Chainstack {label} — index of pages. Each links to clean Markdown (.md).\n",
                 "\n## Pages\n"]
        for p in ps:
            lines.append(f"- [{title_of(p)}](/{p}.md)\n")
        files[subpath] = "".join(lines)

    # small root index linking to sub-indexes (root-relative), priority-ordered
    ordered = sorted(meta.items(), key=lambda kv: kv[1][2])
    root = ["# Chainstack Documentation\n",
            "\n> Chainstack developer documentation: deploy nodes and get RPC endpoints across "
            "27+ protocols. Sections are ordered by usage — highest-traffic protocols (Ethereum, "
            "Solana, Hyperliquid, TON, TRON) first. Each section links to a per-section index; "
            "every page is also available as Markdown by appending `.md`, via the search MCP "
            "server, and in the sitemap.\n",
            "\n## Node APIs\n"]
    guides_started = False
    for key, (subpath, label, prio) in ordered:
        if prio >= 100 and not guides_started:
            root.append("\n## Guides and resources\n")
            guides_started = True
        root.append(f"- [{label}](/{subpath})\n")
    for p in root_pages:
        root.append(f"- [{title_of(p)}](/{p}.md)\n")
    files["llms.txt"] = "".join(root)

    return files, len(pages)


def main():
    files, n_pages = build()
    check = "--check" in sys.argv
    stale = []
    for rel, content in files.items():
        path = os.path.join(REPO, rel)
        current = open(path, encoding="utf-8").read() if os.path.exists(path) else None
        if current != content:
            stale.append(rel)
        if not check:
            os.makedirs(os.path.dirname(path) or REPO, exist_ok=True)
            open(path, "w", encoding="utf-8").write(content)

    root_sz = len(files["llms.txt"])
    sub_sizes = {r: len(c) for r, c in files.items() if r != "llms.txt"}
    print(f"pages: {n_pages} | sub-indexes: {len(sub_sizes)} | root llms.txt: {root_sz:,} chars "
          f"(<50K: {root_sz < 50000}) | largest sub-index: {max(sub_sizes.values()):,} chars "
          f"(all <50K: {all(s < 50000 for s in sub_sizes.values())})")
    if check:
        if stale:
            print(f"STALE ({len(stale)}): " + ", ".join(sorted(stale)[:8]))
            print("Run: python3 scripts/generate_llms_txt.py")
            sys.exit(1)
        print("llms.txt files are up to date.")
    else:
        print(f"wrote llms.txt + {len(sub_sizes)} sub-index files.")


if __name__ == "__main__":
    main()
