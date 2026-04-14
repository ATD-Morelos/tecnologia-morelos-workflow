# Search Patterns — TM MCP

## Recommended: hybrid_search

Combines keyword matching + vector similarity. Best for finding content.

```
hybrid_search({
  query: "authentication OAuth",
  knowledgeBaseId: "<kb_id>",    // optional — scope to a KB
  projectId: "<project_id>",     // optional — scope to a project
  limit: 5,
  fulltextWeight: 0.5,
  vectorWeight: 0.5
})
```

Returns chunks with: `chunkId`, `nodeId`, `nodeTitle`, `nodeSlug`, `content`, `score`.

## Alternative: semantic_search

Pure vector similarity. Good for conceptual queries.

```
semantic_search({
  query: "how does the system handle user authentication",
  knowledgeBaseId: "<kb_id>"
})
```

## Avoid: search_knowledge

Returns results sorted by `updatedAt`, NOT by relevance to the query.
Only use if you need to find recently updated nodes regardless of content.

## Related knowledge

```
find_related_knowledge({ nodeId: "<node_id>" })
get_knowledge_relations({ nodeId: "<node_id>" })
```
