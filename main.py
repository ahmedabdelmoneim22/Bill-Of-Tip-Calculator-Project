import tkinter as tk # GUI library;
def rgb_to_hex(rgb):
    """Converts an RGB tuple to a hexadecimal color code."""
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])
def Calculate_The_Tip():
    # Tip-Calculator-Project;
    # input The Total Bill;
    bill = float(billEntry.get())
    if bill > 0 and bill < 1000000:
        # input The Tip you want to give;
        tip = float(tipEntry.get())
        if tip > 0 and tip < 21:
            # Number of the People bay the bill;
            people = float(peopleEntry.get())
            if people > 0 and people < 100:
                tip_as_percent = tip / 100
                total_tip_amount = bill * tip_as_percent
                total_bill = bill + total_tip_amount
                bill_per_person = total_bill / people
                final_amount = round(bill_per_person, 2)
                # Final Amount for Each Person;
                final_amount = "{:.2f}".format(bill_per_person)
                resultLabel.configure(text=f"{final_amount}$(Per Person).",fg="green")
            else:
                resultLabel.configure(text="Incorrect Input.")
        else:
            resultLabel.configure(text="Incorrect Input.")
    else:
        resultLabel.configure(text="Incorrect Input.")
                # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
rgb_color = (237, 0, 29)
hex_color = rgb_to_hex(rgb_color)#Color of the Label;
blue_color = (0, 56, 184)
hex_blue = rgb_to_hex(blue_color)
mainWindow = tk.Tk()
mainWindow.config(background=hex_blue)
mainWindow.title("TIP CALCULATOR")
mainWindow.geometry("420x200")
welcomeLabel = tk.Label(mainWindow,text="WELCOME TO TIP CALCULATOR",fg=hex_color,
                        font=("Helvetica", 15, "bold"),background=hex_blue)
welcomeLabel.grid(row=0,column=0,columnspan=2)
billLabel = tk.Label(mainWindow,text="The Bill Value",fg=hex_color,font=("Helvetica",10,"bold"),background=hex_blue)
billLabel.grid(row=1,column=0)
billEntry=tk.Entry()
billEntry.grid(row=1,column=1)
tipLabel = tk.Label(mainWindow,text="Tip Percentage",fg=hex_color,font=("Helvetica",10,"bold"),background=hex_blue)
tipLabel.grid(row=2,column=0)
tipEntry=tk.Entry()
tipEntry.grid(row=2,column=1)
peopleLabel = tk.Label(mainWindow,text="No. of Persons",fg=hex_color,font=("Helvetica",10,"bold"),background=hex_blue)
peopleLabel.grid(row=3,column=0)
peopleEntry=tk.Entry()
peopleEntry.grid(row=3,column=1)
totalLabel = tk.Label(mainWindow,text="THE TOTAL BILL",fg=hex_color,font=("Helvetica", 15, "bold"),background=hex_blue)
totalLabel.grid(row=4,column=0)
resultLabel = tk.Label(mainWindow,text="-----------",fg=hex_color,font=("Helvetica", 15, "bold"),background=hex_blue)
resultLabel.grid(row=4,column=1)
resultButton = tk.Button(text="Calculate",bg=hex_color,fg="white",
                         font=("Helvetica",12,"bold"),width=12,command=Calculate_The_Tip)
resultButton.grid(row=5,column=1)
mainWindow.resizable(False, False)
mainWindow.mainloop()
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# print("Welcome to the tip calculator!")
#bill = float(input("What was the total bill? $"))
# tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
#people = int(input("How many people to split the bill?"))
##print(f"Each person should pay: ${final_amount}")
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
