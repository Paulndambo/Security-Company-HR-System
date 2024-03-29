# Human-Resource-Management-System
This is a simplified Human Resource Management System built using;-
1. Python
2. Django
3. Bootstrap 5
4. sqlite3.

This application provides common human resources management functionality such as;-
1. Employee Records Management.
2. Attendance Records Management.
3. Salary Records Management.
4. Company Equipment & Equipment Issue Records Management.


Upcoming Features;-
1. Task Management.
2. Tax API integration


# How to run
It is assumed that you have Python installed on your system, if not, follow the instructions below;-
1. Download Python from <link>https://www.python.org/downloads/</link>
2. Locate the downloaded file and install it.

With Python installed, you need to create a virtual environment, to do so, follow the instructions below;-
1. Create a new directory call HRMS using ```mkdir Desktop/HRMS```
2. Create virtual environment using 
```sql
    python3 -m venv venv
```
3. Activate the virtual environment using the following command
```sql
source venv/bin/activate
```
4. Clone the project from github, using the following command
```sql
git clone https://github.com/ndambopaul/Human-Resource-Management-System.git

or 
git clone git@github.com:ndambopaul/Human-Resource-Management-System.git 
```
5. Change Directory to cloned folder
```sql 
cd Human-Resource-Management-System
```
6. Then, install required libraries using the following command
```sql 
pip install -r requirements.txt
```

7. Run the project using the following command
```sql 
python manage.py runserver
```