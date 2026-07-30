# Static Analysis & CI/CD Reflection

## Research & Learning
* **What is CI/CD?** Continuous Integration (CI) is the practice of automating the integration of code changes from multiple contributors into a single software project. Continuous Deployment (CD) is the practice of automatically deploying those changes to a production environment.
* **Automating Style Checks:** Automating checks like linting and spelling ensures that the codebase remains clean, readable, and professional without requiring manual review for every small detail.
* **Challenges:** Sometimes automated checks can be "too strict" and block a developer from pushing a small fix. Setting up the initial configuration can also be complex.
* **Small vs. Large Teams:** In small teams, CI/CD might just be a simple test runner. In large teams, it includes security scans, performance testing, and complex deployment pipelines across many servers.

## My Strategy
* I have implemented a GitHub Action that runs `markdownlint` to check my document formatting and `cspell` to check for typos.
