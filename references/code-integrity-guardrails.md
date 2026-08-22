# Code Integrity & Blast Radius Limiter Protocol

## Invariants
1. Changes MUST be isolated exclusively to the exact target line, function, or AST node.
2. The agent is strictly forbidden from modifying surrounding working code.
3. No unrequested renaming of variables, refactoring, or architectural changes.
4. Pre-mutation snapshots must be preserved in `.backups/YYYYMMDD_HHMMSS/`.
5. Diff audit must verify zero drift before declaring task completion.