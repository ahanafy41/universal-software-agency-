# Custom Knowledge & Reference Ingestion Guide

When working with proprietary SDKs, internal APIs, specialized JSON schemas, or domain-specific language rules, the agency ingests user-provided files in `docs/` and `references/`.

---

## 1. Supported Document Types
- **Markdown Guides (`.md`)**: Human-readable architecture guides, API docs, coding rules.
- **JSON Schemas (`.json`)**: Formal schemas for configuration or data models.
- **Type Definitions (`.d.ts`, `.cs`, `.py`, `.rs`)**: Interface contracts and model signatures.
- **Code Samples (`.py`, `.cs`, `.js`, `.lua`, `.sh`)**: Reference implementations.

---

## 2. Flash-Optimized JSON Indexing (`references_manifest.json`)
To enable fast, hallucination-free retrieval for lightweight and Flash models, the Knowledge Ingestion Subagent indexes references into `references/references_manifest.json`:

```json
{
  "references": [
    {
      "title": "Custom Auth API Spec",
      "file_path": "docs/auth-spec.md",
      "doc_type": "api_spec",
      "summary": "Defines HMAC-SHA256 authentication header and token refresh lifecycle.",
      "key_symbols": [
        "AuthClient.Authenticate(apiKey, secret)",
        "AuthClient.RefreshToken(token)",
        "UserSession"
      ],
      "strict_rules": [
        "Never send plaintext passwords in requests",
        "Tokens expire after 3600 seconds"
      ]
    }
  ]
}
```

---

## 3. Grounded Code Synthesis Rule
1. Worker subagents must cross-reference `references_manifest.json` before writing API calls.
2. If a method is not found in the manifest or reference files, the agent must ask the user for clarification rather than hallucinating an imaginary endpoint.
