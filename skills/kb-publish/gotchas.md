# TM MCP Gotchas

Known issues and workarounds for the Tecnología Morelos MCP.

## 1. `id` vs `nodeId` — different parameter names for the same UUID

The TM API uses two different parameter names for the same node identifier:

| Operation | Parameter name | Example |
|-----------|---------------|---------|
| `get_knowledge_node` | `nodeId` | `get_knowledge_node({ nodeId: "abc-123" })` |
| `update_knowledge_node` | `id` | `update_knowledge_node({ id: "abc-123" })` |
| `move_knowledge_node` | `id` | `move_knowledge_node({ id: "abc-123" })` |
| `delete_knowledge_node` | `id` | `delete_knowledge_node({ id: "abc-123" })` |

**The UUID is the same.** Only the parameter name changes. Using `nodeId` in
an update call (or `id` in a get call) will fail silently or error.

**Rule:** GET uses `nodeId`. Everything else uses `id`.

## 2. `search_knowledge` does not rank by relevance

`search_knowledge` returns results sorted by `updatedAt`, not by relevance
to the query. This means:
- A recently updated but unrelated page may appear before an older exact match
- Full-text matching is unreliable for finding specific content

**Workaround:** Use `hybrid_search` instead. It combines semantic and keyword
search and returns results ranked by relevance score.

```
# Bad — results not ranked by relevance
search_knowledge({ query: "authentication flow" })

# Good — relevance-ranked results
hybrid_search({ query: "authentication flow" })
```

## 3. `list_projects` may not return all projects

The `list_projects` endpoint may not return the complete list of projects,
especially in workspaces with many projects.

**Workaround:** If you're looking for a specific project, also try:
- `hybrid_search` with the project name
- Direct navigation if you know the project ID
- Ask the user to confirm the project exists

## 4. Code blocks inside Markdoc components BREAK the renderer

Code blocks (triple backtick) inside `{% accordion %}`, `{% step %}`, or
`{% card %}` components cause the renderer to break **silently** — the content
simply doesn't display correctly.

**Only `{% codegroup %}` accepts code blocks inside.**

See [markdoc-reference.md](markdoc-reference.md) for correct patterns.

**Symptoms of this bug:**
- Content after the code block disappears
- The component renders partially or not at all
- No error is thrown — it fails silently

## 5. Mermaid inside Markdoc components BREAKS the renderer

Same issue as code blocks: Mermaid diagrams (` ```mermaid `) inside any
Markdoc component will break the renderer.

**Rule:** Mermaid diagrams must always be at the **top level** of the document,
outside any component.

**Correct pattern:**
```
## Architecture

```mermaid
graph LR
    A --> B
```

{% accordion title="Details" %}
The diagram above shows the high-level architecture.
{% /accordion %}
```

**WRONG pattern:**
```
{% accordion title="Architecture" %}
```mermaid
graph LR
    A --> B
```
{% /accordion %}
```

## Summary Checklist

Before publishing any content to TM:

- [ ] Using `nodeId` for GET and `id` for UPDATE/MOVE/DELETE
- [ ] Using `hybrid_search` (not `search_knowledge`) for finding content
- [ ] No code blocks inside accordion, step, or card components
- [ ] No Mermaid inside any Markdoc component
- [ ] Code blocks that need tabs are inside `{% codegroup %}` only
- [ ] Mermaid diagrams are at the top level of the document
