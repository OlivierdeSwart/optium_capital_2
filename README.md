# 💼 Optium Capital – Financial Report Generator

This tool lets you generate financial summaries from hundreds of Excel files, using a simple browser-based interface — no coding experience needed.

---

## ✅ What This Tool Does

- Combines multiple Excel files into one unified dataset  
- Lets you search by one or more `ENTITY_ID`s  
- Shows totals and monthly breakdowns for Visa/MasterCard sales and fees  
- Allows you to export reports as Excel files  

---

## 🛠️ First-Time Setup (Windows)

> For users who’ve never used Python or a terminal before.

### 1. 📁 Download and Extract the Project

1. Go to: https://github.com/OlivierdeSwart/optium_capital_2  
2. Click the green **"Code"** button  
3. Choose **"Download ZIP"**  
4. Extract the ZIP file to a location like your Desktop  

---

### 2 📂 Add Your csv Files

Download csv from dropbox. Audrey/2025-4-25%20SWAY%20Project/Monthly%20Comparisons
Place your `.csv` file into the `data/` folder inside the project.  

### 3. 🐍 Install Python

1. Visit: https://www.python.org/downloads/  
2. Click the yellow **Download Python 3.13.3** button  
3. Run the installer  
4. ✅ **Check the box that says "Add Python to PATH"** before continuing  

### 4. 🖥 Open Command Prompt & Navigate

1. Press the **Windows** key, type `command prompt`, and open it  
2. Use the following basics to navigate:

- Go up one level: `cd ..`  
- Go into a folder: `cd folder_name`  
- List contents: `dir`  

Navigate to the folder that contains `requirements.txt`. Example:  
`C:\Users\Olivier\Downloads\optium_capital_2-main`  
Use `dir` to confirm the file is there.

### 5. ⚙️ Set Up and Run the App

Run the following lines one at a time in Command Prompt:

- `py -m venv venv`  
- `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`  
- `venv\Scripts\activate.bat`  
- `pip install -r requirements.txt`  
- `streamlit run app/main.py`  

✅ This sets up your environment and launches the app in your browser.  
If the browser doesn’t open, copy the URL shown in the terminal into your browser manually.

---

## 🔁 Running the App Later

To use the app again:

1. Open **Command Prompt**
2. Navigate to your `optium_capital_2-main` folder (e.g. [ cd desktop/optium_capital_2-main ] or [ cd "C:\Users\eopti\OneDrive\Desktop\optium_capital_2-main" ])
3. Run the following:

- `venv\Scripts\activate.bat`  
- `streamlit run app/main.py`

---

## ❓ Troubleshooting

- Missing Python? Reinstall and make sure you checked **"Add Python to PATH"**  
- Place csv file in the correct `data/` folder  
- No internet connection is required after setup — the app runs locally  

---

## 🔐 100% Local & Private

This tool runs entirely on your computer.  
No data is uploaded or shared — your Excel files stay secure and private.

---

Made to save you hours of manual work! 💼📈
