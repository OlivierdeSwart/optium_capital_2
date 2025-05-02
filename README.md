# 📊 Financial Report Generator

This tool lets you generate financial summaries from hundreds of Excel files, using a simple browser-based interface — no coding experience needed.

---

## ✅ What This Tool Does

- Combines multiple Excel files into one unified dataset
- Lets you search by one or more ENTITY_IDs
- Shows totals and monthly breakdowns for Visa/MasterCard sales and fees
- Allows you to export reports as Excel files

---

## 🛠️ Setup Instructions (for Windows or Mac)

Assumes:  
✅ You don't have Python installed  
✅ You’ve never used VS Code or a terminal

### 1. 📁 Download and Extract This Project

1. Visit the GitHub repo page https://github.com/OlivierdeSwart/optium_capital
2. Click the green **"Code"** button
3. Choose **"Download ZIP"**
4. Unzip it somewhere easy to find (like your Desktop)

### 2. 🐍 Install Python

If you don’t have Python installed:

1. Go to https://www.python.org/downloads/
2. Click **Download Python**
3. Run the installer
4. ✅ On Windows: **Check the box that says "Add Python to PATH"**

### 3. 📦 Install Required Libraries

1. Open the folder where you extracted the project
2. Windows: Click in the folder bar (top of File Explorer) 
   Type `cmd` (on Windows) or open **Terminal** (on Mac), then press Enter
   Mac: hit command + space bar at the same time. 
   Type terminal and hit enter
3. In the window that opens, make sure you are at the correct folder: optium_capital. Then run:

```bash
pip install -r requirements.txt
```

This installs the necessary packages (Streamlit, pandas, Excel support, etc.)

### 4. ▶️ Run the App

Still in that same terminal, run:

```bash
python run.py
```

This will open the app in your browser.  
(If it doesn’t, just copy the link shown in the terminal into your browser.)

### 5. 📂 Add Your Excel Files

Place all `.xlsx` files into the `data/` folder inside the project.  
Each file should be a monthly financial report like the ones you've used before.

---

## ❓ Troubleshooting

- If you see an error about missing Python, recheck that it’s installed
- Make sure `.xlsx` files go in the correct folder
- The tool does **not** need internet to run

---

## 🔐 Private & Local

This tool runs entirely on your machine. No data is sent anywhere — your Excel files never leave your computer.

---

Made to save you hours of manual work!
