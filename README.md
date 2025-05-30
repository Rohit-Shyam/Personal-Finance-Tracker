# 💰 Personal Finance Tracker

A simple, console-based **Personal Finance Tracker** written in **Python** to help you manage your income and expenses efficiently. This project allows users to record financial transactions, view summaries within custom date ranges, and visualize their spending and earning patterns using matplotlib.

---

## 📁 Project Structure

```bash
Personal-Finance-Tracker/
├── finance_data.csv # CSV file storing transaction records
├── data_entry.py # User input handling functions
├── main.py # Core logic for transaction handling and visualization
├── Sample Plots/ # Folder with sample date-wise transaction plots
└── pycache/ # Python-generated cache files
```

---

## ✅ Features

- Add new transactions with:
  - 📅 Date (auto or manual)
  - 💵 Amount
  - 📂 Category (Income or Expense)
  - 📝 Optional Description
- Store entries in a persistent CSV file
- Filter and display transactions between custom date ranges
- View summarized results:
  - Total Income
  - Total Expense
  - Net Savings
- 📈 Visualize income vs expenses using **matplotlib** plots

---

## 🛠 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/personal-finance-tracker.git
cd personal-finance-tracker
```

### 2. Install Dependencies
```bash
pip install pandas matplotlib
```

### 3. Run the Application
```bash
python main.py
```

---

## 📊 Sample Output

View a table of transactions between two dates

See a summary of income, expenses, and savings

Generate a line plot of income vs expenses saved in the Sample Plots/ folder

---

```bash
Transaction from 01-03-2025 to 31-03-2025.
       date  amount category   description
   01-03-2025   50.00  Expense    Groceries
   02-03-2025  300.00  Income     Freelance

Summary:
Total Income: $300.00
Total Expense: $50.00
Net Savings: $250.00
```

## 💡 Example Use Cases

📒 Track freelance income and daily expenses

📆 Analyze financial behavior over time

🗂 Maintain a personal offline budget record

📊 Generate visual summaries of your financial activities


---


## 📌 Future Enhancements (Suggestions)
Add category-wise breakdowns (e.g., Rent, Groceries)

Export monthly/weekly reports to PDF/Excel

Build a GUI version using Tkinter or Streamlit

Set personal budget goals and alerts

Add login/user profiles for multi-user tracking


---

### ⭐ If you found this project helpful, give it a star!
### 📬 Feel free to fork it, enhance it, and share your ideas!


---

### ✅ What You Need To Do:
- Replace `yourusername` in GitHub links with your actual GitHub username.
- Replace `your.email@example.com` with your real or public email (optional).
- Optionally, add a screenshot/GIF in the **Sample Output** or **Visual Demo** section.

Let me know if you’d like this version with emojis, GitHub badges, or extra visuals!





