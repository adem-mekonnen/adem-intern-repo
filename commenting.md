# Commenting & Documentation
*Note: This is a practice example written to demonstrate the concept, not taken from a live project.*
## Research: Best Practices
- **Explain the "Why," not the "What":** Code already shows *what* is happening. Good comments explain *why* it's happening — e.g. "Retrying because the API is unstable" — context that isn't obvious from the code alone.
- **Self-Documenting Code:** Use clear variable and function names so the code explains itself without needing a comment to translate it.
- **Keep it updated:** An outdated comment that no longer matches the code is worse than no comment at all, since it actively misleads the reader.
- **Avoid noise comments:** Don't comment on things that are already obvious from the code (e.g. `i++; // increment i`).
## Code Example: Bad vs. Good Comments
### Poorly Commented Code
```javascript
// Function to add two numbers
function add(a, b) {
  let c = a + b; // add a and b and store in c
  return c; // return the result
}
```
Every comment here just restates what the code already says line by line — it adds no real information.
### Improved Version
```javascript
function add(a, b) {
  return a + b;
}
```
The function is simple enough that clear naming (`add`, `a`, `b`) makes it fully self-explanatory — no comments are needed at all. If this function were more complex (e.g. handling rounding rules or currency conversion), a comment would be worth adding to explain *why* a particular approach was chosen, not to restate the arithmetic itself.

## Reflections

**When should you add comments?**
Comments are worth adding when they explain *why* something is done a certain way — non-obvious business logic, a workaround for a bug or limitation, or reasoning that isn't visible from the code itself (e.g. "Retrying 3 times because the payment API occasionally times out"). They're also useful for documenting public function signatures, expected inputs/outputs, or edge cases a future developer wouldn't otherwise anticipate.

**When should you avoid comments and instead improve the code?**
Comments should be avoided when they simply restate what the code already says (e.g. `// add a and b`), since these add clutter and go stale as the code changes. In these cases, the better fix is to make the code self-documenting — clearer variable and function names, smaller focused functions, and simpler logic — so it doesn't need translation in the first place. If a comment is needed just to explain what a poorly named variable or overly complex line does, that's usually a sign the code itself should be refactored instead.
