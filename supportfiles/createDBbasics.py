import sqlite3
import datetime

conn = sqlite3.connect("../MCquizer.db")
DBoperator = conn.cursor()

DBoperator.execute("""
    CREATE TABLE IF NOT EXISTS teacher (
        teacherID INTEGER PRIMARY KEY,
        teachername TEXT,
        username TEXT,
        password TEXT
)
""")

DBoperator.execute("""
    CREATE TABLE IF NOT EXISTS quiz (
        quizID INTEGER PRIMARY KEY,
        quizname TEXT,
        creatorID INTEGER,
        dateAdded datetime,
        FOREIGN KEY (creatorID) REFERENCES teacher(teacherID)
)
""")

DBoperator.execute("""
    CREATE TABLE IF NOT EXISTS subject (
        subjectID INTEGER PRIMARY KEY,
        subjectname TEXT,
        domain TEXT
)
""")

DBoperator.execute("""
    CREATE TABLE IF NOT EXISTS question (
        questionID INTEGER PRIMARY KEY,
        A TEXT,
        B TEXT,
        C TEXT,
        D TEXT,
        E TEXT,
        F TEXT,
        rightAnswer TEXT,
        explanation TEXT,
        creatorID INTEGER,
        dateAdded datetime,
        FOREIGN KEY (creatorID) REFERENCES teacher(teacherID)
)
""")

DBoperator.execute("""
    CREATE TABLE IF NOT EXISTS result (
        resultID INTEGER PRIMARY KEY,
        studentname TEXT,
        studentclass TEXT,
        type TEXT,
        quizID INTENGER,
        subjectID INTEGER,
        noOfQuestions INTEGER,
        timeSpent TEXT,
        score FLOAT,
        dateAdded datetime,
        creatorID INTEGER,
        FOREIGN KEY (quizID) REFERENCES quiz(quizID),
        FOREIGN KEY (subjectID) REFERENCES subject(subjectID)

)
""")

DBoperator.execute("""
    CREATE TABLE IF NOT EXISTS quizQuestion (
        quizID INTEGER,
        questionID INTEGER,
        PRIMARY KEY (quizID, questionID),
        FOREIGN KEY (quizID) REFERENCES quiz(quizID),
        FOREIGN KEY (questionID) REFERENCES question(questionID)    
)
""")

DBoperator.execute("""
    CREATE TABLE IF NOT EXISTS questionSubject (
        subjectID INTEGER,
        questionID INTEGER,
        PRIMARY KEY (subjectID, questionID),
        FOREIGN KEY (subjectID) REFERENCES subject(subjectID),
        FOREIGN KEY (questionID) REFERENCES question(questionID)    
)
""")


#DBoperator.execute(
#    "INSERT INTO students (name, age) VALUES (?, ?)",
#    ("Aarav", 20)
#)

conn.commit()
conn.close()