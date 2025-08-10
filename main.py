from tkinter import *                                                      #importing libraries
import requests

def get_quote():                                                           #function to get request from kanye api and evertime
    response = requests.get("https://api.kanye.rest")                      #we call it generate a quote
    response.raise_for_status()
    quote = response.json()
    canvas.itemconfig(quote_text,text = quote["quote"])

#Making of UI in Tkinter
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="./background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="./kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

get_quote()

window.mainloop()
