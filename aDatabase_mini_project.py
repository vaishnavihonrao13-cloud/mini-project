import mysql.connector

con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)
cursor=con.cursor()

def create_database():
    query="CREATE DATABASE IF NOT EXISTS mydatabase"
    cursor.execute(query)
    print("mydatabase created...")

def delete_database():
    query="DROP DATABASE IF EXISTS mydatabase"
    cursor.execute(query)
    print("mydatabase dropped...")

def create_table():
    cursor.execute("USE mydatabase")
    query="""
    CREATE TABLE IF NOT EXISTS student(
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(40) NOT NULL,
        marks INT,
        age INT
    )
    """
    cursor.execute(query)
    print("student table created...")

def insert_data():
    cursor.execute("USE mydatabase")
    query="INSERT INTO student(name,marks,age) VALUES(%s,%s,%s)"
    student=[
        ("vaishnavi",88,21),
        ("priya",65,21),
        ("shruti",89,22),
        ("siddhi",99,24)
    ]
    cursor.executemany(query,student)
    con.commit()
    print("inserted successfully")

def update_data():
    cursor.execute("USE mydatabase")
    query="UPDATE student SET name=%s WHERE id=%s"
    data=("yogita",2)
    cursor.execute(query,data)
    con.commit()
    print("updated...")

def retrive_data():
    cursor.execute("USE mydatabase")
    query="SELECT * FROM student"
    cursor.execute(query)
    data=cursor.fetchall()
    print("student data retrieved...")
    for row in data:
        print(row)

def delete_data():
    cursor.execute("USE mydatabase")
    query="DELETE FROM student"
    cursor.execute(query)
    con.commit()
    print("student data deleted...")

while True:
    print("1. create database")
    print("2. drop database")
    print("3. create table")
    print("4. insert data")
    print("5. update data")
    print("6. retrive data")
    print("7. delete data")

    choice=int(input("enter choice: "))

    if choice==1:
        create_database()
    elif choice==2:
        delete_database()
    elif choice==3:
        create_table()
    elif choice==4:
        insert_data()
    elif choice==5:
        update_data()
    elif choice==6:
        retrive_data()
    elif choice==7:
        delete_data()

        break
    else:
        print("invalid option")

con.close()