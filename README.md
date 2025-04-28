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

### Contributing to the Developer Portal

Just contribute as you normally would—PRs, Issues, Discussions, whatever works best for you. We welcome every and all builders.

### Development

Install the [Mintlify CLI](https://www.npmjs.com/package/mintlify) to preview the documentation changes locally. To install, use the following command

```
npm i -g mintlify
```

Run the following command at the root of your documentation (where docs.json is)

```
mintlify dev
```

#### Troubleshooting

- Mintlify dev isn't running - Run `mintlify install` it'll re-install dependencies.
- Page loads as a 404 - Make sure you are running in a folder with `docs.json`
