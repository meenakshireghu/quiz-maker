import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root=root
        self.root.title("Quiz")
        self.root.geometry("360x360")

        # Questions and answers 
        self.questions=[
            {"question": "What is Tkinter?", "options": ["a) A database", "b) A GUI library", "c) A programming language", "d) An IDE"], "answer": "b"},
            {"question": "Which Tkinter method is used to start the application?", "options": ["a) mainloop()", "b) start()", "c) run()", "d) begin()"], "answer": "a"},
            {"question": "Which widget is used to create a clickable button?", "options": ["a) Label", "b) Entry", "c) Button", "d) Frame"], "answer": "c"},
            {"question": "What does the 'pack()' method do?", "options": ["a) Organizes widgets in a block", "b) Opens a new window", "c) Deletes a widget", "d) Closes the application"], "answer": "a"},
            {"question": "How do you set the title of a Tkinter window?", "options": ["a) setTitle()", "b) title()", "c) set_caption()", "d) setWindowTitle()"], "answer": "b"}
        ]

        self.current_question = 0
        self.score = 0
        self.user_answer = tk.StringVar()#user's selected answer
        self.create_welcome_screen()

    def create_welcome_screen(self):
        self.clear_window()
        self.welcome_label=tk.Label(self.root, text="Welcome to the Tkinter Quiz!", font=("Arial", 16))
        self.welcome_label.pack(pady=20)

        self.start_button=tk.Button(self.root, text="Start", font=("Arial", 14), command=self.start_quiz)
        self.start_button.pack(pady=20)

    def start_quiz(self):
        self.clear_window()
        self.current_question=0
        self.score=0
        self.display_question()

    def display_question(self):
        self.clear_window()

        question_data=self.questions[self.current_question]
        question_num=f"Question {self.current_question + 1}/{len(self.questions)}"
        self.user_answer.set("")#to ensure that no answer is preselected

        self.question_num_label=tk.Label(self.root, text=question_num, font=("Arial", 14))
        self.question_num_label.pack(pady=10)

        self.question_label = tk.Label(self.root, text=question_data["question"], font=("Arial", 13))
        self.question_label.pack(pady=20)

        self.option_a = tk.Radiobutton(self.root, text=question_data["options"][0], variable=self.user_answer, value="a", font=("Arial", 13))
        self.option_a.pack(anchor="w")
        self.option_b = tk.Radiobutton(self.root, text=question_data["options"][1], variable=self.user_answer, value="b", font=("Arial", 13))
        self.option_b.pack(anchor="w")
        self.option_c = tk.Radiobutton(self.root, text=question_data["options"][2], variable=self.user_answer, value="c", font=("Arial", 13))
        self.option_c.pack(anchor="w")
        self.option_d = tk.Radiobutton(self.root, text=question_data["options"][3], variable=self.user_answer, value="d", font=("Arial", 13))
        self.option_d.pack(anchor="w")

        self.next_button = tk.Button(self.root, text="Next", command=self.next_question)
        self.next_button.pack(pady=20)

    def next_question(self):
        # Check if the answer is correct
        if self.user_answer.get() == self.questions[self.current_question]["answer"]:
            self.score += 1

        self.current_question += 1

        if self.current_question < len(self.questions):
            self.display_question()
        else:
            self.display_score()

    def display_score(self):
        self.clear_window()
        result_text = f"Your final score is {self.score} out of {len(self.questions)}"
        self.result_label = tk.Label(self.root, text=result_text, font=("Arial", 14))
        self.result_label.pack(pady=20)

        self.restart_button = tk.Button(self.root, text="Restart Quiz", font=("Arial", 14), command=self.start_quiz)
        self.restart_button.pack(pady=20)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


root = tk.Tk()
app = QuizApp(root)
root.mainloop()