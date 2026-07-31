# Handling Errors & Edge Cases

## Research: Strategies for Robust Code
* **Guard Clauses:** These are checks at the beginning of a function that return early if a condition isn't met. This prevents deeply nested "if" statements and makes the code cleaner.
* **Input Validation:** Checking that the data entering a function is correct (e.g., making sure a number isn't a string or that a required field isn't empty).
* **Graceful Failure:** Ensuring that if an error happens, the app shows a helpful message instead of crashing.

## Code Refactoring Example

### ❌ Original Function (No Error Handling)
This function will crash if the `user` object is missing or if the `score` is not a number.
```javascript
function updateHighScore(user, score) {
  if (score > user.highScore) {
    user.highScore = score;
    return "New record!";
  }
}
---

# Commenting & Documentation

## Research: Best Practices
* **Explain the "Why," not the "What":** Code tells you *what* is happening. Comments should tell you *why* it is happening (e.g., "Retrying because the API is unstable").
* **Self-Documenting Code:** Use clear variable and function names so you don't need a comment to explain them.
* **Keep it updated:** An outdated comment is worse than no comment at all.

## Code Example: Bad vs. Good Comments

### ❌ Poorly Commented Code
```javascript
// Function to add two numbers
function add(a, b) {
  let c = a + b; // add a and b and store in c
  return c; // return the result
}
---

# Refactoring Code for Simplicity

## Research: Refactoring Techniques
* **Extract Method:** If a function is too long, break parts of it into smaller, named functions.
* **Simplify Boolean Expressions:** Instead of complex `if (a == true && b == false)`, use clear logic.
* **Remove Dead Code:** Delete variables or functions that are never used.
* **Replace Loop with Pipeline:** Using modern methods like `.filter()` or `.map()` instead of manual `for` loops.

## Code Example: Over-engineered vs. Simple

### ❌ Over-engineered Code
This code is too long and manually tracks a counter to find active users.
```javascript
function getActiveUsers(users) {
  let activeList = [];
  for (let i = 0; i < users.length; i++) {
    if (users[i].status === 'active') {
      if (users[i].age > 18) {
        activeList.push(users[i]);
      }
    }
  }
  return activeList;
}
