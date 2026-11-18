import sqlite3

from DB_handler import DB_handler

class SubjectHandler(DB_handler):
    def __init__(self):
        super().__init__()

    def subjectIDExists(self, id):
        if self.getSubject(id):
            return True
        else:
            return False

    def getAllSubjects(self):
        # Responsiblity:
        # get all subjects from the database
        getSubjectsQuery = "SELECT * FROM subject"
        try:
            self._DBoperator.execute(getSubjectsQuery)
            return self._DBoperator.fetchall()
        except sqlite3.OperationalError as error:
            print(error)

    def getSubject(self, subjectid):
        # Responsiblity:
        # get the subject with the provided subjectid
        getSubjectQuery = "SELECT * FROM subject WHERE subjectID = ?"
        try:
            self._DBoperator.execute(getSubjectQuery, (subjectid,))
            return self._DBoperator.fetchone()
        except sqlite3.OperationalError as error:
            print(error)

    def getQuestionsForSubject(self, subjectid):
        # Responsiblity:
        # get all questions for the provided subjectid
        getQuestionsForSubjectQuery = "SELECT * FROM question, questionSubject, subject WHERE  subject.subjectID = questionSubject.subjectID AND question.questionID = questionSubject.questionID AND subject.subjectID = ?"
        try:
            self._DBoperator.execute(getQuestionsForSubjectQuery, (subjectid,))
            return self._DBoperator.fetchall()
        except sqlite3.OperationalError as error:
            print(error)

    def getHowManyQuestions(self, subjectid):
        # Responsiblity:
        # get the number of questions for the provided subjectid
        getQuestionsForSubjectQuery = "SELECT COUNT(*) FROM question, questionSubject, subject WHERE  subject.subjectID = questionSubject.subjectID AND question.questionID = questionSubject.questionID AND subject.subjectID = ?"
        try:
            self._DBoperator.execute(getQuestionsForSubjectQuery, (subjectid,))
            return self._DBoperator.fetchone()[0]
        except sqlite3.OperationalError as error:
            print(error)
