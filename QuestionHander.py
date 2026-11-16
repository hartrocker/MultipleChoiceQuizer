import sqlite3
import datetime

from DB_handler import DB_handler

class QuestionHandler(DB_handler):
    def __init__(self):
        super().__init__()

    def getAllQuestions(self):
        # Responsiblity:
        # get all questions from the database
        getQuestionsQuery = "SELECT * FROM question"
        try:
            self._DBoperator.execute(getQuestionsQuery)
            print(self._DBoperator.fetchall())
            return self._DBoperator.fetchall()
        except sqlite3.OperationalError as error:
            print(error)

    def getQuestion(self, questionid):
        # Responsibility:
        # get the question with the provided questionid
        getQuestionQuery = "SELECT * FROM question WHERE questionID = ?"
        try:
            self._DBoperator.execute(getQuestionQuery, (questionid,))
            return self._DBoperator.fetchone()
        except sqlite3.OperationalError as error:
            print(error)

    def getQuestionforQuiz(self, quizid):
        # Responsibility:
        # get all questions for the provided quizid
        getQuestionforQuizQuery = "SELECT * FROM question, quizQuestion, quiz WHERE  quiz.quizID = quizQuestion.quizID AND question.questionID = quizQuestion.questionID AND quiz.quizID = ?"
        try:
            self._DBoperator.execute(getQuestionforQuizQuery, (quizid))
            return self._DBoperator.fetchall()
        except sqlite3.OperationalError as error:
            print(error)

    def getQuestionforSubject(self, subjectid):
        # Responsibility:
        # get all questions for the provided quizid
        getQuestionforSubjectQuery = "SELECT * FROM question, questionSubject, subject WHERE  subject.subjectID = questionSubject.subjectID AND question.questionID = questionSubject.questionID AND subject.subjectID = ?"
        try:
            self._DBoperator.execute(getQuestionforSubjectQuery, (subjectid))
            return self._DBoperator.fetchall()
        except sqlite3.OperationalError as error:
            print(error)

    def getCreator(self, questionid):
        # Responsibility:
        # get the creator of the question with the provided questionid
        getCreatorQuery = "SELECT creatorID FROM question WHERE questionID = ?"
        try:
            self._DBoperator.execute(getCreatorQuery, (questionid,))
            return self._DBoperator.fetchone()[0]
        except sqlite3.OperationalError as error:
            print(error)

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

    def editQuestion(self, questionID, question, answerA, answerB, explanation, creatorID, rightAnswer, answerC=None,):
        pass

    def removeQuestion(self, questionID):
        # Responsiblity:
        # remove the question with the provided questionID
        removeQuestionQuery = "DELETE FROM question WHERE questionID = ?"
        try:
            self._DBoperator.execute(removeQuestionQuery, (questionID,))
            self._conn.commit()
        except sqlite3.OperationalError as error:
            print(error)