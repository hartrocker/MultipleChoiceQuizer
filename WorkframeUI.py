import tkinter as tk

from DB_handler import DB_handler
from SubjectHandler import SubjectHandler
from QuestionHander import QuestionHandler
from QuizHandler import QuizHandler
from ResultHandler import ResultHandler

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
        self.__quizHandler = QuizHandler()
        self.__resultHandler = ResultHandler()
        self.__teacherID = None
        self.frame.grid(row=5, column=0, columnspan=9, sticky="nsew", padx=10, pady=10)
        self.frame.columnconfigure(2, weight=1)

    def setTeacherID(self, teacherID):
        # Responsiblity:
        # Set the teacher ID.
        self.__teacherID = teacherID

    """ add a question interface and functions """
    def buildAddQuestionInterface(self):
        # Responsiblity:
        # Build an interface so the teacher can add a question to the database.
        self.clearInterface()
        if self.__teacherID is None:
            return
        self.frame.grid(row=5, column=0, columnspan=9, sticky="nsew", padx=10, pady=10)
        self.frame.columnconfigure(2, weight=1)

        for col in range(2, 8):
            self.frame.columnconfigure(col, weight=1)

        # MDL found a nice quick implementation of a radiobutton at https://www.geeksforgeeks.org/python/radiobutton-in-tkinter-python/
        # Making the radio checkboxes
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

        # Making the textboxes
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
            command=lambda: self.saveQuestion(type='insert')
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

    def clearInterface(self):
        # Responsiblity:
        # Remove the add question interface.
        for widget in self.frame.winfo_children():
            widget.destroy()


    def saveQuestion(self, type):
        # Responsiblity:
        # If the entered data is valid, save the question to the database.
        print("Saving question")
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
            else:
                print("Caught 'm all")

        # get the selected checkboxes into selected
        if type == 'insert':
            self.__questionHandler.insertQuestion(question, A, B, explanation, teacherID, rightAnswer, C, D, E, F)
            questionid = self.__questionHandler.getLastID()
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
        elif type == 'update':
            self.__questionHandler.editQuestion(self.__editQuestionid, question, A, B, explanation, teacherID, rightAnswer, C, D, E, F)
        self.clearInterface()

    """add quiz interface and functions"""
    def buildAddQuizInterface(self):
        # Responsiblity:
        # Build an interface so the teacher can add a question to the database.
        self.clearInterface()
        if self.__teacherID is None:
            print("je bennie ingelogd doos")
            return
        self.frame.grid(row=5, column=0, columnspan=9, sticky="nsew", padx=10, pady=10)
        self.frame.columnconfigure(2, weight=1)
        self.__quizlabel = tk.Label(self.frame, text="Quiznaam").grid(row=10, column=1)
        self.__quizEntry = tk.Entry(self.frame)
        self.__quizEntry.grid(row=10, column=2, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY, columnspan=7, sticky="we")
        self.__buttonMakeQuiz = tk.Button(
            self.frame,
            text="Make Quiz",
            width=BUTTONWIDTH,
            height=BUTTONHEIGHT,
            bg='aquamarine',
            command=lambda: self.saveQuiz()
        )
        self.__buttonMakeQuiz.grid(row=11, column=8, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)

    def saveQuiz(self):
        quizname = self.__quizEntry.get()
        self.__quizHandler.addQuiz(quizname, self.__teacherID)
        self.clearInterface()

    def buildSeeResultsInterface(self):
        results = self.__resultHandler.getAllResults()
        print(results)
        self.clearInterface()
        tk.Label(self.frame, text="Results").grid(row=1, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
        placement = 2
        for result in results:
            score = float(float(result[7])/float(result[6])*9+1)
            tk.Label(self.frame, text="Quiz: " + result[1] ).grid(row=placement, column=0, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
            tk.Label(self.frame, text=" Type: " + result[2] ).grid(row=placement, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
            tk.Label(self.frame, text=" Good answers: " + str(result[7])).grid(row=placement, column=2, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
            tk.Label(self.frame, text=" No of questions: " + str(result[6])).grid(row=placement, column=3, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
            tk.Label(self.frame, text=" Grade: " + str(score)).grid(row=placement, column=4, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
            placement += 1

    '''edit question interface and functions'''
    def pickQuestionInterface(self):
        questions = self.__questionHandler.getAllQuestions()
        self.__choosenQuestion = tk.StringVar()
        counter=1
        self.clearInterface()

        self.frame.grid(row=5, column=0, columnspan=9, sticky="nsew", padx=10, pady=10)
        self.frame.columnconfigure(2, weight=1)
        for question in questions:
            tk.Radiobutton(self.frame, text=counter, variable=self.__choosenQuestion,
                           value=question[0], indicator=0).grid(row=3+counter, column=0)
            tk.Label(self.frame, text=question[1]).grid(row=3+counter, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
            counter += 1
        self.__buttonEditQuestion = tk.Button(
            self.frame,
            text="Make Quiz",
            width=BUTTONWIDTH,
            height=BUTTONHEIGHT,
            bg='aquamarine',
            command=lambda: self.buildEditQuestionInterface()
        )
        self.__buttonEditQuestion.grid(row=50, column=8, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)

    def buildEditQuestionInterface(self):
        # Responsiblity:
        # Build an interface so the teacher can eidit a question to the database.
        if self.__teacherID is None:
            return
        self.__editQuestionid = self.__choosenQuestion.get()
        print("retrieving question with id ", self.__editQuestionid, " for editing")
        self.clearInterface()
        question = self.__questionHandler.getQuestion(self.__editQuestionid)
        print("retrieved question: ", question)
        self.frame.grid(row=5, column=0, columnspan=9, sticky="nsew", padx=10, pady=10)
        self.frame.columnconfigure(2, weight=1)

        for col in range(2, 8):
            self.frame.columnconfigure(col, weight=1)

        # MDL found a nice quick implementation of a radiobutton at https://www.geeksforgeeks.org/python/radiobutton-in-tkinter-python/
        # Making the radio checkboxes
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

        # Making the textboxes
        print("Building add question interface textboxes")
        self.__questionLabel = tk.Label(self.frame, text="Question:")
        self.__questionLabel.grid(row=1, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
        self.__questionEntry = tk.Entry(self.frame)
        self.__questionEntry.insert(0, question[1])
        self.__questionEntry.grid(row=1, column=2, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY, columnspan=7, sticky="we")
        self.__answerALabel = tk.Label(self.frame, text="Answer A:")
        self.__answerALabel.grid(row=2, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
        self.__answerAEntry = tk.Entry(self.frame)
        self.__answerAEntry.insert(0, question[6])
        self.__answerAEntry.grid(row=2, column=2, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY, columnspan=7, sticky="we")
        self.__answerBLabel = tk.Label(self.frame, text="Answer B:")
        self.__answerBLabel.grid(row=3, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
        self.__answerBEntry = tk.Entry(self.frame)
        self.__answerBEntry.insert(0, question[7])
        self.__answerBEntry.grid(row=3, column=2, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY, columnspan=7, sticky="we")
        self.__answerCLabel = tk.Label(self.frame, text="Answer C:")
        self.__answerCLabel.grid(row=4, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
        self.__answerCEntry = tk.Entry(self.frame)
        self.__answerCEntry.insert(0, question[8])
        self.__answerCEntry.grid(row=4, column=2, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY, columnspan=7, sticky="we")
        self.__answerDLabel = tk.Label(self.frame, text="Answer D:")
        self.__answerDLabel.grid(row=5, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
        self.__answerDEntry = tk.Entry(self.frame)
        self.__answerDEntry.insert(0, question[9])
        self.__answerDEntry.grid(row=5, column=2, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY, columnspan=7, sticky="we")
        self.__answerELabel = tk.Label(self.frame, text="Answer E:")
        self.__answerELabel.grid(row=6, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
        self.__answerEEntry = tk.Entry(self.frame)
        self.__answerEEntry.insert(0, question[10])
        self.__answerEEntry.grid(row=6, column=2, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY, columnspan=7, sticky="we")
        self.__answerFLabel = tk.Label(self.frame, text="Answer F:")
        self.__answerFLabel.grid(row=7, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
        self.__answerFEntry = tk.Entry(self.frame)
        self.__answerFEntry.insert(0, question[11])
        self.__answerFEntry.grid(row=7, column=2, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY, columnspan=7, sticky="we")
        self.__explanationLabel = tk.Label(self.frame, text="Explanation:")
        self.__explanationLabel.grid(row=8, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
        self.__explanationEntry = tk.Entry(self.frame)
        self.__explanationEntry.insert(0, question[2])
        self.__explanationEntry.grid(row=8, column=2, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY, columnspan=7, sticky="we")
        self.__buttonSaveQuestion = tk.Button(self.frame,
            text="Save Question",
            width=BUTTONWIDTH,
            height=BUTTONHEIGHT,
            bg='aquamarine',
            command=lambda: self.saveQuestion(type='update')
        )
        self.__buttonSaveQuestion.grid(row=50, column=8, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)

    def buildChooseQuizInterface(self, type='add'):
        print("Building choose quiz interface")
        quizes = self.__quizHandler.getAllQuizes()
        placement = 5
        self.clearInterface()
        self.__quizChoosenToAddQuestion = tk.StringVar()
        for quiz in quizes:
            print("Displaying a quiz:")
            self.button = (tk.Radiobutton(self.frame, text=quiz[0], variable=self.__quizChoosenToAddQuestion,
                           value=quiz[0], indicator=0))
            self.button.grid(row=placement, column=1)
            self.label = tk.Label(self.frame, text=quiz[1])
            self.label.grid(row=placement, column=2, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
            placement += 1
        if type == 'add' or type == 'update' or type == 'remove':
            self.__buttonMakeQuiz = tk.Button(
                self.frame,
                text="Choose this Quiz",
                width=BUTTONWIDTH,
                height=BUTTONHEIGHT,
                bg='khaki',
                command=lambda: self.buildChooseQuestionInterface(quizid=self.__quizChoosenToAddQuestion.get(), type=type)
            )
            self.__buttonMakeQuiz.grid(row=placement, column=8, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
        elif type == 'delete':
            self.__buttonDeleteQuiz = tk.Button(
                self.frame,
                text="Choose this Quiz",
                width=BUTTONWIDTH,
                height=BUTTONHEIGHT,
                bg='khaki',
                command=lambda: self.buildConfirmationInterface(quizid=self.__quizChoosenToAddQuestion.get())
            )
            self.__buttonDeleteQuiz.grid(row=placement, column=8, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)


    def buildChooseQuestionInterface(self, quizid = None, type='add'):
        print ("Building Choose question interface")
        if type == 'add' or type == 'delete' or type == 'update':
            questions = self.__questionHandler.getAllQuestions()
            quizid = quizid
        if type == 'remove':
            questions = self.__questionHandler.getQuestionforQuiz(quizid)
            quizid = quizid
        placement = 5
        self.clearInterface()
        self.__questionChoosenToAddToQuiz = tk.StringVar()
        for question in questions:
            #print("Displaying a quiz:")
            self.button = (tk.Radiobutton(self.frame, text=question[0], variable=self.__questionChoosenToAddToQuiz,
                           value=question[0], indicator=0))
            self.button.grid(row=placement, column=1)
            self.label = tk.Label(self.frame, text=question[1])
            self.label.grid(row=placement, column=2, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
            placement += 1
        if type == 'add':
            self.__buttonAddQuizQuestion = tk.Button(
                self.frame,
                text="Store Question in Quiz",
                width=BUTTONWIDTH,
                height=BUTTONHEIGHT,
                bg='khaki',
                command=lambda: self.__questionHandler.addQuestionToQuiz(quizid=quizid,
                                                                         questionid=self.__questionChoosenToAddToQuiz.get())
            )
            self.__buttonAddQuizQuestion.grid(row=placement, column=8, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
        elif type == 'remove':
            self.__buttonRemoveQuizQuestion = tk.Button(
                self.frame,
                text="Remove Question from Quiz",
                width=BUTTONWIDTH,
                height=BUTTONHEIGHT,
                bg='khaki',
                command=lambda: self.__questionHandler.removeQuestionFromQuiz(quizid=quizid,
                                                                         questionid=self.__questionChoosenToAddToQuiz.get())
            )
            self.__buttonRemoveQuizQuestion.grid(row=placement, column=7, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
        elif type == 'delete':
            self.__buttonDeleteQuestion = tk.Button(
                self.frame,
                text="Delete Question",
                width=BUTTONWIDTH,
                height=BUTTONHEIGHT,
                bg='khaki',
                command=lambda: self.buildConfirmationInterface(questionid=self.__questionChoosenToAddToQuiz.get())
            )
            self.__buttonDeleteQuestion.grid(row=placement, column=8, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)


    def buildConfirmationInterface(self, quizid = None, questionid = None):
        if quizid:
            self.__quizname = self.__quizHandler.getQuiz(quizid)[1]
            self.clearInterface()
            self.label = tk.Label(self.frame, text="Are you sure you want to delete this quiz?").grid(row=1, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
            self.label = tk.Label(self.frame, text= self.__quizname).grid(row=2, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
            self.__buttonCancel = tk.Button(
                self.frame,
                text="Cancel",
                width=BUTTONWIDTH,
                height=BUTTONHEIGHT,
                bg='khaki',
                command=lambda: self.clearInterface()
            )
            self.__buttonCancel.grid(row=4, column=8, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
            self.__buttonRemove = tk.Button(
                self.frame,
                text="Remove Quiz",
                width=BUTTONWIDTH,
                height=BUTTONHEIGHT,
                bg='khaki',
                command=lambda: self.__quizHandler.removeQuiz(quizid)
            )
            self.__buttonRemove.grid(row=4, column=8, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
        elif questionid:
            self.__questionname = self.__questionHandler.getQuestion(questionid)[1]
            self.clearInterface()
            self.label = tk.Label(self.frame, text="Are you sure you want to delete this quiz?").grid(row=1, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
            self.label = tk.Label(self.frame, text= self.__questionname).grid(row=2, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
            self.__buttonCancel = tk.Button(
                self.frame,
                text="Cancel",
                width=BUTTONWIDTH,
                height=BUTTONHEIGHT,
                bg='khaki',
                command=lambda: self.clearInterface()
            )
            self.__buttonCancel.grid(row=4, column=7, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
            self.__buttonRemove = tk.Button(
                self.frame,
                text="Remove Question",
                width=BUTTONWIDTH,
                height=BUTTONHEIGHT,
                bg='khaki',
                command=lambda: self.__questionHandler.removeQuestion(questionid)
            )
            self.__buttonRemove.grid(row=4, column=8, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)