# AGENTS Guidelines for This Repository

This repository contains the Chainstack Developer Portal built with Mintlify. When working on the project interactively with an agent (e.g. the Codex CLI) please follow the guidelines below for efficient documentation development and maintenance.

## 1. Use Mintlify Development Server

* **Always use `mintlify dev`** for local preview.
* **Test at** http://localhost:3000.
* **Do _not_ deploy to production** during agent development sessions.
* **Run link checks** with `mint broken-links` before submitting PRs.

## 2. Keep Documentation Structure Consistent

When creating new documentation:

1. Install Mintlify CLI: `npm i -g mintlify`
2. Run dev server: `mintlify dev`
3. Check for broken links: `mint broken-links`
4. Follow existing patterns for consistency

## 3. MDX File Requirements

Every MDX file must start with YAML frontmatter:

```yaml
---
title: "Clear, specific title"
description: "Concise description for SEO and navigation"
---
```

Never forget to add new files to `docs.json` navigation.

## 4. Navigation Management

When adding new documentation:

1. **Create MDX file** in appropriate directory (`docs/`, `reference/`, or `recipes/`)
2. **Add frontmatter** with title and description
3. **Update `docs.json`** to include file in navigation (without `.mdx` extension)
4. **Test navigation** works in local preview

## 5. Release Notes Workflow

Creating release notes requires three steps:

### Step 1: Update `changelog.mdx`
Copy previous entry within `<Update>` tags and paste on top:
```mdx
<Update label="Chainstack updates: December 31, 2025" description=" by Your Name" >

**Protocols**. Your update content here.

<Button href="/changelog/chainstack-updates-december-31-2025">Read more</Button>
</Update>
```

### Step 2: Create changelog file
Create `changelog/chainstack-updates-december-31-2025.mdx` with same content (without `<Update>` tags).

### Step 3: Update navigation
In `docs.json`, add to `Release notes` section:
```json
"pages": [
  "changelog",
  "changelog/chainstack-updates-december-31-2025",
  "changelog/chainstack-updates-previous-entry"
]
```

## 6. Mintlify Components Usage

Use appropriate components for content:

| Component | Use Case |
| --------- | -------- |
| `<Note>` | Helpful supplementary information |
| `<Warning>` | Important cautions and breaking changes |
| `<Tip>` | Best practices and expert advice |
| `<Info>` | Neutral contextual information |
| `<Check>` | Success confirmations |
| `<Steps>` | Sequential instructions |
| `<CodeGroup>` | Multiple language examples |
| `<Tabs>` | Side-by-side information |
| `<Accordion>` | Progressive disclosure |
| `<Card>`, `<CardGroup>` | Highlighting content |
| `<Frame>` | Wrapping images with alt text |

## 7. Code Examples

When adding code examples:

* Include complete, runnable examples
* Use `<CodeGroup>` for multiple languages
* Specify language tags on all code blocks
* Include realistic data, not placeholders
* Use `<RequestExample>` and `<ResponseExample>` for API docs

## 8. Writing Style Guidelines

Follow the established style guide:

* **Use sentence case** for everything (not Title Case)
* **Active voice** over passive voice
* **American English** spelling
* **Oxford comma** in lists
* **Escape dollar signs** with backslash (`\$`) in MDX files
* **Bold UI elements** when referencing them
* Use `>` for UI clickthrough paths

## 9. API Documentation

For API reference documentation:

* Document all parameters with `<ParamField>`
* Show response structure with `<ResponseField>`
* Include both success and error examples
* Use `<Expandable>` for nested object properties
* Always include authentication examples

## 10. Image Management

When adding images:

* Place in `images/` directory
* Use descriptive filenames
* Wrap in `<Frame>` component
* Always include alt text
* Optimize for web (compress large images)

## 11. Master Lists Maintenance

The `node-options-master-list.json` is the source of truth for node options. When updating:

1. Edit the master list JSON
2. Regenerate dependent tables:
   - `nodes-clouds-regions-and-locations.mdx`
   - `protocols-networks.mdx`
3. Verify changes display correctly

## 12. Quality Checklist

Before submitting changes:

- [ ] All code examples tested
- [ ] Links checked with `mint broken-links`
- [ ] New files added to `docs.json`
- [ ] Frontmatter includes title and description
- [ ] Images optimized and have alt text
- [ ] Follows sentence case convention
- [ ] Dollar signs escaped with backslash (`\$`)
- [ ] UI elements are bolded
- [ ] No Title Case used

## 13. Common Tasks

### Add New Tutorial
1. Create MDX file in `docs/`
2. Add frontmatter with protocol prefix (e.g., `ethereum-tutorial-...`)
3. Update `docs.json` navigation
4. Include complete code examples
5. Add to relevant protocol's tooling page

### Add New API Method
1. Create MDX file in `reference/`
2. Use API documentation components
3. Include request/response examples
4. Update `docs.json` navigation
5. Test interactive features

### Add New Recipe
1. Create MDX file in `recipes/`
2. Keep it concise and focused
3. Include working code snippet
4. Update `docs.json` navigation

## 14. Development Commands

| Command | Purpose |
| ------- | ------- |
| `mintlify dev` | Start local preview server |
| `mint broken-links` | Check for broken links |
| `mintlify install` | Re-install dependencies if issues |

## 15. MCP Server Integration

The portal provides an MCP server at `https://docs.chainstack.com/mcp`:

* This is for documentation access, not RPC nodes
* It's streamable HTTP (not SSE)
* Agents can search and navigate all documentation
* Keep this in mind when structuring content

## 16. IDE Integration

The project has rules for different IDEs:

* **Cursor**: `.cursor/rules/` directory
* **Windsurf**: `.windsurf/rules/` directory
* **Kiro**: `.kiro/steering/` directory
* **Claude Code**: `CLAUDE.md` file

These ensure consistent contributions across different tools.

## 17. Troubleshooting

### Common Issues

**"Mintlify dev not running"**
```bash
mintlify install
```

**"Page loads as 404"**
- Ensure running in directory with `docs.json`
- Check file is added to navigation
- Verify frontmatter is valid YAML

**"Broken links found"**
- Use relative paths for internal links
- Check file exists at specified path
- Ensure `.mdx` extension not included in links

**Mintlify schema validation fail**
- Make sure you update to the latets Mintlify version in your local dev environment

## 18. Important Guidelines

* **Never use Title Case** - always sentence case
* **Never mix abbreviated and non-abbreviated** date formats
* **Always test code examples** before publishing
* **Always run link checker** before PR
* **Never commit without updating** `docs.json` for new files

---

Following these practices ensures consistent documentation quality, maintains the established style guide, and enables efficient content management. Always preview changes locally and check for broken links before submitting pull requests.