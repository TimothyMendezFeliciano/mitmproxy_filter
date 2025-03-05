# Windows Web Filtering with mitmproxy

This project sets up **mitmproxy** on Windows to filter web traffic. It blocks **adult websites** while allowing essential services like **WhatsApp, Google, YouTube, and ChatGPT** to function correctly.

## 🚀 Features
- ✅ Blocks access to adult websites.
- ✅ Allows WhatsApp, Google, YouTube, and ChatGPT domains.
- ✅ Automatically configures **Windows Proxy Settings**.
- ✅ Installs mitmproxy's **CA certificate** for HTTPS interception.
- ✅ Runs as a **background process** on Windows.

---

## 📌 Prerequisites
1. **Install Python** (>= 3.8)
   - Download from [python.org](https://www.python.org/)
   - Ensure **Python is added to PATH** during installation.

2. **Install mitmproxy**
   ```sh
   pip install mitmproxy
   ```

---

## 🛠️ Setup Instructions
### **1️⃣ Run the Setup Script**
The script will:
- Enable **Windows proxy** (`127.0.0.1:9090`).
- Install mitmproxy's **CA Certificate**.
- Start mitmproxy in **regular mode** (non-transparent).

Run the script:
```sh
python setup_mitmproxy.py
```

---

### **2️⃣ Start the mitmproxy Filter**
After setting up, run:
```sh
python mitmproxy_filter.py
```
This will:
- Intercept all web requests.
- **Allow** WhatsApp, Google, YouTube, and ChatGPT.
- **Block** adult websites.

---

## ⚙️ **How It Works**
### ✅ **Whitelisted Domains** (Always Allowed)
- WhatsApp: `mmg.whatsapp.net`, `media.whatsapp.net`, `static.whatsapp.net`
- Google: `www.google.com`, `ssl.gstatic.com`, `mtalk.google.com`
- YouTube: `www.youtube.com`, `googlevideo.com`
- ChatGPT: `chatgpt.com`, `ab.chatgpt.com`, `files.oaiusercontent.com`

### ❌ **Blocked Domains**
- `pornhub.com`, `xvideos.com`, `redtube.com`, `onlyfans.com`
- `xxx.com`, `sex.com`, `hentaikey.com`, `brazzers.com`
- **(Full list in `mitmproxy_filter.py`)**

---

## 🛠️ **How to Stop or Reset**
To **disable** mitmproxy filtering:
```sh
python disable_mitmproxy.py
```
This will:
- **Remove proxy settings** from Windows.
- **Uninstall the mitmproxy certificate**.

---

## 📈 **Customization**
- To **block more websites**, add them to the `BLOCKED_DOMAINS` list in `mitmproxy_filter.py`.
- To **whitelist more services**, add them to `WHITELISTED_DOMAINS`.

---

## 🔄 **Auto-Start mitmproxy on Windows Boot**
1. Open **Task Scheduler** (`Win + R`, type `taskschd.msc`).
2. **Create a new task** → Name: `"Mitmproxy Auto Start"`.
3. **Trigger:** `At system startup`.
4. **Action:** `Start a Program` → Use:
   - **Program:** `python`
   - **Arguments:** `"C:\path\to\mitmproxy_filter.py"`
5. **Enable "Run with highest privileges"**.
6. Click **OK**, restart your PC.

---

## 🚀 **Troubleshooting**
| Issue | Solution |
|-------|----------|
| mitmproxy is not blocking sites | Check if Windows proxy is enabled (`Settings → Network → Proxy` → Ensure `127.0.0.1:9090` is set). |
| YouTube, WhatsApp, or ChatGPT are blocked | Ensure their domains are **whitelisted** in `mitmproxy_filter.py`. |
| HTTPS sites show security warnings | Run `python setup_mitmproxy.py` to **install mitmproxy CA certificate**. |
| mitmproxy is not running | Open **Task Manager** (`Ctrl + Shift + Esc`), check if `python.exe` is running in the background. |

---

## 🔥 **Credits**
Createdf with the assistance of ChatGPT-4o.
