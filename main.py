from TeacherUI import TeacherUI
import tkinter as tk

def main():
    # Responsibility: Starts the Logo Grader application.
    root = tk.Tk()
    window = TeacherUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()