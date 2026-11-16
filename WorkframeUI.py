import tkinter as tk

from DB_handler import DB_handler
from SubjectHandler import SubjectHandler
from QuestionHander import QuestionHandler
#from QuizHandler import Quizhandler
#from ResutHandler import ResultHandler

BUTTONPADDINGX = 3
BUTTONPADDINGY = 3
BUTTONWIDTH = 25
BUTTONHEIGHT = 2

class WorkframeUI():
    def __init__(self, frame):
        self.frame = frame
        self.__DBhandler = DB_handler()
        self.__subjectHandler = SubjectHandler()
        self.__questionHandler = QuestionHandler()
        #self.__quizHandler = QuizHandler()
        #self.__resultHandler = ResultHandler()
        self.__teacherID = None

    def setTeacherID(self, teacherID):
        # Responsiblity:
        # Set the teacher ID.
        self.__teacherID = teacherID

    """ add a question interface and functions """
    def buildAddQuestionInterface(self):
        # Responsiblity:
        # Build an interface so the teacher can add a question to the database.
        if self.__teacherID is None:
            return
        self.frame.grid(row=5, column=0, columnspan=9, sticky="nsew", padx=10, pady=10)
        self.frame.columnconfigure(2, weight=1)

        for col in range(2, 8):
            self.frame.columnconfigure(col, weight=1)

        # MDL found a nice quick implementation of a radiobutton at https://www.geeksforgeeks.org/python/radiobutton-in-tkinter-python/
        print("Building add question interface radiobuttons")
        self.__rightAnswer = tk.StringVar()
        values = {"1": "A",
                  "2": "B",
                  "3": "C",
                  "4": "D",
                  "5": "E",
                  "6": "F"}
        for (text, value) in values.items():
            tk.Radiobutton(self.frame, text=value, variable=self.__rightAnswer,
                        value=value, indicator=0).grid(row=1+int(text), column=0)

        print("Building add question interface textboxes")
        self.__questionLabel = tk.Label(self.frame, text="Question:")
        self.__questionLabel.grid(row=1, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
        self.__questionEntry = tk.Entry(self.frame)
        self.__questionEntry.grid(row=1, column=2, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY, columnspan=7, sticky="we")
        self.__answerALabel = tk.Label(self.frame, text="Answer A:")
        self.__answerALabel.grid(row=2, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
        self.__answerAEntry = tk.Entry(self.frame)
        self.__answerAEntry.grid(row=2, column=2, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY, columnspan=7, sticky="we")
        self.__answerBLabel = tk.Label(self.frame, text="Answer B:")
        self.__answerBLabel.grid(row=3, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
        self.__answerBEntry = tk.Entry(self.frame)
        self.__answerBEntry.grid(row=3, column=2, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY, columnspan=7, sticky="we")
        self.__answerCLabel = tk.Label(self.frame, text="Answer C:")
        self.__answerCLabel.grid(row=4, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
        self.__answerCEntry = tk.Entry(self.frame)
        self.__answerCEntry.grid(row=4, column=2, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY, columnspan=7, sticky="we")
        self.__answerDLabel = tk.Label(self.frame, text="Answer D:")
        self.__answerDLabel.grid(row=5, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
        self.__answerDEntry = tk.Entry(self.frame)
        self.__answerDEntry.grid(row=5, column=2, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY, columnspan=7, sticky="we")
        self.__answerELabel = tk.Label(self.frame, text="Answer E:")
        self.__answerELabel.grid(row=6, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
        self.__answerEEntry = tk.Entry(self.frame)
        self.__answerEEntry.grid(row=6, column=2, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY, columnspan=7, sticky="we")
        self.__answerFLabel = tk.Label(self.frame, text="Answer F:")
        self.__answerFLabel.grid(row=7, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
        self.__answerFEntry = tk.Entry(self.frame)
        self.__answerFEntry.grid(row=7, column=2, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY, columnspan=7, sticky="we")
        self.__explanationLabel = tk.Label(self.frame, text="Explanation:")
        self.__explanationLabel.grid(row=8, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
        self.__explanationEntry = tk.Entry(self.frame)
        self.__explanationEntry.grid(row=8, column=2, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY, columnspan=7, sticky="we")
        self.__buttonSaveQuestion = tk.Button(self.frame,
            text="Save Question",
            width=BUTTONWIDTH,
            height=BUTTONHEIGHT,
            bg='aquamarine',
            command=lambda: self.saveQuestion()
        )

        # Building the subject checkboxes
        self.__subjects = self.__subjectHandler.getAllSubjects()
        print(self.__subjects)
        tk.Label(self.frame, text="Onderwerpen").grid(row=9, column=1)
        placement = 10
        self.__subjectlist = []
        for row in self.__subjects:
            subject = tk.BooleanVar()
            tk.Checkbutton(self.frame, variable = subject, text=str(row[1])).grid(row=placement, column=1,  sticky="w")
            self.__subjectlist.append(subject)
            placement += 1
        print (self.__subjectlist)

        self.__buttonSaveQuestion.grid(row=50, column=8, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)

    def removeAddQuestionInterface(self):
        # Responsiblity:
        # Remove the add question interface.
        if self.frame is not None:
            self.frame.destroy()
            self.frame = None

    def saveQuestion(self):
        # Responsiblity:
        # If the entered data is valid, save the question to the database.

        if self.__teacherID is None:
            return
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
        questionid = self.__questionHandler.getLastID()
        # get the selected checkboxes into selected
        selected = []
        for option, var in zip(self.__subjects, self.__subjectlist):
            if var.get():
                selected.append(option)
        print("Selected options:", selected)
        # add question/subject record to database for each selected subject
        for subject in selected:
            subject = subject[0]
            print('we gaan een subject toevoegen, namelijk ', subject, ' voor vraag', questionid)
            self.__questionHandler.addQuestionToSubject(questionid, subject)