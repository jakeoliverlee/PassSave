from tkinter import *

class PassSaveGUI:
    def __init__(self, master):
        master.title("PassSave")
        master.config(padx=50, pady=50)
        self.canvas = Canvas(height=200, width=200)
        self.logo = PhotoImage(file="logo.png")
        self.canvas.create_image(100, 100, image=self.logo)
        self.canvas.grid(row=0, column=1)

        # Labels
        self.website_label = Label(text="Website:")
        self.website_label.grid(row=1, column=0)
        self.email_label = Label(text="Email:")
        self.email_label.grid(row=2, column=0)
        self.password_label = Label(text="Password:")
        self.password_label.grid(row=3, column=0)

        # Entries
        self.website_entry = Entry(width=39)
        self.website_entry.grid(row=1, column=1, columnspan=3, sticky="NSEW")
        self.email_entry = Entry(width=39)
        self.email_entry.grid(row=2, column=1, columnspan=3, sticky="NSEW")
        self.password_entry = Entry(width=24)
        self.password_entry.grid(row=3, column=1, columnspan=2, sticky="NSEW")

        # Buttons
        self.generate_pass_button = Button(text="Generate")
        self.generate_pass_button.grid(row=3, column=3, sticky="NSEW")
        self.add_button = Button(text="Add")
        self.add_button.grid(row=4, column=1, sticky="NSEW")
        self.clear_button = Button(text="Clear")
        self.clear_button.grid(row=4, column=2, sticky="NSEW")
        self.search_button = Button(text="Search")
        self.search_button.grid(row=4, column=3, sticky="NSEW")


def main():
    main_window = Tk()
    PassSave = PassSaveGUI(main_window)
    main_window.mainloop()