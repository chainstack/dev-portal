# Chainstack Developer Portal

This is the repository for the [Chainstack Developer Portal](https://docs.chainstack.com/).

The Developer Portal runs on [Mintlify](https://mintlify.com/)—the same docs engine as used by Anthropic & Cursor, so if you ever used those, you'll feel right at home.

### Using the Developer Portal

You can use the Developer Portal by just browsing and searching through it as you would normally. Note that the [RPC node API reference](https://docs.chainstack.com/reference/) is interactive, so feel free to play around with the calls.

Since we are in the age of AI and LLMs, here are three additional ways to use the Developer Portal with agents:

* This repository is public, so your agents can just ingest it.
* [llms-full.txt](https://docs.chainstack.com/llms-full.txt) is automatically generated and published on every change.
* Built-in MCP server — just run `npx @mintlify/mcp@latest add chainstack` to add the Developer Portal as a local MCP server.

Note that the Developer Portal MCP server is a docs project and is different from an [RPC node MCP server](https://ideas.chainstack.com/p/mcp-server) that we are also building.

### MCP server

Built-in MCP server — just run `npx @mintlify/mcp@latest add chainstack` to add the Developer Portal as a local MCP server.

### Contributing to the Developer Portal

Just contribute as you normally would—PRs, Issues, Discussions, whatever works best for you. We welcome every and all builders.

#### Cursor, Windsurf, Claude Code rules & memory

To make your contribution consistent & effortless, the Chainstack Developer Portal has project rules for IDEs:

* Cursor:
   * `.cursor/rules/project-context-structure-and-formatting.mdc`
   * `.cursor/rules/project-writing-style-guide.mdc`

The rules are set to `alwaysApply: true`.

Each of the rules files is under 500 lines as per Cursor recommendations.

* Windsurf:
   * `.windsurf/rules/project-context-structure-and-formatting.md`
   * `.windsurf/rules/project-writing-style-guide.md`

The rules are set to `trigger: always_on`.

Each of the rules files is under 12000 characters as per Windsurf recommendations.

* Claude Code:
   * `CLAUDE.md`

#### Adding release notes

The release notes structure might be a bit convoluted to figure out at first glance, so here's a step-by-step walkthrough:

The structure:

```
dev-portal/
├── changelog.mdx
├── docs.json
└── changelog/
   ├── chainstack-updates-may-30-2025.mdx
   ├── chainstack-updates-april-1-2025.mdx
   ├── chainstack-updates-march-4-2025.mdx
   ├── chainstack-updates-february-5-2025.mdx
   └── chainstack-updates-january-7-2025.mdx
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

2. In the `changelog/` directory, copy or create a file in the proper format. Example `chainstack-updates-may-30-2025.mdx`. In the file, paste in the same entry (without the `<Updates>` tag) that you did in the `changelog.mdx` file.
3. In `docs.json`, in the `Release notes` section, add the newly created file name (without `.mdx`) between `changelog` and the previous release notes entries. This will let the docs pick up the release notes file and properly display it.

Example:
```
       "tab": "Release notes",
        "pages": [
          "changelog",
          "changelog/chainstack-updates-may-30-2025",
          "changelog/chainstack-updates-may-16-2025",
```

And you are done.

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

### Available node options master list

`node-options-master-list.json` is the main file for this Developer Portal where the all the available node options are kept up to date. If you need a custom table with whatever options you want, you feed the master list to an LLM and generate your own table. The context length of `node-options-master-list.json` is about 17387 tokens.

### Dead links check

A CI job will check each PR and warn on the dead links.

You can also run the dead links check locally before submitting your PR:

```
mint broken-links
```

Running locally is much more convenient and much faster than a CI job.

#### Troubleshooting

- Mintlify dev isn't running - Run `mintlify install` it'll re-install dependencies.
- Page loads as a 404 - Make sure you are running in a folder with `docs.json`
