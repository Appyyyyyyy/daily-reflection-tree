## Daily Reflection Tree

This repository contains a deterministic reflection system designed to guide employees through structured end-of-day introspection.

### Structure

- /tree/reflection-tree.tsv → Core decision tree
- /tree/tree-diagram.md → Visual representation
- write-up.md → Design rationale

### Key Features

- Fully deterministic (no LLM at runtime)
- Fixed-option decision tree
- Covers three psychological axes:
  - Locus of Control
  - Contribution vs Entitlement
  - Radius of Concern

### How to Use

The tree can be read directly as structured data or executed via a simple CLI agent (optional Part B).

Each node defines:
- Question or reflection
- Fixed options
- Deterministic transitions
