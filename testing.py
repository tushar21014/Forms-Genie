import multiprocessing
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
def hello1():
    print("1")
def hello2():
    print("2")
def hello3():
    print("3")

p1 = multiprocessing.Process(target=hello1)
p3 = multiprocessing.Process(target=hello2)
p2 = multiprocessing.Process(target=hello3)

def when_clicked():
    p1.start()
    p3.start()
    p2.start()
       


if __name__ == '__main__':
    window = Tk()
    window.geometry('1366x789')
    submit_button = Button(window, text="Submit", command=when_clicked)
    submit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    window.mainloop()


# success_label = Label(root, text="")

