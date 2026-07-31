# Identifying & Fixing Code Smells

## 1. Magic Numbers & Strings
**Smelly:**
```javascript
if (user.status === 1) { // What is 1?
  setTimeout(doSomething, 86400); // What is 86400?
}
Refactored:
code
JavaScript
const STATUS_ACTIVE = 1;
const SECONDS_IN_A_DAY = 86400;

if (user.status === STATUS_ACTIVE) {
  setTimeout(doSomething, SECONDS_IN_A_DAY);
}
2. Deeply Nested Conditionals
Smelly:
code
JavaScript
function getDiscount(user) {
  if (user.isLoggedIn) {
    if (user.isPremium) {
      if (user.yearsActive > 5) {
        return 0.2;
      }
    }
  }
  return 0;
}
Refactored (Using Guard Clauses):
code
JavaScript
function getDiscount(user) {
  if (!user.isLoggedIn || !user.isPremium || user.yearsActive <= 5) return 0;
  return 0.2;
}
3. Duplicate Code & Long Functions
Smelly:
code
JavaScript
function processOrder(order) {
  // Long logic for calculation...
  let tax = order.price * 0.1;
  let total = order.price + tax;
  console.log("Total is " + total);
  
  // Duplicate logic elsewhere for invoices...
  let invTax = invoice.price * 0.1;
  let invTotal = invoice.price + invTax;
  console.log("Total is " + invTotal);
}
Refactored:
code
JavaScript
const calculateTotal = (price) => price * 1.1;

function processOrder(order) {
  console.log("Total is " + calculateTotal(order.price));
}
4. Inconsistent Naming & Commented-Out Code
Smelly:
code
JavaScript
let x = 10; // What is x?
// let oldVal = 5;  <-- Unused clutter
let User_Name = "Adem"; // Snake_case
let userEmail = "adem@mail.com"; // camelCase
Refactored:
code
JavaScript
let maxRetryCount = 10;
let userName = "Adem";
let userEmail = "adem@mail.com"; 
