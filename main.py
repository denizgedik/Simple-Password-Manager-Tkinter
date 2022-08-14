from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def password_generator():

    password_input.delete(0, END)

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def saver():
    f = open("data.txt", "a")
    website_name = website_input.get()
    email_name = email_input.get()
    password_name = password_input.get()

    if len(website_name) == 0 or len(email_name) == 0 or len(password_name) == 0:
        messagebox.showerror(title="Missing values", message="You haven't entered all the necessary fields.\n"
                                                             "Try again.")

    else:
        is_ok = messagebox.askokcancel(title=website_name,
                                       message=f"These are the details entered: Website: {website_name}"
                                               f"\nEmail: {email_name}"
                                               f"\nPassword: {password_name} \nIs it ok to save?")

        if is_ok:
            f.write(f"{website_name} / {email_name} / {password_name}\n")
            f.close()
            website_input.delete(0, END)
            email_input.delete(0, END)
            email_input.insert(END, "@gmail.com")
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("PassPass")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, highlightthickness=0, bg="white")
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0, padx=(32, 0))

website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", bg="white")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row=3)

website_input = Entry(width=40, highlightbackground="white")
website_input.grid(column=1, row=1, columnspan=2, pady=1)
website_input.focus()
email_input = Entry(width=40, highlightbackground="white")
email_input.grid(column=1, row=2, columnspan=2, pady=1)
email_input.insert(END, "@gmail.com")
password_input = Entry(width=25, highlightbackground="white")
password_input.grid(column=1, row=3, pady=1)

generate_button = Button(text="Generate Password", highlightbackground="white", width=10, command=password_generator)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", highlightbackground="white", width=38, command=saver)
add_button.grid(column=1, row=4, pady=5, columnspan=2)

window.mainloop()
