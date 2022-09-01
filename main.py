
import random
import tkinter
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generatePass():
    let = [random.choice(letters) for x in range(random.randint(8,10))]
    num = [random.choice(numbers) for x in range(random.randint(2,3))]
    sym = [random.choice(symbols) for x in range(random.randint(2,3))]
    password = let+num+sym
    random.shuffle(password)
    newPass = "".join(password)
    passEntry.insert(0, newPass)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def savePass():
    web = webEntry.get()
    user = userEntry.get()
    password = passEntry.get()
    data = f"{web} | {user} | {password}\n"

    messageBox = messagebox.askokcancel(title="Save password", message=f"Web: {web}\nUser: {user}\nPassword: {password}\nDo you want to save this password?")
    print(messageBox)
    if messageBox and len(web) > 0 and len(password) > 0:
        with open("data.txt","a") as file:
            file.write(data)
            webEntry.delete(0, tkinter.END)
            passEntry.delete(0, tkinter.END)
            messagebox.showinfo(title="Saved", message="Password saved.")    
    else:
        messagebox.showerror(title="Error", message="Canceled")

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo = tkinter.PhotoImage(file="logo.png")

canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)


webLabel = tkinter.Label(text="Website:")
webLabel.grid(column=0, row=1)
webEntry = tkinter.Entry(width=35)
webEntry.focus()
webEntry.grid(column=1, row=1, columnspan=2)

userLabel = tkinter.Label(text="Email/Username:")
userLabel.grid(column=0, row=2)

userEntry = tkinter.Entry(width=35)
userEntry.grid(column=1, row=2, columnspan=2)
userEntry.insert(0, "mongol@gmail.com")


passLabel = tkinter.Label(text="Password:")
passLabel.grid(column=0, row=3)
passEntry = tkinter.Entry(width=25)
passEntry.grid(column=1, row=3)
passButton = tkinter.Button(text="Generate", command=generatePass)
passButton.grid(column=2, row=3)

addButton = tkinter.Button(width=36, text="Add", command=savePass)
addButton.grid(column=1, row=4, columnspan=2)


window.mainloop()