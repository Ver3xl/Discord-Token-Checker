# 🚀 Super Fast Discord Token Checker

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Working-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A high-performance, asynchronous **Discord Token Checker** written in Python. This tool rapidly validates tokens and captures key account details including Nitro status, Available Boosts, and Account Age.

## ✨ Features

-   ⚡ **Super Fast:** Built with `aiohttp` and `asyncio` for blazing fast concurrency.
-   📝 **Detailed Capture:** Logs `Username`, `Nitro Status`, `Boost Availability`, and `Account Age`.
-   📂 **Smart Sorting:** Automatically sorts results into:
    -   `Valid`
    -   `Bad`
    -   `Nitro`
    -   `Capture`
-   🔄 **Flexible Input:** Supports multiple token formats automatically:
    -   `TOKEN`
    -   `"TOKEN"`
    -   `'TOKEN'`
-   🎨 **Beautiful Output:** Clean, color-coded console output using `colorama`.

## 📦 Installation

1.  **Clone the repository** (or download the source code):
    ```bash
    git clone https://github.com/Ver3xl/Discord-Token-Checker.git
    cd token-checker
    ```

2.  **Install dependencies:**
    ```bash
    pip install aiohttp colorama
    ```

## 🛠️ Usage

1.  **Add your tokens** into the `tokens.txt` file (one token per line).
2.  **Run the script:**
    ```bash
    python main.py
    ```
3.  **Check the Results:**
    All results will be saved in the `Result/` folder:
    -   🟢 `Valid_Token.txt`: All working tokens.
    -   💎 `Nitro_Tokens.txt`: Tokens with active Nitro.
    -   📄 `Capture.txt`: Detailed info (Username, Nitro, Boosts, Age).
    -   🔴 `Bad_Tokens.txt`: Invalid or dead tokens.

## ⚠️ Disclaimer

This tool is developed for **educational purposes only**. The developer is not responsible for any misuse of this software. Please respect Discord's Terms of Service and API Guidelines.

---
Made with ❤️ by [Your Name]

