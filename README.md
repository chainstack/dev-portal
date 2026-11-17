# Chainstack Developer Portal

This is the source for the [Chainstack Developer Portal](https://docs.chainstack.com/), the documentation for Chainstack Cloud and Chainstack Self-Hosted. The Developer Portal runs on [Mintlify](https://www.mintlify.com/).

## Using the Developer Portal

Browse and search [docs.chainstack.com](https://docs.chainstack.com/) as you would any docs site. The [RPC node API reference](https://docs.chainstack.com/reference/blockchain-apis) is interactive, so you can send the calls from the browser.

### With AI agents

* [Chainstack MCP server](https://docs.chainstack.com/docs/chainstack-mcp-server) — `https://mcp.chainstack.com/mcp`. Searches the docs and also deploys nodes, requests testnet funds, fetches pricing, and checks platform status. The page has setup for Claude Code, Codex, Cursor, Devin, Gemini CLI, VS Code, and other clients. You can also type `get mcp.chainstack.com` into any agent and it walks you through setup.
* [llms.txt](https://docs.chainstack.com/llms.txt) — an index of the docs with a nested index per section. [llms-full.txt](https://docs.chainstack.com/llms-full.txt) has the full text of every page.
* [skill.md](https://docs.chainstack.com/skill.md) — a generated description of what the docs cover, for agents that load skills.
* Markdown pages — append `.md` to any page URL, for example `https://docs.chainstack.com/docs/platform-introduction.md`.
* Page menu — every page has a menu to copy or view it as Markdown, open it in ChatGPT, Claude, Perplexity, or Grok, or connect it to Cursor or VS Code.
* This repository — it's public, so agents can read the MDX source directly.

The docs-only [Developer Portal MCP server](https://docs.chainstack.com/docs/developer-portal-mcp-server) at `https://docs.chainstack.com/mcp` still works but is deprecated in favor of the Chainstack MCP server.

## Contributing

Open a pull request or an issue. We welcome every and all builders.

The repository includes `CLAUDE.md` and `AGENTS.md` with project context and the style guide for AI-assisted contributions. Read the style guide in `CLAUDE.md` before writing a page.

### Two-product architecture

The docs use Mintlify's product switcher with two products:

- **Cloud** — managed blockchain infrastructure (docs in `docs/`)
- **Self-Hosted** — deploy on your own infrastructure (docs in `docs/self-hosted/`)

Both products share the same `docs.json` for navigation.

### Adding release notes

The documentation has two products with separate release notes:

- **Cloud** — `changelog.mdx` + `changelog/` directory
- **Self-Hosted** — `docs/self-hosted/release-notes.mdx` + `docs/self-hosted/changelog/`

#### Cloud release notes

The structure:

```
dev-portal/
├── changelog.mdx
├── docs.json
└── changelog/
   ├── chainstack-updates-may-30-2025.mdx
   ├── chainstack-updates-april-1-2025.mdx
   └── [previous entries...]
```

You need to work with each of these files to create proper release notes (order is not important):

1. In `changelog.mdx`, copy the previous entry within the `<Update...> </Update>` tags (and including these tags) and paste it on top of the previous entry.

Example:

```
<Update label="Chainstack updates: May 30, 2025" description=" by Ake" >

**Protocols**. Now, you can deploy [Global Nodes](/docs/global-elastic-node) for Unichain Mainnet. See also [Unichain tooling](/docs/unichain-tooling) and a [tutorial](/docs/unichain-collecting-uniswapv4-eth-usdc-trades).

<Button href="/changelog/chainstack-updates-may-30-2025">Read more</Button>
</Update>
```

Edit the entry to make it your piece of the release notes.

Make sure you change the dates properly in the update label and in the button label.

2. In the `changelog/` directory, copy or create a file in the proper format. Example `chainstack-updates-may-30-2025.mdx`. In the file, paste in the same entry (without the `<Update>` tags) that you did in the `changelog.mdx` file.
3. In `docs.json`, in the Cloud product's `Release notes` tab, add the newly created file name (without `.mdx`) between `changelog` and the previous release notes entries. This will let the docs pick up the release notes file and properly display it.

Example:
```
       "tab": "Release notes",
        "pages": [
          "changelog",
          "changelog/chainstack-updates-may-30-2025",
          "changelog/chainstack-updates-may-16-2025",
```

#### Self-Hosted release notes

The structure:

```
dev-portal/
└── docs/self-hosted/
    ├── release-notes.mdx
    └── changelog/
        ├── chainstack-self-hosted-v1-0-0-january-28-2026.mdx
        └── [version entries...]
```

1. In `docs/self-hosted/release-notes.mdx`, add a new `<Update>` entry at the top.

Example:

```
<Update label="Chainstack Self-Hosted v1.0.0: January 28, 2026" description="">

**Initial beta release**. Your update content here.

<Button href="/docs/self-hosted/changelog/chainstack-self-hosted-v1-0-0-january-28-2026">Read more</Button>
</Update>
```

2. Create file in `docs/self-hosted/changelog/` using format `chainstack-self-hosted-v1-0-0-month-day-year.mdx`. The page title should match the label.
3. In `docs.json`, in the Self-Hosted product's `Release notes` tab, add the new changelog page.

#### After creating release notes

Run `mint dev` and do a quick local visual check.

Run `mint broken-links` for a quick links check.

And submit your PR.

## Development

Install the [Mintlify CLI](https://www.mintlify.com/docs/cli/install) to preview changes locally. It needs Node.js v20.17.0 or later (Node.js 25 isn't supported).

```bash
npm i -g mint
```

Run the preview from the repository root, where `docs.json` is:

```bash
mint dev
```

The preview runs at `http://localhost:3000`.

### CLI commands

| Command | Purpose |
| ------- | ------- |
| `mint dev` | Start the local preview server |
| `mint validate` | Check content and OpenAPI specs, then run a strict build |
| `mint broken-links` | Check for broken links |
| `mint a11y` | Check accessibility (color contrast, alt text) |
| `mint score` | Run agent-readiness checks on a docs site |
| `mint update` | Update the CLI to the latest version |

Every pull request runs the **Mintlify Deployment** check, which builds the docs. Fix any failure it reports before merging.

### Troubleshooting

- `mint dev` fails to start — run `mint update`, and check that your Node.js version is supported. If it still fails, delete `~/.mintlify/` and run `mint dev` again.
- Page loads as a 404 — make sure you are running in the directory with `docs.json`.

### OpenAPI 3.0 nullability and Try it button

If a reference page renders without the Try it button or throws an error like:

```
Error: no matching OpenAPI operation object found with path "/evm" and method "post"
```

check the referenced OpenAPI spec for invalid null types. OpenAPI 3.0 does not support `"type": "null"`. Use `"nullable": true` on the actual schema instead. For example, replace:

```json
"result": {
  "oneOf": [
    { "type": "null" },
    { "type": "object" }
  ]
}
```

with:

```json
"result": {
  "type": "object",
  "nullable": true
}
```

After fixing the spec, restart `mint dev` and the Try it button should appear.

## Master lists

### Node options master list

`node-options-master-list.json` is the main file for this Developer Portal where all the available node options are kept up to date. If you need a custom table with whatever options you want, you feed the master list to an LLM and generate your own table.

Relevant tables (updated on every master list change):
* `nodes-clouds-regions-and-locations.mdx`
* `protocols-networks.mdx`

When regenerating the tables, use the current product node-type names — **Global Node** (the `global` node type), **Dedicated Node**, and **Trader Node**. Do **not** emit **Elastic** (the deprecated name for Global Node): in `protocols-networks.mdx` the **Support** column reads `Global Node, Dedicated` and the availability headers are `Global Node Mainnet Support` / `Global Node Testnet Support`.

### Self-Hosted deployments master list

`self-hosted-deployments.json` is the source of truth for every Chainstack Self-Hosted deployment: protocols, networks, clients, versions, resources, presets, and ports. Regenerate these tables on every change:

* `docs/self-hosted/supported-clients-and-protocols.mdx`
* `docs/self-hosted/requirements.mdx`

### llms.txt

The `llms.txt` files are custom and replace the Mintlify-generated one: a small root index at the repository root that links to one index per section, such as `docs/llms.txt`. A daily workflow regenerates them from `docs.json` and opens a pull request when they drift.
