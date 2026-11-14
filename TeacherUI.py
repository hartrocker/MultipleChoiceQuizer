import sqlite3
import tkinter as tk

BUTTONPADDINGX = 3
BUTTONPADDINGY = 3
BUTTONWIDTH = 25
BUTTONHEIGHT = 2

class TeacherUI():
    def __init__(self, root):
        #self.canvasBuilder()
        self.window = root
        self.window.title("Quiz manager")
        self.window.geometry("1200x800")
        self.screen = None
        self.screen = tk.Canvas(self.window, width=1200, height=800)
        self.screen.config()
        self.buildInterface()

    def buildInterface(self):
        self.__buttonMakeQuestion = tk.Button(
            text="Make Question",
            width=BUTTONWIDTH,
            height=BUTTONHEIGHT,
            bg='aquamarine',
            command=lambda: self.makeQuestion()
        )
        self.__buttonMakeQuestion.grid(row=1, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)

        self.__buttonMakeQuiz = tk.Button(
            text="Make Quiz",
            width=BUTTONWIDTH,
            height=BUTTONHEIGHT,
            bg='aquamarine',
            command=lambda: self.makeQuiz()
        )
        self.__buttonMakeQuiz.grid(row=1, column=2, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)

        self.__buttonEditQuestion = tk.Button(
            text="Edit Question",
            width=BUTTONWIDTH,
            height=BUTTONHEIGHT,
            bg='khaki',
            command=lambda: self.editQuestion()
        )
        self.__buttonEditQuestion.grid(row=2, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)

        self.__buttonAddQuestionToQuiz = tk.Button(
            text="Add Question to Quiz",
            width=BUTTONWIDTH,
            height=BUTTONHEIGHT,
            bg='khaki',
            command=lambda: self.addQuestionToQuiz()
        )
        self.__buttonAddQuestionToQuiz.grid(row=2, column=2, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)

        self.__buttonRemoveQuestionFromQuiz = tk.Button(
            text="Remove Question from Quiz",
            width=BUTTONWIDTH,
            height=BUTTONHEIGHT,
            bg='khaki',
            command=lambda: self.removeQuestionFromQuiz()
        )
        self.__buttonRemoveQuestionFromQuiz.grid(row=2, column=3, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)

        self.__buttonDeleteQuestion = tk.Button(
            text="Delete Question",
            width=BUTTONWIDTH,
            height=BUTTONHEIGHT,
            bg='coral',
            command=lambda: self.deleteQuestion()
        )
        self.__buttonDeleteQuestion.grid(row=3, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)

        self.__buttonDeleteQuiz = tk.Button(
            text="Delete Quiz",
            width=BUTTONWIDTH,
            height=BUTTONHEIGHT,
            bg='coral',
            command=lambda: self.deleteQuiz()
        )
        self.__buttonDeleteQuiz.grid(row=3, column=2, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)

        self.__buttonDeleteQuiz = tk.Button(
            text="See Results",
            width=BUTTONWIDTH,
            height=BUTTONHEIGHT,
            bg='CornflowerBlue',
            command=lambda: self.seeResults()
        )
        self.__buttonDeleteQuiz.grid(row=3, column=3, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)

        self.screen.grid(row=4, column=1, rowspan=1, columnspan=8)

    def makeQuestion(self):
        pass
    def makeQuiz(self):
        pass
    def editQuestion(self):
        pass
    def addQuestionToQuiz(self):
        pass
    def removeQuestionFromQuiz(self):
        pass
    def deleteQuestion(self):
        pass
    def deleteQuiz(self):
        pass
    def seeResults(self):
        pass

def main():
    # Responsibility: Starts the Logo Grader application.
    root = tk.Tk()
    window = TeacherUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()