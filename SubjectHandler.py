import sqlite3


from DB_handler import DB_handler

class SubjectHandler(DB_handler):
    def __init__(self):
        super().__init__()


def getSubjects(self):
    # Responsiblity:
    # get all subjects from the database
    getSubjectsQuery = "SELECT * FROM subject"
    try:
        DB_handler._DBoperator.execute(getSubjectsQuery)
        return self._DBoperator.fetchall()
    except sqlite3.OperationalError as error:
        print(error)