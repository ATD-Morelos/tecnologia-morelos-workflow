---
name: kb-publish
description: >
  Create, edit, and publish documents in Tecnología Morelos knowledge bases.
  Use when a document is ready to be published to tecnologia.morelos.gob.mx
  after the user has approved the content.
allowed-tools: mcp__tecnologia-morelos__create_knowledge_base mcp__tecnologia-morelos__create_knowledge_node mcp__tecnologia-morelos__update_knowledge_node mcp__tecnologia-morelos__move_knowledge_node mcp__tecnologia-morelos__delete_knowledge_node mcp__tecnologia-morelos__create_knowledge_relation mcp__tecnologia-morelos__find_similar_and_create_relations mcp__tecnologia-morelos__get_knowledge_node mcp__tecnologia-morelos__list_knowledge_nodes
---

# KB Publish — Create and Publish to Tecnología Morelos

## When to use

- After a document has been generated and approved by the user
- When creating the initial KB structure for a new project
- When updating existing documents with new content

## Critical rules

1. **Always read before writing** — Use `get_knowledge_node` to read current
   content before updating. Never overwrite blindly.

2. **Use `id` for updates, `nodeId` for reads**:
   - `get_knowledge_node({ nodeId: "..." })` ← reading
   - `update_knowledge_node({ id: "..." })` ← writing
   - `move_knowledge_node({ id: "..." })` ← moving

3. **AI transparency footer** — Every published document must end with:
   ```
   ---
   Generado con AI (tecnologia-morelos-workflow v0.1.0), revisado por [nombre]
   ```

## Creating a new KB for a project

```
create_knowledge_base({
  projectId: "<project_id>",
  title: "[Project Name]",
  description: "Documentation for [Project Name]"
})
```

## Creating nodes

```
create_knowledge_node({
  knowledgeBaseId: "<kb_id>",
  title: "Document Title",
  documentType: "PAGE",           // PAGE, GUIDE, or API_REFERENCE
  content: "markdown content...",
  parentId: "<parent_folder_id>"  // optional — for nesting inside a folder
})
```

For folders:
```
create_knowledge_node({
  knowledgeBaseId: "<kb_id>",
  title: "Folder Name",
  nodeType: "FOLDER",
  parentId: "<parent_id>"
})
```

## Markdoc rules

See [markdoc-reference.md](markdoc-reference.md) for detailed rules and
[gotchas.md](gotchas.md) for known TM MCP issues.

**The #1 rule**: Code blocks (triple backtick) must be OUTSIDE
`{% accordion %}`, `{% step %}`, `{% card %}`. Only `{% codegroup %}`
accepts code blocks inside.

Mermaid diagrams must also be OUTSIDE any Markdoc component.

## Publishing checklist

- [ ] Read current content with `get_knowledge_node` before editing
- [ ] Used `id` (not `nodeId`) in `update_knowledge_node`
- [ ] No code blocks inside accordion/step/card components
- [ ] Mermaid diagrams are outside Markdoc components
- [ ] AI transparency footer is included
- [ ] User approved the content before publishing
