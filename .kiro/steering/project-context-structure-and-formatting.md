---
inclusion: always
---
# Chainstack Developer Portal project context, structure, and formatting

## Project context

- This is a documentation project on the Mintlify platform
- We use MDX files with YAML frontmatter  
- Navigation is configured in `docs.json`

## Required page structure

Every page must start with frontmatter:

```yaml
---
title: "Clear, specific title"
description: "Concise description for SEO and navigation"
---
```

## Mintlify components

### Callouts

- `<Note>` for helpful supplementary information
- `<Warning>` for important cautions and breaking changes
- `<Tip>` for best practices and expert advice  
- `<Info>` for neutral contextual information
- `<Check>` for success confirmations

### Code examples

- When appropriate, include complete, runnable examples
- Use `<CodeGroup>` for multiple language examples
- Specify language tags on all code blocks
- Include realistic data, not placeholders
- Use `<RequestExample>` and `<ResponseExample>` for API docs

### Procedures

- Use `<Steps>` component for sequential instructions
- Include verification steps with `<Check>` components when relevant
- Break complex procedures into smaller steps

### Content organization

- Use `<Tabs>` when deemed appropriate to show information in tabs-style next to each other in one row
- Use `<Accordion>` for progressive disclosure
- Use `<Card>` and `<CardGroup>` for highlighting content
- Wrap images in `<Frame>` components with descriptive alt text

## Release notes

### Structure

Release notes require updates to three files:

```
dev-portal/
├── changelog.mdx
├── docs.json
└── changelog/
   ├── chainstack-updates-may-30-2025.mdx
   ├── chainstack-updates-april-1-2025.mdx
   └── [previous entries...]
```

### Process

1. **Update `changelog.mdx`**: Copy the previous entry within `<Update...> </Update>` tags and paste it on top of the previous entry. Edit dates and content appropriately.

Example:
```
<Update label="Chainstack updates: May 30, 2025" description=" by Ake" >

**Protocols**. Now, you can deploy [Global Nodes](/docs/global-elastic-node) for Unichain Mainnet. See also [Unichain tooling](/docs/unichain-tooling) and a [tutorial](/docs/unichain-collecting-uniswapv4-eth-usdc-trades).

<Button href="/changelog/chainstack-updates-may-30-2025">Read more</Button>
</Update>
```

2. **Create file in `changelog/` directory**: Use format `chainstack-updates-may-30-2025.mdx`. Paste the same entry content (without the `<Update>` tags) from step 1.

3. **Update `docs.json`**: In the `Release notes` section, add the newly created file name (without `.mdx`) between `changelog` and the previous release notes entries.

Example:
```
       "tab": "Release notes",
        "pages": [
          "changelog",
          "changelog/chainstack-updates-may-30-2025",
          "changelog/chainstack-updates-may-16-2025",
```

## API documentation requirements

- Document all parameters with `<ParamField>` 
- Show response structure with `<ResponseField>`
- Include both success and error examples
- Use `<Expandable>` for nested object properties
- Always include authentication examples

## Quality standards

- Test all code examples before publishing whenever possible
- Use relative paths for internal links
- Include alt text for all images
- Ensure proper heading hierarchy (start with h2)
- Check existing patterns for consistency