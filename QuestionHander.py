import sqlite3
import datetime

from DB_handler import DB_handler

class QuestionHandler(DB_handler):
    def __init__(self):
        super().__init__()

    def questionIDExists(self, id):
        if self.getQuestion(id):
            return True
        else:
            return False

    def getAllQuestions(self):
        # Responsiblity:
        # get all questions from the database
        getQuestionsQuery = "SELECT questionID, question, explanation, rightAnswer, dateAdded, creatorID, A, B, C, D, E, F FROM question"
        try:
            self._DBoperator.execute(getQuestionsQuery)
            #print(self._DBoperator.fetchall())
            return self._DBoperator.fetchall()
        except sqlite3.OperationalError as error:
            print(error)

    def getQuestion(self, questionid):
        # Responsibility:
        # get the question with the provided questionid
        getQuestionQuery = "SELECT questionID, question, explanation, rightAnswer, dateAdded, creatorID, A, B, C, D, E, F FROM question WHERE questionID = ?"
        try:
            self._DBoperator.execute(getQuestionQuery, (questionid,))
            return self._DBoperator.fetchone()
        except sqlite3.OperationalError as error:
            print(error)

    def getQuestionforQuiz(self, quizid):
        # Responsibility:
        # get all questions for the provided quizid
        getQuestionforQuizQuery = "SELECT question.questionID, question.question, question.explanation, question.rightAnswer, question.dateAdded, question.creatorID, question.A, question.B, question.C, question.D, question.E, question.F FROM question, quizQuestion, quiz WHERE  quiz.quizID = quizQuestion.quizID AND question.questionID = quizQuestion.questionID AND quiz.quizID = ?"
        print(getQuestionforQuizQuery)
        print("Gonna get questions for quiz", quizid)
        try:
            self._DBoperator.execute(getQuestionforQuizQuery, (quizid))
            return self._DBoperator.fetchall()
        except sqlite3.OperationalError as error:
            print(error)

    def getQuestionforSubject(self, subjectid, random = None, maximum = None):
        # Responsibility:
        # get all questions for the provided quizid
        if not random:
            getQuestionforSubjectQuery = "SELECT question.questionID, question.question, question.explanation, question.rightAnswer, question.dateAdded, question.creatorID, question.A, question.B, question.C, question.D, question.E, question.F FROM question, questionSubject, subject WHERE  subject.subjectID = questionSubject.subjectID AND question.questionID = questionSubject.questionID AND subject.subjectID = ?"
        else:
            getQuestionforSubjectQuery = "SELECT question.questionID, question.question, question.explanation, question.rightAnswer, question.dateAdded, question.creatorID, question.A, question.B, question.C, question.D, question.E, question.F FROM question, questionSubject, subject WHERE  subject.subjectID = questionSubject.subjectID AND question.questionID = questionSubject.questionID AND subject.subjectID = ? ORDER BY RANDOM() LIMIT ?"
        try:
            self._DBoperator.execute(getQuestionforSubjectQuery, (subjectid, maximum))
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
            return True
        except sqlite3.OperationalError as error:
            print(error)

    def addQuestionToQuiz(self, questionid, quizid):
        # Responsiblity:
        # insert the provided questionid and subjectid into the questionSubject table
        insertQuestionQuizQuery = "INSERT into quizQuestion (questionID, quizid) VALUES (?, ?)"
        print(insertQuestionQuizQuery)
        print("adding quiz ", quizid, " and question ",questionid)
        try:
            self._DBoperator.execute(insertQuestionQuizQuery,
                                   (questionid, quizid))
            self._conn.commit()
            return True
        except sqlite3.OperationalError as error:
            print(error)
            return False

    def removeQuestionFromQuiz(self, questionid, quizid):
        # Responsiblity:
        # remove the provided questionid and subjectid from the questionSubject table
        removeQuestionQuizQuery = "DELETE from quizQuestion WHERE questionID = ? AND quizID = ?"
        print(removeQuestionQuizQuery)
        print("removing quiz ", quizid, " and question ",questionid)
        try:
            self._DBoperator.execute(removeQuestionQuizQuery, (questionid, quizid))
            self._conn.commit()
        except sqlite3.OperationalError as error:
            print(error)
            return False

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

    def editQuestion(self, questionID, question, answerA, answerB, explanation, creatorID, rightAnswer, answerC=None, answerD=None, answerE=None, answerF=None):
        # Responsiblity:
        # edit the question with the provided questionID
        editQuestionQuery = "UPDATE question SET question = ?, A = ?, B = ?, C = ?, D = ?, E = ?, F = ?, rightAnswer = ?, explanation = ? WHERE questionID = ?"
        try:
            self._DBoperator.execute(editQuestionQuery,
                                   (question, answerA, answerB, answerC, answerD, answerE, answerF, rightAnswer, explanation, questionID))
            self._conn.commit()
        except sqlite3.OperationalError as error:
            print(error)