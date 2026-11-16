import sqlite3

from DB_handler import DB_handler

class ResultHandler(DB_handler):
    def __init__(self):
        super().__init__()

    def getAllResults(self):
        # Responsibility:
        # get all results from the result table
        getResultsQuery = "SELECT * FROM result"
        try:
            self._DBoperator.execute(getResultsQuery)
            return self._DBoperator.fetchall()
        except sqlite3.OperationalError as error:
            print(error)

    def getResult(self, resultid):
        # Responsibility:
        # get the result with the provided resultid
        getResultQuery = "SELECT * FROM result WHERE resultID = ?"
        try:
            self._DBoperator.execute(getResultQuery, (resultid,))
            return self._DBoperator.fetchone()
        except sqlite3.OperationalError as error:
            print(error)

    def getResultForSubject(self, subjectid):
        # Responsibility:
        # get the results with the provided subjectid
        getSubjectQuery = "SELECT * FROM result WHERE subjectID = ?"
        try:
            self._DBoperator.execute(getSubjectQuery, (subjectid,))
            return self._DBoperator.fetchone()[0]
        except sqlite3.OperationalError as error:
            print(error)

    def getResultForQuiz(self, quizid):
        # Responsibility:
        # get the results with the provided quizid
        getQuizQuery = "SELECT * FROM result WHERE quizID = ?"
        try:
            self._DBoperator.execute(getQuizQuery, (quizid,))
            return self._DBoperator.fetchone()[0]
        except sqlite3.OperationalError as error:
            print(error)

    def getResultForClass(self, studentclass):
        # Responsibility:
        # get the results with the provided schoolclass
        getClassQuery = "SELECT * FROM result WHERE result.studentclass = ?"
        try:
            self._DBoperator.execute(getClassQuery, (studentclass,))
            return self._DBoperator.fetchone()[0]
        except sqlite3.OperationalError as error:
            print(error)

    def addResult(self, studentclass, quiztype, score, goodAnswers, noOfQuestions = None, quizid = None, subjectid = None):
        # Responsibility:
        # insert the provided result into the result table
        dateAdded=self.getDateString()
        insertResultQuery = "INSERT INTO result (studentclass, type, goodAnswers, noOfQuestions, quizid, subjectid) VALUES (?, ?, ?, ?, ?, ?)"
        try:
            self._DBoperator.execute(insertResultQuery, (studentclass, quiztype, score, goodAnswers, noOfQuestions, quizid, subjectid))
            self._conn.commit()
        except sqlite3.OperationalError as error:
            print(error)

    def removeResult(self, resultid):
        # Responsibility:
        # remove the result with the provided resultid
        removeResultQuery = "DELETE FROM result WHERE resultID = ?"
        try:
            self._DBoperator.execute(removeResultQuery, (resultid,))
            self._conn.commit()
        except sqlite3.OperationalError as error:
            print(error)
