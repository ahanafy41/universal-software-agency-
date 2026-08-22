# Live Web & Deep API Research Guide

Procedures for Subagent G when conducting live documentation queries and repository forensics.

## Search Strategy
1. Query official documentation portals first (docs.python.org, learn.microsoft.com, developer.mozilla.org, docs.rs).
2. For specific runtime exceptions, search exact error strings on GitHub Issues and Stack Overflow.
3. Compare at least two authoritative sources before selecting a library or pattern.

## Output Format
Subagent G must return:
- Target API Signature / Class Name
- Minimum SDK/Language Version
- Breaking Changes / Deprecation Notices
- Verified Code Snippet with Source URL