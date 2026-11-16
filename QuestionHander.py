import sqlite3
import datetime

from DB_handler import DB_handler

class QuestionHandler(DB_handler):
    def __init__(self):
        super().__init__()

    def addQuestionToSubject(self, questionid, subjectid):
        # Responsiblity:
        # insert the provided questionid and subjectid into the questionSubject table
        insertQuestionSubjectQuery = "INSERT into questionSubject (questionID, subjectID) VALUES (?, ?)"
        print(insertQuestionSubjectQuery)
        try:
            self._DBoperator.execute(insertQuestionSubjectQuery,
                                   (questionid, subjectid))
            self._conn.commit()
        except sqlite3.OperationalError as error:
            print(error)


    def insertQuestion(self, question, answerA, answerB, explanation, creatorID, rightAnswer, answerC=None,
                           answerD=None, answerE=None, answerF=None):
        # Responsiblity:
        # insert the provided question into the question table

        insertQuestionQuery = "INSERT INTO question (question, A, B, C, D, E, F, rightAnswer, explanation, dateAdded, creatorID) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        dateAdded = self.getDateString()
        print(insertQuestionQuery)
        try:
            self._DBoperator.execute(insertQuestionQuery,
                                   (question, answerA, answerB, answerC, answerD, answerE, answerF, rightAnswer,
                                    explanation, dateAdded, creatorID))
            self._conn.commit()
        except sqlite3.OperationalError as error:
            print(error)
