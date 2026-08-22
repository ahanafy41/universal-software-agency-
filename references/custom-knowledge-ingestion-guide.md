# Custom Knowledge & Reference Ingestion Guide

Guide for ingesting user documentation, custom JSON schemas, and SDK manuals into the agency workflow.

## Steps
1. Scan `docs/` and `references/` directories for user-provided Markdown guides and schemas.
2. Compile `references_manifest.json` indexing all available symbols, schemas, and constraints.
3. Enforce user-provided specifications as absolute ground truth (Zero-Hallucination guarantee).