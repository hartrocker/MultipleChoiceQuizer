import tkinter as tk

from ResultHandler import ResultHandler
from WorkframeUI import WorkframeUI
from DB_handler import DB_handler
from QuestionHander import QuestionHandler
from SubjectHandler import SubjectHandler
#from QuizHandler import QuizHandler
#from ResultHandler import ResultHandler

BUTTONPADDINGX = 3
BUTTONPADDINGY = 3
BUTTONWIDTH = 25
BUTTONHEIGHT = 2


class TeacherUI():
    def __init__(self, root):
        #self.canvasBuilder()
        self.__DBhandler = DB_handler()
        self.__authorized = False
        self.window = root
        self.window.title("Quiz manager")
        self.window.geometry("1200x800")
        self.screen = None
        self.screen = tk.Canvas(self.window, width=1200, height=800)
        self.screen.config()
        self.buildMainInterface()
        self.WorkFrame = tk.Frame(self.window)
        self.WorkFrameUI = WorkframeUI(self.WorkFrame)
        self.WorkFrameUI.buildAddQuestionInterface()

    def buildMainInterface(self):
        # Responsiblity:
        # Build the main interface for teachers
        # It's the menu up top with the colored buttons and the login box.
        self.menuFrame = tk.Frame(self.window)
        self.menuFrame.grid(row=1, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY, sticky="nw")

        self.__buttonMakeQuestion = tk.Button(
            self.menuFrame,
            text="Make Question",
            width=BUTTONWIDTH,
            height=BUTTONHEIGHT,
            bg='aquamarine',
            command=lambda: self.makeQuestion()
        )
        self.__buttonMakeQuestion.grid(row=1, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)

        self.__buttonMakeQuiz = tk.Button(
            self.menuFrame,
            text="Make Quiz",
            width=BUTTONWIDTH,
            height=BUTTONHEIGHT,
            bg='aquamarine',
            command=lambda: self.makeQuiz()
        )
        self.__buttonMakeQuiz.grid(row=1, column=2, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)

        self.__buttonEditQuestion = tk.Button(
            self.menuFrame,
            text="Edit Question",
            width=BUTTONWIDTH,
            height=BUTTONHEIGHT,
            bg='khaki',
            command=lambda: self.WorkFrameUI.pickQuestionInterface()
        )
        self.__buttonEditQuestion.grid(row=2, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)

        self.__buttonAddQuestionToQuiz = tk.Button(
            self.menuFrame,
            text="Add Question to Quiz",
            width=BUTTONWIDTH,
            height=BUTTONHEIGHT,
            bg='khaki',
            command=lambda: self.WorkFrameUI.buildChooseQuizInterface(type="add")
        )
        self.__buttonAddQuestionToQuiz.grid(row=2, column=2, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)

        self.__buttonRemoveQuestionFromQuiz = tk.Button(
            self.menuFrame,
            text="Remove Question from Quiz",
            width=BUTTONWIDTH,
            height=BUTTONHEIGHT,
            bg='khaki',
            command=lambda: self.WorkFrameUI.buildChooseQuizInterface(type="remove")
        )
        self.__buttonRemoveQuestionFromQuiz.grid(row=2, column=3, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)

        self.__buttonDeleteQuestion = tk.Button(
            self.menuFrame,
            text="Delete Question",
            width=BUTTONWIDTH,
            height=BUTTONHEIGHT,
            bg='coral',
            command=lambda: self.deleteQuestion()
        )
        self.__buttonDeleteQuestion.grid(row=3, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)

        self.__buttonDeleteQuiz = tk.Button(
            self.menuFrame,
            text="Delete Quiz",
            width=BUTTONWIDTH,
            height=BUTTONHEIGHT,
            bg='coral',
            command=lambda: self.deleteQuiz()
        )
        self.__buttonDeleteQuiz.grid(row=3, column=2, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)

        self.__buttonDeleteQuiz = tk.Button(
            self.menuFrame,
            text="See Results",
            width=BUTTONWIDTH,
            height=BUTTONHEIGHT,
            bg='CornflowerBlue',
            command=lambda: self.seeResults()
        )
        self.__buttonDeleteQuiz.grid(row=3, column=3, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)

        # Makes sure the empty space is filled up so the login aligns to the right
        self.window.columnconfigure(4, weight=1)


        self.loginFrame = tk.Frame(self.window)
        self.loginFrame.grid(row=1, column=5, rowspan=3, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY, sticky="ne")

        self.__enterUsername= tk.Entry(self.loginFrame)
        self.__enterUsername.grid(row=1, column=8, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
        self.__enterPassword = tk.Entry(self.loginFrame)
        self.__enterPassword.grid(row=2, column=8, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
        self.__buttonAuthorize = tk.Button(
            self.loginFrame,
            text="Login",
            width=BUTTONWIDTH,
            height=BUTTONHEIGHT,
            bg='CornflowerBlue',
            command=lambda: self.authorize()
        )
        self.__buttonAuthorize.grid(row=3, column=8, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)

        #self.screen.grid(row=4, column=1, rowspan=1, columnspan=8)

    # MdL: all the functions below here are just a step to make sure the user is authorized before calling the right function in the interface
    # MdL: The 'logged in' variable is set in this class
    # MdL: Captain hindsight is wondering now if this was the right choice, since this feels kinda redundant.

    def makeQuestion(self):
        # Responsiblity:
        # If the user is authorized, build the add question interface.
        if self.__authorized:
            print("authorized, good to go")
            self.WorkFrameUI.buildAddQuestionInterface()
        else:
            self.__showUsername = tk.Label(self.window, text="Not logged in")
            print("Not authorized")
        #self.removeAddQuestionInterface()

    def makeQuiz(self):
        # Responsiblity:
        # If the user is authorized, build the add quiz interface.
        if self.__authorized:
            print("authorized, good to go")
            self.WorkFrameUI.buildAddQuizInterface()
        else:
            self.__showUsername = tk.Label(self.window, text="Not logged in")
            print("Not authorized")

    def editQuestion(self):
        # Responsiblity:
        # If the user is authorized, build the add quiz interface.
        if self.__authorized:
            print("authorized, good to go")
            self.WorkFrameUI.buildEditQuizInterface()
        else:
            self.__showUsername = tk.Label(self.window, text="Not logged in")
            print("Not authorized")
    def addQuestionToQuiz(self):
        pass
    def removeQuestionFromQuiz(self):
        pass
    def deleteQuestion(self):
        pass
    def deleteQuiz(self):
        pass
    def seeResults(self):
        if self.__authorized:
            print("authorized, good to go")
            self.resultHandler.buildSeeResultsInterface()
        else:
            self.__showUsername = tk.Label(self.window, text="Not logged in")
            print("Not authorized")

    def authorize(self):
        # Responsiblity:
        # Check if the entered username and password are correct.
        # If they are, set the authorized variable to True.
        if self.__DBhandler.authorizeTeacher(self.__enterUsername.get(), self.__enterPassword.get()):
            self.__authorized = True
            print("Authorized")
            self.__showUsername = tk.Label(self.window, text="User: " + self.__enterUsername.get())
            self.__showUsername.grid(row=1, column=7, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
            self.__teacherID = self.__DBhandler.getTeacherID(self.__enterUsername.get())
            self.WorkFrameUI.setTeacherID(self.__teacherID)
            self.__enterUsername.delete(0, tk.END)
            self.__enterPassword.delete(0, tk.END)
        else:
            self.__authorized = False
            print("Not authorized")

    ''' not necesary
    def handleRightAnswer(self):
         
        self.__selectedRightAnswer = self.__rightAnswer.get()
    '''

    ''' moved to QuestionHandler'''
    '''
    def saveQuestion(self):
        A = self.__answerAEntry.get()
        B = self.__answerBEntry.get()
        C = self.__answerCEntry.get()
        D = self.__answerDEntry.get()
        E = self.__answerEEntry.get()
        F = self.__answerFEntry.get()
        rightAnswer = self.__rightAnswer.get()
        question = self.__questionEntry.get()
        explanation = self.__explanationEntry.get()
        teacherID = self.__teacherID
        checklist = [A, B, rightAnswer, question, explanation, teacherID]
        for item in checklist:
            if item == "":
                print("Missing item ", item)
                return
        self.__questionHandler.insertQuestion(question, A, B, explanation, teacherID, rightAnswer,  C, D, E, F)
        '''



def main():
    # Responsibility: Starts the Logo Grader application.
    root = tk.Tk()
    window = TeacherUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()