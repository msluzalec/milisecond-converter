from tkinter import *


class ConvertMilliseconds:

    # result = 0
    ans = 0

    def __init__(self, master):
        self.result = 0

        self.master = master
        master.title("Converting milliseconds")

        self.label = Label(master, text="Enter time in milliseconds:")
        self.label.pack()

        self.entry = Entry(master)
        self.entry.pack()

        self.convert_button = Button(master, text="Convert", command=self.convert_milliseconds)
        self.convert_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

        self.outcome = Label(master, text="The result is: {}".format(self.result))
        # self.var.set(self.result)
        self.outcome.pack()

    def convert_milliseconds(self):
        self.millis = int(self.entry.get())
        self.seconds = int((self.millis / 1000) % 60)

        self.minutes = int((self.millis / (1000 * 60)))

        if self.seconds < 10:
            self.result = "{}:0{}".format(self.minutes, self.seconds)
            self.outcome.configure(text="The result is: {}".format(self.result))
        else:
            self.result = "{}:{}".format(self.minutes, self.seconds)
            self.outcome.configure(text="The result is: {}".format(self.result))





root = Tk()
my_gui = ConvertMilliseconds(root)
root.mainloop()
