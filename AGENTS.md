# AGENTS Guidelines for This Repository

This repository contains the Chainstack Developer Portal built with Mintlify. When working on the project interactively with an agent (e.g. the Codex CLI) please follow the guidelines below for efficient documentation development and maintenance.

## 1. Use Mintlify Development Server

* **Always use `mintlify dev`** for local preview.
* **Test at** http://localhost:3000.
* **Do _not_ deploy to production** during agent development sessions.
* **Run link checks** with `mint broken-links` before submitting PRs.

## 2. Two-product architecture

The docs use Mintlify's product switcher with two products:

- **Cloud** — managed blockchain infrastructure (docs in `docs/`)
- **Self-Hosted** — deploy on your own infrastructure (docs in `docs/self-hosted/`)

Both products share the same `docs.json` for navigation. When adding pages, make sure you add them under the correct product.

## 3. Keep documentation structure consistent

When creating new documentation:

1. Install Mintlify CLI: `npm i -g mintlify`
2. Run dev server: `mintlify dev`
3. Check for broken links: `mint broken-links`
4. Validate build: `mint validate`
5. Follow existing patterns for consistency

## 4. MDX file requirements

Every MDX file must start with YAML frontmatter:

```yaml
---
title: "Clear, specific title"
description: "Concise description for SEO and navigation"
---
```

Never forget to add new files to `docs.json` navigation.

## 5. Navigation management

When adding new documentation:

1. **Create MDX file** in appropriate directory (`docs/`, `reference/`, or `recipes/`)
2. **Add frontmatter** with title and description
3. **Update `docs.json`** to include file in navigation (without `.mdx` extension)
4. **Test navigation** works in local preview

## 6. Release notes workflow

The documentation has two products with separate release notes:

- **Cloud** — managed blockchain infrastructure (`changelog.mdx` + `changelog/` directory)
- **Self-Hosted** — deploy on your own infrastructure (`docs/self-hosted/release-notes.mdx` + `docs/self-hosted/changelog/`)

### Cloud release notes

Creating release notes requires three steps:

#### Step 1: Update `changelog.mdx`
Copy previous entry within `<Update>` tags and paste on top:
```mdx
<Update label="Chainstack updates: December 31, 2025" description=" by Your Name" >

**Protocols**. Your update content here.

<Button href="/changelog/chainstack-updates-december-31-2025">Read more</Button>
</Update>
```

#### Step 2: Create changelog file
Create `changelog/chainstack-updates-december-31-2025.mdx` with same content (without `<Update>` tags).

#### Step 3: Update navigation
In `docs.json`, in the Cloud product's `Release notes` tab, add the newly created file name (without `.mdx`) between `changelog` and the previous release notes entries:
```json
"pages": [
  "changelog",
  "changelog/chainstack-updates-december-31-2025",
  "changelog/chainstack-updates-previous-entry"
]
```

### Self-Hosted release notes

#### Step 1: Update `docs/self-hosted/release-notes.mdx`
Add a new `<Update>` entry at the top:
```mdx
<Update label="Chainstack Self-Hosted v1.0.0: January 28, 2026" description="">

**Initial beta release**. Your update content here.

<Button href="/docs/self-hosted/changelog/chainstack-self-hosted-v1-0-0-january-28-2026">Read more</Button>
</Update>
```

#### Step 2: Create changelog file
Create file in `docs/self-hosted/changelog/` using format `chainstack-self-hosted-v1-0-0-month-day-year.mdx`. The page title should match the label.

#### Step 3: Update navigation
In `docs.json`, in the Self-Hosted product's `Release notes` tab, add the new changelog page.

## 7. Mintlify components usage

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

## 8. Code examples

When adding code examples:

* Include complete, runnable examples
* Use `<CodeGroup>` for multiple languages
* Specify language tags on all code blocks
* Include realistic data, not placeholders
* Use `<RequestExample>` and `<ResponseExample>` for API docs

## 9. Writing style guidelines

Follow the established style guide:

* **Use sentence case** for everything (not Title Case)
* **Active voice** over passive voice
* **American English** spelling
* **Oxford comma** in lists
* **Escape dollar signs** with backslash (`\$`) in MDX files
* **Bold UI elements** when referencing them
* Use `>` for UI clickthrough paths

## 10. API documentation

For API reference documentation:

* Document all parameters with `<ParamField>`
* Show response structure with `<ResponseField>`
* Include both success and error examples
* Use `<Expandable>` for nested object properties
* Always include authentication examples

## 11. Image management

When adding images:

* Place in `images/` directory
* Use descriptive filenames
* Wrap in `<Frame>` component
* Always include alt text
* Optimize for web (compress large images)

## 12. Node options master list

`node-options-master-list.json` is the main file for this Developer Portal where all the available node options are kept up to date. If you need a custom table with whatever options you want, you feed the master list to an LLM and generate your own table.

Relevant tables (updated on every master list change):

- `nodes-clouds-regions-and-locations.mdx`
- `protocols-networks.mdx`

When updating:

1. Edit `node-options-master-list.json`
2. Regenerate dependent tables
3. Verify changes display correctly

## 13. Quality checklist

Before submitting changes:

- [ ] All code examples tested
- [ ] Build validated with `mint validate`
- [ ] Links checked with `mint broken-links`
- [ ] New files added to `docs.json`
- [ ] Frontmatter includes title and description
- [ ] Images optimized and have alt text
- [ ] Follows sentence case convention
- [ ] Dollar signs escaped with backslash (`\$`)
- [ ] UI elements are bolded
- [ ] No Title Case used

## 14. Common tasks

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

## 15. Development commands

| Command | Purpose |
| ------- | ------- |
| `mintlify dev` | Start local preview server |
| `mint validate` | Validate documentation build locally (strict mode) |
| `mint broken-links` | Check for broken links |
| `mint a11y` | Check accessibility (color contrast, alt text) |
| `mint openapi-check <file>` | Validate OpenAPI specifications |
| `mintlify install` | Re-install dependencies if issues |

## 16. MCP server integration

The portal provides an MCP server at `https://docs.chainstack.com/mcp`:

* This is for documentation access, not RPC nodes
* It's streamable HTTP (not SSE)
* Agents can search and navigate all documentation
* Keep this in mind when structuring content

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
- Make sure you update to the latest Mintlify version in your local dev environment

## 18. Important guidelines

* **Never use Title Case** - always sentence case
* **Never mix abbreviated and non-abbreviated** date formats
* **Always test code examples** before publishing
* **Always run link checker** before PR
* **Never commit without updating** `docs.json` for new files

---

Following these practices ensures consistent documentation quality, maintains the established style guide, and enables efficient content management. Always preview changes locally and check for broken links before submitting pull requests.