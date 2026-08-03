# Interacting with Native Windows UI Elements

## Research & Practice
I used **Accessibility Insights** to map out the UI tree of the Windows Calculator. I successfully automated a basic math operation and verified that the output displayed on the screen matched the expected result.

## Reflection

### How do you locate and interact with Windows UI elements in Pywinauto?
I use the `child_window()` method to search the application's UI tree. Once an element is located, I use methods like `.click()` for buttons, `.type_keys()` for text inputs, and `.select()` for dropdown items.

### What are the different ways to find elements?
*   **automation_id:** This is the preferred method because IDs are usually unique and don't change if the app's language changes.
*   **name:** Useful when an ID isn't available (e.g., the text shown on a label).
*   **control_type:** Helps narrow down the search (e.g., searching for a "Button" specifically).
*   **title:** Used for main windows or specific dialog titles.

### How would you handle UI elements that load dynamically?
I use the `.wait()` or `.wait_not()` functions. Instead of hard-coding a "sleep" timer, I tell the script to wait until an element is `'visible'` or `'ready'`. This makes the test faster and less likely to fail if the computer is running slowly.

### What are common challenges when automating native Windows UI?
*   **Nesting:** Some elements are buried deep inside "Containers" or "Groups," making them hard to find without a specific search path.
*   **Focus Issues:** Sometimes a window needs to be brought to the front (`.set_focus()`) before it will accept clicks.
*   **Non-Standard Controls:** Custom-built buttons (often found in apps like Focus Bear) might not have standard IDs, requiring me to find them by their coordinates or relative position.
# Interacting with Native Windows UI Elements

## Research & Practice
I used **Accessibility Insights** to map out the UI tree of the Windows Calculator. I successfully automated a basic math operation and verified that the output displayed on the screen matched the expected result using conditional logic in Python.

## Reflection

### How do you locate and interact with Windows UI elements in Pywinauto?
I use the `child_window()` method to search the application's UI tree. Once an element is located, I use methods like `.click()` for buttons, `.type_keys()` for text inputs, and `.window_text()` to extract data for verification.

### What are the different ways to find elements?
*   **automation_id:** The most reliable method because IDs are usually unique and static.
*   **name:** Useful when an ID isn't available (e.g., searching for the text "Save").
*   **control_type:** Helps narrow down the search (e.g., looking for a "Button" vs a "Text" element).
*   **title:** Used for main windows or specific dialog titles.

### How would you handle UI elements that load dynamically?
I use the `.wait()` or `.wait_not()` functions. Instead of hard-coding a "sleep" timer, I tell the script to wait until an element is `'visible'` or `'ready'`. This makes the test faster and prevents "flaky" tests if the app takes a moment to respond.

### What are common challenges when automating native Windows UI?
*   **Nesting:** Some elements are buried deep inside "Containers" or "Groups," making them hard to find without a specific search path.
*   **Focus Issues:** Sometimes a window needs to be brought to the front (`.set_focus()`) before it will accept keyboard input.
*   **Resolution/Scaling:** Differences in Windows display scaling (100% vs 125%) can sometimes cause click offsets, making `click_input()` more reliable as it simulates real mouse clicks.
