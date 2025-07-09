# 🔎 Telegram Port Scanner Bot

A simple yet powerful Telegram bot that scans the top 60 common ports of a given **public IP address** and returns banners for open ports. Built with Python and integrated via the Telegram Bot API.

---

## 🚀 Features

* Scan common TCP ports on public IPs
* Banner grabbing for open ports
* Beautiful tree‑style output on Telegram
* Rejects private IP ranges (e.g. `192.168.x.x`)
* Lightweight and fast
* Logs every user interaction with timestamps

---

## ⚙️ Technologies Used

| Purpose               | Tech/Library                                                     |
| --------------------- | ---------------------------------------------------------------- |
| Bot framework         | [`pyTelegramBotAPI`](https://pypi.org/project/pyTelegramBotAPI/) |
| Environment variables | [`python‑dotenv`](https://pypi.org/project/python-dotenv/)       |
| Networking            | Python `socket` module                                           |
| JSON output           | Python `json` module                                             |

---

## 📦 Setup Instructions

### 1  Clone the repository

```bash
git clone https://github.com/Raihan93-coder/telegram-port-scanner-bot.git
cd telegram-port-scanner-bot
```

### 2  Create & activate a virtual environment *(optional but recommended)*

```bash
python3 -m venv env
source env/bin/activate  # Windows → env\Scripts\activate
```

### 3  Install dependencies

```bash
pip install -r requirements.txt
```

### 4  Add your Telegram API token

Create a `.env` file in the project root:

```env
API_TOKEN=123456789:ABCdefGhIJkLmNoPqRsTuVwXyZ
```

> **Never** commit `.env` to version control. It’s already listed in `.gitignore`.

### 5  Run the bot locally

```bash
python telegram.py
```

You can now DM the bot on Telegram:

```text
/start
/scan 8.8.8.8
/result
```

---

## 📄 Bot Commands

| Command             | Description                              |
| ------------------- | ---------------------------------------- |
| `/start`            | Show welcome & usage text                |
| `/scan <public_ip>` | Scan the top 60 ports on the target IP   |
| `/result`           | Return a formatted tree view of the scan |

---

## 📁 Project Structure

```text
.
├── scanner.py           # Port-scan + banner‑grab logic
├── telegram.py          # Telegram bot interface
├── requirements.txt     # Python dependencies
├── .env                 # Your private bot token (ignored by git)
├── .gitignore           # Ignore secrets, logs, venvs, byte‑code
└── README.md            # Documentation (this file)
```

---

## 🔐 Security & Legal Notice

* The bot **refuses to scan private IP ranges** (`10.*`, `172.16‑31.*`, `192.168.*`).
* Unauthorized port scanning is illegal in many jurisdictions. **Only scan systems you own or have explicit permission to test.**
* The author accepts **no liability** for misuse.

---

## 🛠 Sample Output

```
Scan result for 142.250.180.14
├─ 22    SSH‑2.0‑OpenSSH_8.2p1 Ubuntu‑4ubuntu0.10
├─ 80    HTTP/1.1 308 Permanent Redirect
└─ 443   No banner
```

---

## 🧠 Future Improvements

* 🔄 Asynchronous scanning to keep the bot responsive
* 🌐 Optional webhook deployment for zero‑latency sleeps
* 🛡️ Access‑control list to restrict who can run `/scan`
* 🖥  Dockerfile & CI/CD workflow for one‑click deploy
* 🧪 Unit tests for scanner logic

---

## ✨ Author

[**Raihan**](https://github.com/Raihan93-coder)  – Cybersecurity student & red‑team enthusiast.

---

## 🛑 Disclaimer

> This project is **for educational purposes only**. Use it responsibly.

