from itertools import tee
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QiuzInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(height=1100, width=400, padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(height=250, width=300, bg='white', highlightthickness=0)
        self.question = self.canvas.create_text(
            150,
            125, 
            width= 250,
            text='abra', 
            font=('Arial', 15, 'italic'), 
            fill=THEME_COLOR
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score = Label(text=f'Score: 0', font=('Arial', 13, 'normal'), bg=THEME_COLOR, fg='white')
        self.score.grid(column=1, row=0)

        true_image = PhotoImage(file='./Quizzler_app/images/true.png')
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)

        false_image = PhotoImage(file='./Quizzler_app/images/false.png')
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()   

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text='You\'ve reached the end of the quiz')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def false_pressed(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)
    
    def true_pressed(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)
    
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)


