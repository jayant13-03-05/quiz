import tkinter as tk
from tkinter import messagebox

# Data
questions = [
    "1. What is the full form of HTTP?",
    "2. Which of the following is NOT a programming language?",
    "3. Who developed Python?",
    "4. In networking, what does IP stand for?"
]
options = [
    ["Hyper Text Transfer Protocol", "Hyperlinks Text Transfer Protocol", "Hyper Text Transmission Protocol", "Hyperlink Transfer Text Protocol"],
    ["Python", "HTML", "Java", "C++"],
    ["Guido van Rossum", "Dennis Ritchie", "Mark Zuckerberg", "Linus Torvalds"],
    ["Internet Protocol", "Interlink Protocol", "Internal Protocol", "Intranet Protocol"]
]
answers = [0, 1, 0, 0]

# Main window setup
root = tk.Tk()
root.overrideredirect(True)  # Title bar hide karega
root.geometry("500x400")
root.configure(bg="#007bff")

question_index = 0
score = 0
selected_option = tk.IntVar(value=-1)
time_left = 15  # Seconds
quiz_over = False  # New flag to check if quiz is over

def load_question():
    global time_left
    question_label.config(text=questions[question_index])
    selected_option.set(-1)
    for i, btn in enumerate(option_buttons):
        btn.config(text=options[question_index][i], bg="white", fg="black", state="normal", anchor="w", justify="left")
    tracker_label.config(text=f"{question_index+1} of {len(questions)} Questions")
    next_btn.pack_forget()  # Hide next button until answer selected or time up
    time_left = 15
    update_timer()

def update_timer():
    global time_left, quiz_over
    if quiz_over:
        return  # Stop timer if quiz is over
    if time_left > 0:
        timer_label.config(text=f"Time Left: {time_left} sec")
        time_left -= 1
        root.after(1000, update_timer)
    else:
        messagebox.showinfo("Time's Up!", "Moving to next question...")
        show_next_button()

def check_answer(idx):
    global score
    correct = answers[question_index]
    for i, btn in enumerate(option_buttons):
        if i == correct:
            btn.config(bg="#d4edda", fg="#155724", text="✔ " + options[question_index][i])
        if i == idx and idx != correct:
            btn.config(bg="#f8d7da", fg="#721c24", text="❌ " + options[question_index][i])
        btn.config(state="disabled")
    if idx == correct:
        score += 1
    show_next_button()

def show_next_button():
    next_btn.pack(pady=10)

def next_question():
    global question_index, quiz_over
    question_index += 1
    if question_index < len(questions):
        load_question()
    else:
        quiz_over = True  # Mark quiz as over to stop timer
        messagebox.showinfo("Quiz Over", f"You scored {score} out of {len(questions)}")
        root.destroy()

# Center the root window on the screen
root.update_idletasks()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (500 // 2)
y = (screen_height // 2) - (400 // 2)
root.geometry(f"500x400+{x}+{y}")

# Card Frame for Quiz Layout
card = tk.Frame(root, bg="white", bd=0, relief="solid")
card.place(relx=0.5, rely=0.5, anchor="center", width=400, height=340)

# Custom Close Button (Top Right)
close_btn = tk.Button(root, text="X", bg="red", fg="white", font=("Arial", 10, "bold"),
                    relief="flat", command=root.destroy)
close_btn.place(x=470, y=10, width=20, height=20)

# Header Label
header = tk.Label(card, text="Awesome Quiz Application", bg="white", font=("Helvetica", 14, "bold"))
header.pack(pady=8)

# Timer Label
timer_label = tk.Label(card, text="Time Left: 15 sec", bg="white", fg="#007bff", font=("Arial", 10, "bold"))
timer_label.pack()

# Question Label
question_label = tk.Label(card, text="", wraplength=350, bg="white", font=("Arial", 12, "bold"), justify="center")
question_label.pack(pady=10)

# Options Frame
options_frame = tk.Frame(card, bg="white")
options_frame.pack(fill="x")

option_buttons = []
for i in range(4):
    btn = tk.Button(options_frame, text="", wraplength=300, relief="solid", bd=1, bg="white", fg="black",
                    command=lambda idx=i: check_answer(idx), anchor="w", justify="left")
    btn.pack(fill="x", padx=20, pady=4, anchor="w")
    option_buttons.append(btn)

# Tracker Label
tracker_label = tk.Label(card, text="", bg="white", font=("Arial", 10))
tracker_label.pack(pady=5)

# Next Button (initially hidden)
next_btn = tk.Button(card, text="Next Question", bg="#007bff", fg="white", font=("Arial", 10, "bold"),
                    relief="flat", padx=10, pady=5, command=next_question)

# Load the first question
load_question()

root.mainloop()
