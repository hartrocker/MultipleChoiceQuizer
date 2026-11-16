import sqlite3
import hashlib


teacher=input("Enter teacher name: ")
user=input("Enter username: ")
pw = input("Enter password: ").encode('utf-8')

print("password:", pw)
hash_object = hashlib.sha512()
hash_object.update(pw)
hex=hash_object.hexdigest()
print(hex)


conn = sqlite3.connect("../MCquizer.db")
DBoperator = conn.cursor()

DBoperator.execute("""
    CREATE TABLE IF NOT EXISTS teacher
    (
        teacherID   INTEGER PRIMARY KEY,
        teachername TEXT,
        username    TEXT,
        password    TEXT
    )
""")

insertTeacherQuery = "INSERT INTO teacher (teachername, username, password) VALUES (?, ?, ?)"
print (insertTeacherQuery)
try:
    DBoperator = conn.cursor()
    DBoperator.execute(insertTeacherQuery, (teacher, user, hex))
    conn.commit()
except sqlite3.OperationalError as error:
    print(error)