PROJECT INTRODUCTIONS
Tamil Nadu Travel Planner 
* This project is designed to simplify and enhance your travel planning experience within the districts of Tamilnadu. It is a **desktop-based tourism application** that allows users to explore hotel options across different districts of Tamil Nadu. It provides a simple and interactive interface to view curated hotel data for each district.
* The application is built using **Python (Tkinter)** for the user interface and **MySQL** for data storage.

How It Works:
1.	Enter the district you wish to travel to in the list of choices displayed.
2.	Available hotels, tourist spots and places of sightseeing will be shown.

## Features

* Select any district from a dropdown menu
* View multiple hotels available in that district
* Automatic data cleaning:
* Removes empty values
* Eliminates duplicate entries
* Normalizes inconsistent formatting
* Scrollable interface for better usability
* Fast database querying using MySQL

## Tech Stack

* **Frontend (GUI):** Tkinter (Python)
* **Backend Logic:** Python
* **Database:** MySQL
* **Data Source:** Excel/CSV dataset

## Key Concepts Implemented

* Modular programming (single reusable function for all districts)
* Database connectivity using `mysql.connector`
* Parameterized SQL queries (secure and efficient)
* Data preprocessing and cleaning
* GUI-based interaction design

## Project Structure

```
project/
│
├── tntp.py                  
├── chema.sql         
├── Hotels in Tamil Nadu.xlsx  
└── README.md
```

### 3. Update Database Credentials

In `tntp.py`, update:

```python
con = sql.connect(
    host='localhost',
    user='root',
    passwd='your_password',
    database='T'
)
```

## Dataset Information

The dataset contains:

* Tamil Nadu districts
* Up to 10 hotels per district

Data was preprocessed to handle:
* Missing values
* Duplicate entries
* Inconsistent formatting
---
## Use Case

* Database-driven application development
* GUI design using Python
* Data cleaning and preprocessing techniques
