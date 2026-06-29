# Cyborg Nexus: Professional Development Workflow

This document defines the standard operating procedures for the Cyborg Nexus project, emphasizing high quality, robustness, and efficient "one-pass" delivery.

## 1. Design & Requirements
Before writing a single line of code:
- **Analyze:** Fully understand the requirement, edge cases, and impact on existing code.
- **Architect:** Plan the abstraction, data flow, and interface contract (especially between Go and Flutter).
- **Document:** Update `MIGRATION.md` or relevant documentation with the proposed changes.

## 2. Robust Coding Philosophy ("One-Pass Delivery")
Aiming for "one-pass" doesn't mean rushing; it means doing it *right the first time*.
- **Defensive Programming:** Anticipate failures, validate inputs, and handle errors explicitly (no silent failures).
- **Type Safety:** Leverage Dart's strong typing and Go's static typing. Avoid `dynamic` or `interface{}` whenever possible.
- **Modularity:** Keep functions small, focused, and testable.
- **Consistency:** Follow naming conventions (Flutter: `camelCase`, Go: `PascalCase`/`camelCase` per idiomatic standards).

## 3. Quality Assurance & Testing
No change is complete without verification.
- **Unit Testing:** Mandatory for logic in Go (`_test.go`) and Flutter (`test/`).
- **Integration Testing:** Test the FFI bridge to ensure data passes correctly between Go and Dart.
- **Validation:** Run linting (`flutter analyze`, `go vet`) before submitting.
- **CI/CD:** Every commit should pass local tests.

## 4. Maintenance & Documentation
- **Meaningful Commits:** Each commit must have a clear "why" (e.g., "feat: implement FFI binding for AI provider").
- **Documentation:** Code should be self-documenting. If it's complex, document the *intent* (not just the implementation) in code comments.
- **Review:** Every significant change requires a thoughtful self-review (or peer review).
