# Data Privacy & Confidentiality Reflection

## Research & Learning

### 1. Key Takeaways from Focus Bear’s Privacy Policy
Focus Bear collects data primarily to help users track their habits and improve focus. The policy emphasizes that data is used to provide the service and is not sold to third parties. Users have control over their data, and the company aims to collect only the minimum information necessary for the app to function.

### 2. Confidential Data Types at Focus Bear
*   **User Data:** Email addresses, specific habit/routine details, and app usage logs.
*   **Company Data:** Internal source code, future product roadmaps, and internal security credentials (API keys/passwords).
*   **Communication:** Internal Discord discussions regarding business strategy or sensitive technical issues.

### 3. Best Practices for Handling Confidential Data
*   **Principle of Least Privilege:** Only access the data you actually need for your current task.
*   **Never Hardcode Secrets:** Avoid putting API keys or passwords directly into the code (use environment variables instead).
*   **Secure Tools:** Use approved password managers and encrypted communication channels.

### 4. Breach Response
If I suspect a data breach or accidentally disclose a secret (like pushing a password to GitHub), I will **immediately notify my supervisor or the CEO (Jeremy)**. Speed is essential to rotate keys or delete exposed data before it is exploited.

---

## Reflection

### Daily Security Steps
In my daily tasks, I will ensure my workstation is locked whenever I step away. I will also double-check my code commits using `git diff` to make sure I am not accidentally uploading sensitive configuration files or personal notes.

### Safe Disposal & Storage
I will store all credentials in a secure password manager rather than in plain text files. Sensitive files that are no longer needed will be permanently deleted rather than left in the "Downloads" or "Trash" folder.

### Common Mistakes to Avoid
A common mistake is "Secret Leaking"—accidentally pushing an API key to a public GitHub repo. This can be avoided by using a `.gitignore` file and using automated tools (like the "Secret Scanning" feature on GitHub) to catch mistakes before they are finalized.

---

## Task Summary
*   **New Habit:** I am adopting the habit of reviewing every line of my code specifically for sensitive information before I commit and push to the repository.
*   **Security Measure:** I will ensure that my GitHub account uses Two-Factor Authentication (2FA) as a primary security measure to protect the company's codebase.
