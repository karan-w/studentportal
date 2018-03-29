# Student Portal

## Installation
1. Install Python 3.6.5
```
Download Python 3.6.5 from https://www.python.org/downloads/
This will be installed as python3

```

2. Install rest of the dependencies
```
	pip install -r requirements.txt
  
```

3. Download and install MySQL DBMS.
```
    On Linux, run the following commands

        1. sudo apt-get update
        2. sudo apt-get install mysql-server
        3. sudo apt-get install libmysqlclient-dev

```

4. Create the database in your MySQL Server.
```
    1.CREATE DATABASE studentportal_database;

```

4. Create a new user in MySQL Server.
```
	1. CREATE USER 'admin'@'localhost' IDENTIFIED BY '1234';
	2. GRANT ALL ON studentportal_database.* TO 'admin'@'localhost';
```
