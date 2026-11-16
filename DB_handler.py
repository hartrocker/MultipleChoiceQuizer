import sqlite3
import hashlib
import datetime


class DB_handler:
    # Responsibility:
    # handles all general and login database stuff
    def __init__(self):
        self._conn = sqlite3.connect("MCquizer.db")
        self._DBoperator = self._conn.cursor()

    def getLastID(self):
        # Responsibility:
        # get the id for the last inserted row
        # make sure you use it from the right handler class!
        return self._DBoperator.lastrowid

    def getDateString(self):
        # Responsibility:
        # get a Date in stringformat to insert in the DB
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def authorizeTeacher(self, username, password):
        # Responsibility:
        # Check if the username + password combo are present in the database
        hashedPW=self.getHash(password)
        username = username.lower()
        getTeacherQuery = "SELECT teacherID FROM teacher WHERE username = ? AND password = ?"
        try:
            self._DBoperator.execute(getTeacherQuery, (username, hashedPW))
            if self._DBoperator.fetchone():
                return True
            else:
                return False
        except sqlite3.OperationalError as error:
            print(error)

    def getTeacherID(self, username):
        # Responsiblitiy:
        # get the id for the teacher with the parameter username
        getTeacherQuery = "SELECT teacherID FROM teacher WHERE username = ?"
        try:
            self._DBoperator.execute(getTeacherQuery, (username,))
            return self._DBoperator.fetchone()[0]
        except sqlite3.OperationalError as error:
            print(error)

    def getHash(self, password):
        # Responsibility:
        # get the sha512 hash in string format for the provided password
        password = password.encode('utf-8')
        hash_object = hashlib.sha512()
        hash_object.update(password)
        hashstring = hash_object.hexdigest()
        return hashstring




