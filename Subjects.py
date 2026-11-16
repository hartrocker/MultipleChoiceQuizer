import sqlite3

__CONN = sqlite3.connect("MCquizer.db")
__DB_OPERATOR = __CONN.cursor()

class Subject:
    def __init__(self, id):
        self.__subjectID = id

    def getID(self):
        return self.__subjectID

    def getSubjectname(self):
        getNameQuery = "SELECT subjectname FROM subject WHERE subjectID = ?"
        try:
            self.__DB_OPERATOR.execute(getNameQuery, (self.__subjectID))
            if self.__DB_OPERATOR.fetchone():
                subjectname = self.__DB_OPERATOR.fetchone()[0]
                return subjectname
            else:
                return False
        except sqlite3.OperationalError as error:
            print(error)

    def getdomain(self):
        getDOmainQuery = "SELECT domain FROM subject WHERE subjectID = ?"
        try:
            self.__DB_OPERATOR.execute(getDomainQuery, (self.__subjectID))
            if self.__DB_OPERATOR.fetchone():
                domain = self.__DB_OPERATOR.fetchone()[0]
                return domain
            else:
                return False
        except sqlite3.OperationalError as error:
            print(error)

