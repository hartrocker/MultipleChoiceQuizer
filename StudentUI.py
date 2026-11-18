import tkinter as tk

#from DB_handler import DB_handler
from QuestionHander import QuestionHandler
from SubjectHandler import SubjectHandler
from QuizHandler import QuizHandler
from ResultHandler import ResultHandler

BUTTONPADDINGX = 3
BUTTONPADDINGY = 3
BUTTONWIDTH = 25
BUTTONHEIGHT = 2


class StudentUI():
    def __init__(self, root):
        #self.canvasBuilder()
        self.__questionHandler = QuestionHandler()
        self.__subjectHandler = SubjectHandler()
        self.__quizHandler = QuizHandler()
        self.__resultHandler = ResultHandler()
        self.__authorized = False
        self.__counter = None
        self.window = root
        self.window.title("Quiz module")
        self.window.geometry("1200x800")
        self.screen = None
        self.screen = tk.Canvas(self.window, width=1200, height=800)
        self.screen.config()
        self.buildMainInterface()
        self.workFrame = tk.Frame(self.window)
        self.workFrame.grid(row=3, column=1, rowspan=1, columnspan=8)

    def clearInterface(self):
        # Responsiblity:
        # Remove the add question interface.
        for widget in self.workFrame.winfo_children():
            widget.destroy()
        #.grid_forget()

    def buildMainInterface(self):
        self.menuFrame = tk.Frame(self.window)
        self.menuFrame.grid(row=1, column=0, columnspan=9, sticky="nsew", padx=10, pady=10)

        self.__buttonTakeQuiz = tk.Button(
            self.menuFrame,
            text="Take a quiz",
            width=BUTTONWIDTH,
            height=BUTTONHEIGHT,
            bg='khaki',
            command=lambda: self.makeChooseQuizInterface()
        )
        self.__buttonTakeQuiz.grid(row=2, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)

        self.__buttonPractiseSubject = tk.Button(
            self.menuFrame,
            text="Practice a subject",
            width=BUTTONWIDTH,
            height=BUTTONHEIGHT,
            bg='khaki',
            command=lambda: self.makeChooseSubjectInterface()
        )
        self.__buttonPractiseSubject.grid(row=2, column=2, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)

        self.__buttonSeeResults = tk.Button(
            self.menuFrame,
            text="See results",
            width=BUTTONWIDTH,
            height=BUTTONHEIGHT,
            bg='khaki',
            command=lambda: self.seeResults()
        )
        self.__buttonSeeResults.grid(row=2, column=3, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)

    def makeChooseQuizInterface(self):
        print("Building add question interface")
        quizes = self.__quizHandler.getAllQuizes()
        placement = 5
        self.__quizChoosen = tk.StringVar()
        for quiz in quizes:
            print("Displaying a quiz:")
            self.button = (tk.Radiobutton(self.workFrame, text=quiz[0], variable=self.__quizChoosen,
                           value=quiz[0], indicator=0))
            self.button.grid(row=placement, column=1)
            self.label = tk.Label(self.workFrame, text=quiz[1])
            self.label.grid(row=placement, column=2, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
            placement += 1
        self.__buttonMakeQuiz = tk.Button(
            self.workFrame,
            text="Make Quiz",
            width=BUTTONWIDTH,
            height=BUTTONHEIGHT,
            bg='khaki',
            command=lambda: self.makeQuestionInterface(type="quiz", quizid=self.__quizChoosen.get())
        )
        self.__buttonMakeQuiz.grid(row=placement, column=8, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)

    def makeChooseSubjectInterface(self):
        print("Building add question interface")
        subjects = self.__subjectHandler.getAllSubjects()
        self.clearInterface()
        # Building the subject checkboxes
        self.__subjects = self.__subjectHandler.getAllSubjects()
        print(self.__subjects)
        tk.Label(self.workFrame, text="Onderwerpen").grid(row=9, column=1)
        placement = 10
        self.__subjectlist = []
        for row in self.__subjects:
            subject = tk.BooleanVar()
            tk.Checkbutton(self.workFrame, variable = subject, text=str(row[1])).grid(row=placement, column=1,  sticky="w")
            self.__subjectlist.append(subject)
            placement += 1
        print (self.__subjectlist)

        self.__buttonChooseSubject = tk.Button(self.workFrame,
            text="Choose Subject",
            width=BUTTONWIDTH,
            height=BUTTONHEIGHT,
            bg='aquamarine',
            command=lambda: self.processSubject()
        )
        self.__buttonChooseSubject.grid(row=50, column=8, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)


    def processSubject(self):
        print("choosing subject. choosen subjects are: ")
        self.__subjectList = []
        for option, var in zip(self.__subjects, self.__subjectlist):
            if var.get():
                self.__subjectList.append(option)
                print(option)
        self.__subjectLengthList = []
        self.clearInterface()
        placement=7
        self.__entryList = []
        for subject in self.__subjectList:
            #questions = self.__questionHandler.getQuestionforSubject(subject)
            max_questions = self.__subjectHandler.getHowManyQuestions(subject[0])
            self.__subjectLengthList.append(max_questions)
            label = tk.Label(self.workFrame, text="Please set the amount of questions you want to practice for " + str(subject[1]) + " (max " + str(max_questions) + ")")
            label.grid(row=placement, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
            self.entry = tk.Entry(self.workFrame)
            self.entry.grid(row=placement, column=2, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
            self.__entryList.append(self.entry)
            placement += 1
        #self.clearInterface()
        print(self.__subjectList)
        #self.makeQuestionInterface(type="subject", subjectids=subjectList)
        self.__buttonChooseSubject = tk.Button(self.workFrame,
            text="Choose Subject",
            width=BUTTONWIDTH,
            height=BUTTONHEIGHT,
            bg='aquamarine',
            command=lambda: self.makeQuestionInterface(type='subject')
        )
        self.__buttonChooseSubject.grid(row=50, column=8, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)

    def makeQuestionInterface(self, type, quizid= None):
        # Responsiblity:
        # Setup the starting critera for the quiz, and setting variables for the quiz.

        #Setting starter variables
        self.__counter = 0
        self.__quiztype = type
        self.__goodAnswers = 0
        self.__questionList = []
        if self.__quiztype == 'quiz':
            self.__quizid = quizid
            # Start generating a teacher made quiz
            print("the selected quiz id is ", self.__quizid)
            self.__questionList = self.__questionHandler.getQuestionforQuiz(quizid)
            print("we have received a list of questions:", self.__questionList)

        elif self.__quiztype == 'subject':
            print("you have received a list of subjects:", self.__subjectList)
            print("you have received a list of subject lengths:", self.__subjectLengthList)
            # Start generating a subject quiz
            lengthList = []
            print ("we are going to pull from the entry list:", self.__entryList)
            for var in self.__entryList:
                length = var.get()
                lengthList.append(length)
            counter = 0
            for subject in self.__subjectList:
                print(" we gaan een subject quiz maken voor ", subject)
                max = lengthList[counter]
                print("max is now ", max ," questions, we will get this many questions for subject ", subject[1])
                questions = self.__questionHandler.getQuestionforSubject(subject[0], random=True, maximum=max)
                self.__questionList.extend(questions)
                counter += 1
            print("starting a subject quiz! we now have ", len(self.__questionList))
        print("the selected quiz type is ", self.__quiztype)
        self.clearInterface()
        #Make exception for an empty quiz
        if self.__counter == 0 and len(self.__questionList) == 0:
            tk.Label(self.workFrame, text="No questions available").grid(row=4, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
            return
        else:
            question = self.__questionList[self.__counter]
            self.displayQuestion(question)

    def loadNextQuestion(self):
        if self.__givenAnswer.get() != "":
            self.rightAnswer = self.__questionList[self.__counter][7]
            if self.__givenAnswer.get().lower() == self.rightAnswer.lower():
                self.__goodAnswers += 1
                print("you currently have ", self.__goodAnswers, " good answers out of ", len(self.__questionList))
            print("the type is anser is ", type(self.__givenAnswer.get()), "the value is ", self.__givenAnswer.get())
            print("an answer was given, loading next question")
            self.__counter += 1
            if self.__counter < len(self.__questionList):
                question = self.__questionList[self.__counter]
                self.clearInterface()
                self.displayQuestion(question)
            else:
                print("End of quiz reached, displaying results")
                self.clearInterface()
                self.displayResultsAfterQuiz()
        else:
            print("no answer was given, not moving on yet")
            tk.Label(self.workFrame, text="Please answer the question before moving on", fg='red').grid(row=18, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)


    def displayQuestion(self, question):
        # Responsiblity:
        # Display the question and the answers.
        # Data from SQL in order: questionid, question, explanation, rightAnswer, dateAdded, creatorID, A, B, C, D, E, F
        question = question
        print(question)
        self.__trackerlabel = tk.Label(self.workFrame, text="Question: " + str(self.__counter+1) + "/" + str(len(self.__questionList)))
        self.__trackerlabel.grid(row=1, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
        self.__questionLabel = tk.Label(self.workFrame, text=question[1])
        self.__questionLabel.grid(row=3, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
        answers = []
        for i in range(6, 12):
            if question[i] != None:
                answers.append(question[i])
        print(answers)
        values = {"6": "A",
                  "7": "B",
                  "8": "C",
                  "9": "D",
                  "10": "E",
                  "11": "F"}
        placement=5
        self.__givenAnswer = tk.StringVar()
        for (sequence, DBindex) in values.items():
            sequence = int(sequence)
            print("sequence is ", sequence, " and DBindex is ", DBindex)
            tk.Radiobutton(self.workFrame, text=DBindex, variable=self.__givenAnswer,
                           value=DBindex, indicator=0).grid(row=placement, column=0)
            tk.Label(self.workFrame, text=answers[sequence-6]).grid(row=placement, column=1)
            placement += 1
        self.__buttonNextQuestion = tk.Button(
            self.workFrame,
            text="Next Question",
            width=BUTTONWIDTH,
            height=BUTTONHEIGHT,
            bg='khaki',
            command=lambda: self.loadNextQuestion())
        self.__buttonNextQuestion.grid(row=placement, column=8, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)

    def displayResultsAfterQuiz(self):
        self.clearInterface()
        print("displaying results")
        tk.Label(self.workFrame, text="You got " + str(self.__goodAnswers) + " out of " + str(len(self.__questionList))).grid(row=7, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
        tk.Label(self.workFrame, text="Name: ").grid(row=8, column=0, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
        self.__entryName = tk.Entry(self.workFrame)
        self.__entryName.grid(row=8, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY, columnspan=7, sticky="we")
        tk.Label(self.workFrame, text="Class: ").grid(row=9, column=0, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
        self.__className = tk.Entry(self.workFrame)
        self.__className.grid(row=9, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY, columnspan=7, sticky="we")
        self.__buttonSaveResults = tk.Button(
            self.workFrame,
            text="Save results",
            width=BUTTONWIDTH,
            height=BUTTONHEIGHT,
            bg='khaki',
            command = lambda: self.saveResults()
        )
        self.__buttonSaveResults.grid(row=4, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY, columnspan=7, sticky="we")

    def saveResults(self):
        name = self.__entryName.get()
        class_name = self.__className.get()
        if self.__quiztype == "quiz":
            #    def addResult(self, studentname, studentclass, quiztype, goodAnswers, noOfQuestions = None, quizid = None, subjectid = None):
            self.__resultHandler.addResult(studentname = name, studentclass = class_name, quiztype=self.__quiztype, goodAnswers=self.__goodAnswers, noOfQuestions=self.__counter, quizid=self.__quizid)
        elif self.__quiztype =="subject":
            # T O D O: process subject quiz
            pass
        self.clearInterface()
        tk.Label(self.workFrame, text="Results saved").grid(row=1, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)

    def buildSeeResultsInterface(self):
        results = self.__resultHandler.getAllResults()
        print(results)
        self.clearInterface()
        tk.Label(self.workFrame, text="Results").grid(row=1, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
        placement = 2
        for result in results:
            score = float(float(result[7])/float(result[6])*9+1)
            tk.Label(self.workFrame, text="Quiz: " + result[1] ).grid(row=placement, column=0, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
            tk.Label(self.workFrame, text=" Type: " + result[2] ).grid(row=placement, column=1, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
            tk.Label(self.workFrame, text=" Good answers: " + str(result[7])).grid(row=placement, column=2, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
            tk.Label(self.workFrame, text=" No of questions: " + str(result[6])).grid(row=placement, column=3, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
            tk.Label(self.workFrame, text=" Grade: " + str(score)).grid(row=placement, column=4, padx=BUTTONPADDINGX, pady=BUTTONPADDINGY)
            placement += 1