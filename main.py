from TeacherUI import TeacherUI
from StudentUI import StudentUI
import tkinter as tk

def main():
    # Responsibility: Starts the Logo Grader application.
    root = tk.Tk()
    window = TeacherUI(root)
    #window = StudentUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()