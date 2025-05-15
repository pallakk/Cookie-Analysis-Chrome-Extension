🕵️‍♀️ Website Content Analyzer - Chrome Extension

Website Content Analyzer is a lightweight Chrome extension that scans the visible text on any webpage and detects the presence of important, pre-defined keywords such as password, account number, credit card, email, and login. This tool helps raise awareness of potentially sensitive or important content that may appear on websites.

------------------------------------------------------------
🚀 Features

✅ Detects general keywords on any webpage.
✅ Alerts users if such keywords are found.
✅ Easy to install and use with one-click scanning.
✅ No user data is collected or stored.

------------------------------------------------------------
📂 Project Structure

website-content-analyzer/
├── manifest.json
├── popup.html
├── popup.js
├── style.css
└── icon.png (optional)

------------------------------------------------------------
🛠️ Installation Guide

1. Clone this repository
   git clone https://github.com/pallakk/Cookie-Analysis-Chrome-Extension.git

2. Open Google Chrome and navigate to chrome://extensions/

3. Enable Developer mode (toggle in the top right corner)

4. Click on "Load unpacked" and select the cloned project folder

5. The extension will now appear in your Chrome Extensions toolbar

------------------------------------------------------------
🎯 How to Use

1. Go to any webpage you wish to scan.
2. Click the Website Content Analyzer icon in the Chrome toolbar.
3. In the popup, click "Scan Page".
4. You will receive an alert indicating:
   - Detected keywords, or
   - A message saying no keywords were found.

------------------------------------------------------------
📝 Default Keywords Checked

- age
- height
- disease
- username
- credit card number
- password
- account number
- phone number
- login

------------------------------------------------------------
⚠️ Note:
This extension uses basic keyword matching based on visible text.
It does not perform contextual analysis, NLP processing, or scan hidden elements like JavaScript-generated content.
