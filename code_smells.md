# Identifying & Fixing Code Smells

## 1. Magic Numbers & Strings

**Smelly:**
```javascript
if (user.status === 1) { // What is 1?
  setTimeout(doSomething, 86400); // What is 86400?
}
```

**Refactored:**
```javascript
const STATUS_ACTIVE = 1;
const SECONDS_IN_A_DAY = 86400;

if (user.status === STATUS_ACTIVE) {
  setTimeout(doSomething, SECONDS_IN_A_DAY);
}
```

## 2. Deeply Nested Conditionals

**Smelly:**
```javascript
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
```

**Refactored (Using Guard Clauses):**
```javascript
function getDiscount(user) {
  if (!user.isLoggedIn || !user.isPremium || user.yearsActive <= 5) return 0;
  return 0.2;
}
```

## 3. Duplicate Code & Long Functions

**Smelly:**
```javascript
function processOrder(order) {
  let tax = order.price * 0.1;
  let total = order.price + tax;
  console.log("Total is " + total);
}

function processInvoice(invoice) {
  let invTax = invoice.price * 0.1;
  let invTotal = invoice.price + invTax;
  console.log("Total is " + invTotal);
}
```

**Refactored:**
```javascript
const calculateTotal = (price) => price * 1.1;

function processOrder(order) {
  console.log("Total is " + calculateTotal(order.price));
}

function processInvoice(invoice) {
  console.log("Total is " + calculateTotal(invoice.price));
}
```

## 4. Inconsistent Naming & Commented-Out Code

**Smelly:**
```javascript
let x = 10; // What is x?
// let oldVal = 5;  <-- Unused clutter
let User_Name = "Adem"; // Snake_case
let userEmail = "adem@mail.com"; // camelCase
```

**Refactored:**
```javascript
let maxRetryCount = 10;
let userName = "Adem";
let userEmail = "adem@mail.com";
```

## 5. Large Classes (God Objects)

**Smelly:**
```javascript
class OrderManager {
  constructor(order) {
    this.order = order;
  }

  validateOrder() {
    if (!this.order.items.length) throw new Error("No items in order");
  }

  calculateTotal() {
    return this.order.items.reduce((sum, item) => sum + item.price, 0);
  }

  applyDiscount(total) {
    return total > 100 ? total * 0.9 : total;
  }

  sendConfirmationEmail(email) {
    console.log("Sending confirmation to " + email);
  }

  saveToDatabase() {
    console.log("Saving order to database");
  }

  generateInvoicePdf() {
    console.log("Generating PDF invoice");
  }
}
```

**Refactored (Split by Responsibility):**
```javascript
class OrderValidator {
  validate(order) {
    if (!order.items.length) throw new Error("No items in order");
  }
}

class PriceCalculator {
  calculateTotal(order) {
    return order.items.reduce((sum, item) => sum + item.price, 0);
  }

  applyDiscount(total) {
    return total > 100 ? total * 0.9 : total;
  }
}

class OrderNotifier {
  sendConfirmation(email) {
    console.log("Sending confirmation to " + email);
  }
}

class OrderRepository {
  save(order) {
    console.log("Saving order to database");
  }
}

class InvoiceGenerator {
  generatePdf(order) {
    console.log("Generating PDF invoice for order " + order.id);
  }
}
```
Each class now has exactly one job — validation, pricing, notification, persistence, or invoicing — instead of one `OrderManager` doing all five.

## Reflections

**What code smells did I find?**
I identified magic numbers and strings, deeply nested conditionals, duplicate code, long functions, inconsistent naming, commented-out code, and a large class (God Object). The `OrderManager` class was the most significant find — it combined validation, pricing, notifications, persistence, and invoicing into a single class, making it hard to reason about or change any one piece without risking the others.

**How did refactoring improve readability and maintainability?**
Replacing magic numbers with named constants (`STATUS_ACTIVE`, `SECONDS_IN_A_DAY`) made the intent of each value clear without needing comments. Using guard clauses in `getDiscount` flattened three levels of nesting into a single readable line. Extracting `calculateTotal` removed duplicate tax logic between `processOrder` and `processInvoice`, so a tax rate change now only needs to happen in one place. Standardizing on camelCase and removing dead code cleaned up naming confusion and clutter. Finally, splitting `OrderManager` into `OrderValidator`, `PriceCalculator`, `OrderNotifier`, `OrderRepository`, and `InvoiceGenerator` meant each class could be understood and modified in isolation, without needing to hold the entire order lifecycle in your head at once.

**How will avoiding code smells make future debugging easier?**
With responsibilities isolated and logic simplified, a bug in discount calculation only requires looking at `PriceCalculator`, not scanning a class that also handles emails and database writes. Clear, consistent naming and flattened conditionals make it much faster to trace what code is actually doing, and removing commented-out code eliminates confusion about what's still active. Smaller, single-purpose units narrow the search space significantly when something eventually breaks.
