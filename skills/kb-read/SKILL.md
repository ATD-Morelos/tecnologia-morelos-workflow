---
name: kb-read
description: >
  Search, browse, and read content in Tecnología Morelos knowledge bases.
  Use when checking if a project or document exists, reading current content
  before editing, or exploring the KB structure.
allowed-tools: mcp__tecnologia-morelos__list_projects mcp__tecnologia-morelos__list_knowledge_bases mcp__tecnologia-morelos__list_knowledge_nodes mcp__tecnologia-morelos__list_knowledge_node_children mcp__tecnologia-morelos__get_knowledge_node mcp__tecnologia-morelos__get_document_context mcp__tecnologia-morelos__hybrid_search mcp__tecnologia-morelos__semantic_search mcp__tecnologia-morelos__find_related_knowledge mcp__tecnologia-morelos__get_knowledge_relations mcp__tecnologia-morelos__get_knowledge_tree mcp__tecnologia-morelos__get_knowledge_base_graph_summary
---

# KB Read — Search and Read in Tecnología Morelos

## When to use

- Before creating any document: check if it already exists
- When the user asks about project status: list what docs exist
- When any skill needs to read existing content before generating new content
- When exploring what projects and KBs are available

## Pipeline

### 1. Find the project/KB

```
list_projects()                           → find the project
list_knowledge_bases()                    → find the KB within the project
```

### 2. Browse the tree

```
list_knowledge_nodes({ knowledgeBaseId })  → list all nodes
list_knowledge_node_children({ nodeId })   → browse into folders
get_knowledge_tree({ knowledgeBaseId })     → full tree view
```

### 3. Read content

```
get_knowledge_node({ nodeId })             → read a specific node
get_document_context({ nodeId })           → extended context
```

### 4. Search

```
hybrid_search({ query, knowledgeBaseId })  → best search (uses both keyword + vector)
```

**Do NOT use `search_knowledge`** — it returns results sorted by `updatedAt`, not relevance.

## Additional resources

- For search tool comparison and patterns, see [search-patterns.md](search-patterns.md)

## Status check pattern

To report project status, compare the KB tree against the canonical structure
in [kb-structure.md](../../kb-structure.md). Report which documents exist and
which are missing, organized by gate/phase.
