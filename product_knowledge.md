# Focus Bear Product Knowledge & Reflection

## Key Takeaways (QA/Automation Perspective)

1.  **Strict Blocking (Grizzly Bear Mode):** The app is designed to be very difficult to bypass. As a QA, I need to test if the "Grizzly Bear" mode correctly blocks system-level shortcuts like Task Manager or Alt+F4.
2.  **Cross-Platform Synchronization:** Focus Bear syncs routines across Windows, Mac, iOS, and Android. A major part of testing will be ensuring that a routine started on a phone correctly updates the status on the desktop app.
3.  **AI-Assisted Categorization:** Instead of just simple URL lists, the app uses AI to decide if a site is work-related. I need to understand the logic behind this to test for "false positives" (sites blocked that shouldn't be).
4.  **Calendar Integration (Late No More):** The app pulls data from Google/Outlook calendars to remind users of meetings. Testing the timing and the "escalating notifications" is a high-priority stability task.

---

## Reflection

### What did you learn about the product that you didn't know before?
I didn't realize how much the app focuses on the biological side of productivity, such as the mandatory micro-breaks for stretching and breathing. I also learned about the "Late No More" feature, which is a clever solution for "time blindness" common in ADHD users.

### Did you spot anything in the help centre that seems out of date?
Yes. Some of the screenshots in the "Adding Habits" guide show a slightly different user interface than the latest Windows version I installed. Specifically, the "More Options" button has moved to a different location in the current build compared to the documentation images.
