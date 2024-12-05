# Bank Account System

### Overview
This project is a Python-based Bank Account System that simulates basic banking operations, such as deposits, withdrawals, and transaction logging. The program maintains a running balance and writes all activities to a log file named `bankActivities.txt`.

---

### Features
- **Deposit Funds**: Add money to the account.
- **Withdraw Funds**: Deduct money from the account.
- **Activity Logging**: All transactions are recorded in the `bankActivities.txt` file.
- **Initial Balance Setup**:
  - Users can input an initial balance when prompted.
  - If an invalid or no input is provided, a default balance of **50,000** is used.

---

### How It Works
1. The program starts by asking the user to input an **initial balance**:
   - If valid input is provided, it is used as the starting balance.
   - Otherwise, a default balance of **50,000** is assigned.
2. All actions are logged in the file `bankActivities.txt`, including the starting balance.
3. Users can perform the following actions:
   - **Deposit**: Add a specified amount to the balance.
   - **Withdraw**: Deduct a specified amount from the balance.
   - **Stop**: Exit the program.

---

### How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/DvirUliel/Python-Bank-Acount-System.git
2. Navigate to the project directory:
   ```bash
   cd Python-Bank-Acount-System
3. Run the script using:
   ```bash
   python Project.py
4. Follow the on-screen prompts to:
   - Enter an initial balance or accept the default.
   - Perform deposit or withdrawal actions.
   - Exit by typing "stop".
