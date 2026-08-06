# Handling Errors & Edge Cases

## Research: Strategies for Robust Code
* **Guard Clauses:** Checks at the beginning of a function that return early if a condition isn't met. This prevents deeply nested "if" statements and keeps logic flat.
* **Input Validation:** Ensuring data is the correct type (e.g., ensuring a score is a number, not a string) before processing.
* **Graceful Failure:** Returning a helpful message instead of allowing the app to crash.

## Code Refactoring Example

### ❌ Original Function (No Error Handling)
This function is fragile because it assumes the `user` exists. It will crash if `user` is null.
```javascript
function updateHighScore(user, score) {
  if (score > user.highScore) {
    user.highScore = score;
    return "New record!";
  }
}
function updateHighScore(user, score) {
  // 1. Guard clause: reject if user object is missing or malformed
  if (!user || typeof user !== 'object') {
    return "Error: invalid user provided.";
  }

  // 2. Guard clause: reject if score isn't a valid number
  if (typeof score !== 'number' || isNaN(score)) {
    return "Error: score must be a valid number.";
  }

  // 3. Handle missing property edge case: Default highScore to 0
  if (typeof user.highScore !== 'number') {
    user.highScore = 0;
  }

  // Core Logic: Only runs if all guards pass
  if (score > user.highScore) {
    user.highScore = score;
    return "New record!";
  }

  return "Score did not beat the current record.";
}
