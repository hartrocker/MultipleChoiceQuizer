import sqlite3
import datetime

conn = sqlite3.connect("tempMCquizer.db")
DBoperator = conn.cursor()

DBoperator.execute("""
    CREATE TABLE IF NOT EXISTS question (
        questionID INTEGER PRIMARY KEY,
        question TEXT,
        rightAnswer TEXT,
        explanation TEXT,
        creatorID INTEGER,
        dateAdded datetime,
        A TEXT,
        B TEXT,
        C TEXT,
        D TEXT,
        E TEXT,
        F TEXT,
        FOREIGN KEY (creatorID) REFERENCES teacher(teacherID)
)
""")

