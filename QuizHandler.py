import sqlite3

from DB_handler import DB_handler

class QuizHandler(DB_handler):
    def __init__(self):
        super().__init__()

    def quizIDExists(self, id):
        if self.getQuiz(id):
            return True
        else:
            return False

    def getAllQuizes(self):
        # Responsibility:
        # get all quizes from the database
        getQuizesQuery = "SELECT * FROM quiz"
        try:
            self._DBoperator.execute(getQuizesQuery)
            return self._DBoperator.fetchall()
        except sqlite3.OperationalError as error:
            print(error)

    def getQuiz(self, quizid):
        # Responsibility:
        # get the quiz with the provided quizid
        getQuizQuery = "SELECT * FROM quiz WHERE quizID = ?"
        try:
            self._DBoperator.execute(getQuizQuery, (quizid,))
            return self._DBoperator.fetchone()
        except sqlite3.OperationalError as error:
            print(error)

    def getQuizesForTeacher(self, teacherid):
        # Responsibility:
        # get all quizes for the provided teacherid
        getQuizesForTeacherQuery = "SELECT * FROM quiz WHERE creatorID = ?"
        try:
            self._DBoperator.execute(getQuizesForTeacherQuery, (teacherid))
            return self._DBoperator.fetchall()
        except sqlite3.OperationalError as error:
            print(error)

    def getQuestionsForQuiz(self, quizid):
        # Responsibility:
        # get all questions for the provided quizid
        getQuesitionsForQuizQuery = "SELECT * FROM question, quizQuestion WHERE quizQuestion.quizID = ? AND question.questionID = quizQuestion.questionID"
        try:
            self._DBoperator.execute(getQuesitionsForQuizQuery, (quizid))
        except sqlite3.OperationalError as error:
            print(error)

    def getCreator(self, quizid):
        # Responsibility:
        # get the creator of the quiz with the provided quizid
        getCreatorQuery = "SELECT creatorID FROM quiz WHERE quizID = ?"
        try:
            self._DBoperator.execute(getCreatorQuery, (quizid,))
            return self._DBoperator.fetchone()[0]
        except sqlite3.OperationalError as error:
            print(error)

    def addQuiz(self, quizname, creatorID):
        # Responsibility:
        # insert the provided quizname and creatorID into the quiz table
        insertQuizQuery = "INSERT into quiz (quizName, creatorID, dateAdded) VALUES (?, ?, ?)"
        dateAdded=self.getDateString()
        try:
            self._DBoperator.execute(insertQuizQuery, (quizname, creatorID, dateAdded))
            self._conn.commit()
            return True
        except sqlite3.OperationalError as error:
            print(error)

    def removeQuiz(self, quizid):
        # Responsibility:
        # remove the quiz with the provided quizid
        removeQuizQuery = "DELETE FROM quiz WHERE quizID = ?"
        try:
            self._DBoperator.execute(removeQuizQuery, (quizid,))
            self._conn.commit()
            return True
        except sqlite3.OperationalError as error:
            print(error)

def main():
    pass

if __name__ == '__main__':
    main()