# Hostel Management System  

## 📌 Project Overview  
**Hostel Management System** is a **Python-based command-line application** designed to manage hostel records efficiently using a **MySQL database**. It allows users to **add, update, and check hostel records** while maintaining structured data storage. This project ensures **data integrity, ease of access, and simplified hostel record management** through a user-friendly interface.  

## ✨ Features  
- **Admission Form** – Register new students in the hostel.  
- **Status Checking** – View records based on department.  
- **Update Details** – Modify existing student details.  
- **Authorities Access** – Placeholder for future authority-based operations.  
- **Exit** – Terminates the application.  

---

## 🛠 Tech Stack  
- **Programming Language:** Python  
- **Database:** MySQL  
- **Database Connector:** `mysql-connector-python`  

---

## 📂 Project Structure  
```
hostel-management/
├── Hostel Management.py     # Main script to run the application
└── README.md                # Project documentation
```  

---

## 🛠 Prerequisites  
Before running the application, ensure you have the following installed:  
- **Python 3.x**  
- **MySQL Server**  
- **Required Python Package:** `mysql-connector-python`  

### 🔧 Installation & Setup  

1. **Install dependencies:**  
    ```
    pip install mysql-connector-python
    ```

2. **Set up MySQL database:**  
    - Create a database named **`HOSTEL_MANAGEMENT`**.  
    - Run the following SQL script to create the `HOSTEL` table:  

      ```
      CREATE TABLE HOSTEL (
          rgn_no INT PRIMARY KEY,
          name VARCHAR(20),
          address VARCHAR(100),
          room_no INT,
          dept VARCHAR(15),
          fees INT,
          bal INT
      );
      ```

---

## 🚀 Running the Application  

1. **Start the application:**  
    ```
    python "Hostel Management.py"
    ```

2. **Follow the on-screen prompts** to perform various operations like admissions, status checks, and updates.  

---

## 📸 Application Interface  

### **Main Menu**  
```
WELCOME TO HOSTEL MANAGEMENT

MAKE YOUR PREFERENCE:
1. ADMISSION FORM
2. STATUS CHECKING
3. UPDATE DETAILS
4. AUTHORITIES
5. EXIT
```

---

## 🏗 Code Overview  
- **Database Connection:** Manages MySQL connectivity.  
- **`AdmnForm()`** – Handles student admissions.  
- **`StatusCheck()`** – Retrieves records based on the department.  
- **`UpdateDetails()`** – Updates existing student records.
