# Chainstack Developer Portal

This is the repository for the [Chainstack Developer Portal](https://docs.chainstack.com/).

The Developer Portal runs on [Mintlify](https://mintlify.com/).

### Using the Developer Portal

You can use the Developer Portal by just browsing and searching through it as you would normally. Note that the [RPC node API reference](https://docs.chainstack.com/reference/) is interactive, so feel free to play around with the calls.

Since we are in the age of AI and LLMs, here are additional ways to use the Developer Portal with agents:

* This repository is public, so your agents can just ingest it.
* [llms-full.txt](https://docs.chainstack.com/llms-full.txt) is automatically generated and published on every change.
* [skill.md](https://docs.chainstack.com/skill.md) is auto-generated with structured capabilities for AI agents.
* Any page is available as markdown by appending `.md` to its URL (e.g., `https://docs.chainstack.com/docs/platform-introduction.md`).
* Hosted MCP server — available at `https://docs.chainstack.com/mcp` (streamable HTTP, not SSE).

Note that the Developer Portal MCP server is a docs project and is different from an [RPC node MCP server](https://ideas.chainstack.com/p/mcp-server) that we are also building.

### MCP server

The Chainstack Developer Portal provides a hosted MCP (Model Context Protocol) server at `https://docs.chainstack.com/mcp`.

This is a **streamable HTTP** MCP server (not SSE). It provides AI models with access to search and navigate through all Chainstack documentation.

#### Supported AI tools

* **Claude Code**: `claude mcp add --transport http Chainstack-Developer-Portal https://docs.chainstack.com/mcp`
* **Cursor**: Click the "Connect to Cursor" button on any docs page
* **VS Code**: Click the "Connect to VS Code" button on any docs page  
* **Windsurf**: Add to `~/.codeium/windsurf/mcp_config.json`:
  ```json
  {
    "mcpServers": {
      "chainstack-developer-portal": {
        "serverUrl": "https://docs.chainstack.com/mcp"
      }
    }
  }
  ```

### Two-product architecture

The docs use Mintlify's product switcher with two products:

- **Cloud** — managed blockchain infrastructure (docs in `docs/`)
- **Self-Hosted** — deploy on your own infrastructure (docs in `docs/self-hosted/`)

Both products share the same `docs.json` for navigation.

### Contributing to the Developer Portal

Just contribute as you normally would—PRs, Issues, Discussions, whatever works best for you. We welcome every and all builders.

The repository includes a `CLAUDE.md` file with comprehensive project context and style guidelines for AI-assisted contributions.

#### Adding release notes

The documentation has two products with separate release notes:

- **Cloud** — `changelog.mdx` + `changelog/` directory
- **Self-Hosted** — `docs/self-hosted/release-notes.mdx` + `docs/self-hosted/changelog/`

##### Cloud release notes

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

##### Self-Hosted release notes

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

##### After creating release notes

Run `mintlify dev` and do a quick local visual check.

Run `mint broken-links` for a quick links check.

And submit your PR.

### Development

Install the [Mintlify CLI](https://www.npmjs.com/package/mintlify) to preview the documentation changes locally. To install, use the following command

```
npm i -g mintlify
```

Run the following command at the root of your documentation (where docs.json is)

```
mintlify dev
```

#### OpenAPI 3.0 nullability and Try it button

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

After fixing the spec, restart `mintlify dev` and the Try it button should appear.

### Available node options master list

`node-options-master-list.json` is the main file for this Developer Portal where all the available node options are kept up to date. If you need a custom table with whatever options you want, you feed the master list to an LLM and generate your own table.

Relevant tables (updated on every master list change):
* `nodes-clouds-regions-and-locations.mdx`
* `protocols-networks.mdx`

### CLI commands

| Command | Purpose |
| ------- | ------- |
| `mintlify dev` | Start local preview server |
| `mint validate` | Validate documentation build locally (strict mode) |
| `mint broken-links` | Check for broken links |
| `mint a11y` | Check accessibility (color contrast, alt text) |
| `mint openapi-check <file>` | Validate OpenAPI specifications |
| `mintlify install` | Re-install dependencies if issues |

A CI job will also check each PR and warn on dead links.

#### Troubleshooting

- Mintlify dev isn't running — run `mintlify install` to re-install dependencies.
- Page loads as a 404 — make sure you are running in a directory with `docs.json`.
