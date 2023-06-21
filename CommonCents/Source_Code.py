from tkinter import *               # importing tkinter library for GUI
from tkinter.font import Font       # importing tkinter.font module for accessing different fonts in GUI
import mysql.connector as ms        # inporting mysql.connector module to connect python with mysql database 
import tkinter.ttk as ttk           # importing tkinter.ttk library to access better widgets

# connecting python with csproject database from mysql
mydb = ms.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password',
    database = 'csproject'
)

# defining the cursor
mycur = mydb.cursor()


root = Tk()                                                 # making a tkinter window
root.title("Login")                                         # giving the window a title
root.iconbitmap("CommonCents1.ico")                         # giving icon to the window

# defining fonts
my_font = Font(
    family = 'Cooper Black',
    size = 35,
    weight = 'bold',
    slant =  'roman',
    underline = True,
    overstrike = False  
)

other_font = Font(
    family="Bookman Old Style",
    size = 20,
    slant='roman',
    underline=False,
    overstrike = False
)

# creating a heading
heading = Label(root, text = "CommonCents: An Expense Manager",  font = my_font)
heading.grid(row=0, column=0, columnspan=2)

# creating input labels
user = Label(root, text = "EMAIL ID", font = other_font)
passwd = Label(root, text = "PASSWORD", font = other_font)

# placing the labels in the window
user.grid(row = 1)
passwd.grid(row =2)

# defining datatype of entry widget
user_value = StringVar()
pass_value = StringVar()

# making entry widgets to get username and password
userentry = Entry(root, textvariable=user_value, font = other_font, width=25)
passentry = Entry(root, textvariable=pass_value, font=other_font, width=25)

# placing entry widgets to the window
userentry.grid(row = 1, column = 1)
passentry.grid(row = 2, column = 1)

# defining a login function to do the login operation in the backend of the program
def login():
    # Getting email id from the database
    mycur.execute("SELECT Email_ID FROM login")
    # Storing the email id in output variable                                                    
    output = mycur.fetchall()

    # creating an empty list
    mail_list = []
    
    # Looping through the list of passwords and appending it to main_list
    for i in range(len(output)):                                                                       
        a = output[i][0]
        mail_list.append(a)
    
    # Getting email id and password from login table in the database
    mycur.execute("SELECT Email_ID, Password FROM login")
    new_output = mycur.fetchall()
    
    # Making a dictionary of email id and password
    a = dict(new_output)
    
    # Getting email id from the entry widget
    mail = userentry.get()
    
    # Defining a function to make success window 
    def login_success():
            succ = Tk()
            
            succ.iconbitmap("CommonCents1.ico")
            succ.title("Success")
            
            label = Label(succ, text = 'Login Successful :)', font = other_font)
            label.pack()
            
            def des():
                succ.destroy()
                root.destroy()
            
            button = Button(succ, text = "OK", font = other_font, command = des)
            button.pack()
            
            succ.mainloop()
    
    # Defining a warning window for incorrect password
    def warning():
        war = Tk()
        
        war.iconbitmap("warning.ico")
        war.title("Warning")
        
        label = Label(war, text = 'Incorrect password\nPlease check your password', font= other_font)
        label.pack()
        def des():
            war.destroy()

        button = Button(war, text = 'OK', font=other_font, command=des)
        button.pack()
        
        war.mainloop()
    
    # Defining a warning window for incorrect email id
    def warning2():
        war = Tk()
        war.iconbitmap("warning.ico")
        war.title("Warning")
        label = Label(war, text = 'Email ID not in database\nPlease Sign Up', font= other_font)
        label.pack()
        def des():
            war.destroy()
        button = Button(war, text = 'OK', font=other_font, command=des)
        button.pack()
        war.mainloop()
    
    # checking if email id and password are matching with each other
    if mail in mail_list:
        pwd = passentry.get()
        if pwd == a[mail]:
            login_success()
        else:
            warning()
    else:
        warning2()

# Creating a button to perform login command
login_button = Button(root, text = "LOGIN", font = other_font, command=login)
login_button.grid(row=5)

# Creating a label for signup warning
signup_text = Label(root, text="Don't have an account?", bg = "red", font = other_font)
signup_text.grid(row=6)

# Defining signup function to do the signup operation in the backend of the program
def signup():
    # Making a new signup window
    win = Tk()
    win.title("Signup")
    win.iconbitmap("CommonCents1.ico")
    
    # Making fonts for the program
    my_font = Font(
        family = 'Cooper Black',
        size = 50,
        weight = 'bold',
        slant =  'roman',
        underline = True,
        overstrike = False,
    )
    
    other_font = Font(
        family="Cambria Math",
        size = 20,
        slant = 'roman',
        underline = False,
        overstrike=False
    )
    
    # Giving the signup window a heading
    heading = Label(win, text = "USER DETAILS", font = my_font)
    heading.grid(row=0, column=0, columnspan=2)
    
    # Email id label and entry
    email = Label(win, text = "Enter your Email ID", font = other_font)
    email.grid(row=1, column=0, columnspan=2, pady=20)
    email_entry = Entry(win, textvariable=StringVar(), font=other_font)
    email_entry.grid(row=2, column=0, columnspan=2)
    
    # First name label and entry
    first_name = Label(win, text = "Enter your First Name", font = other_font, pady = 20)
    first_name.grid(row = 3, column = 0)
    first_name_entry = Entry(win, textvariable=StringVar(), font=other_font)
    first_name_entry.grid(row=4, column = 0)
    
    # Last name label and entry 
    last_name = Label(win, text="Enter your Last Name", font=other_font, padx=40, pady = 20)
    last_name.grid(row=3, column = 1)
    last_name_entry = Entry(win, textvariable=StringVar(), font=other_font)
    last_name_entry.grid(row=4, column =1, padx=40)
    
    # Occupation label and entry 
    occupation = Label(win, text = "Enter your Occupation", font = other_font, pady = 20)
    occupation.grid(row = 5, column = 0)
    occupation_entry = Entry(win, textvariable=StringVar(), font=other_font)
    occupation_entry.grid(row = 6, column = 0)
    
    # Mobile number label and entry
    mobile = Label(win, text="Enter your mobile number", font = other_font, padx=40, pady=20)
    mobile.grid(row=5, column=1)
    mobile_entry = Entry(win, textvariable=IntVar(), font=other_font)
    mobile_entry.grid(row=6, column=1, padx=40)
    
    # Password label and entry
    password = Label(win, text = "Enter your Password", font = other_font, pady=20)
    password.grid(row=7, column =0)
    password_entry = Entry(win, textvariable=StringVar(), font=other_font)
    password_entry.grid(row=8, column=0)
    
    # Confirm password label and entry 
    confirm_pass = Label(win, text = "Confirm your Password", font = other_font, padx=40, pady=20)
    confirm_pass.grid(row=7, column = 1)
    confirm_pass_entry = Entry(win, textvariable=StringVar(), font=other_font)
    confirm_pass_entry.grid(row = 8, column = 1, padx = 40)
    
    # Defining a function to get the entries and store it in the database
    def signupgui():
        # Getting the entries from the entry widget
        fname = first_name_entry.get()
        lname = last_name_entry.get()
        emid = email_entry.get()
        occ = occupation_entry.get()
        mnum = mobile_entry.get()
        pwd = password_entry.get()
        conpwd = confirm_pass_entry.get()
        
        # defining a function to make warning window
        def warning():
            # Creating a new window
            war = Tk()
            war.title("Warning")
            war.iconbitmap("warning.ico")
            
            # creating a re check label
            label=Label(war, text = "Please re-check your password", padx=20, pady = 20)
            label.grid(row=0)
            
            # making a function to close the window when button is clicked
            def gotit():
                war.destroy()
            
            # Creating the button
            gotit_button = Button(war, text ="GOT IT", command = gotit)
            gotit_button.grid(row=1)
            
            war.mainloop()
        
        # Defining function to make success window
        def success():
            # Creating a new window
            succ = Tk()
            succ.title("Successful")
            succ.iconbitmap("CommonCents1.ico")
            
            # confirmation successful message label
            label = Label(succ, text = "Confirmation Successful\nYou can now login to expense manager", padx=20, pady=20)
            label.grid(row=0)
            
            # defining a function to close unwanted windows
            def ok():
                succ.destroy()
                win.destroy()
            
            # Creating a button ok button
            ok_button = Button(succ, text = "OK", command = ok)
            ok_button.grid(row=1)
            
            succ.mainloop()
        
        # Checking if entered password and confirmed password is same
        while True:
            if pwd == conpwd:
                insert = f"INSERT INTO login (Email_ID, First_Name, Last_Name, Occupation, Mobile_Number, Password) VALUE ('{emid}', '{fname}', '{lname}', '{occ}', {mnum}, '{pwd}')"
                mycur.execute(insert)
                mydb.commit()
                success()
                break    
            
            elif pwd != conpwd:
                warning()
                break
        


    # Creating a button to save the entered data in mysql database
    save_button = Button(win, text= "SAVE", font = other_font, command = signupgui)
    save_button.grid(row=11, column=0, columnspan=2, pady = 20)
    
    win.mainloop()


# Creating a button to perform signup operation
signup_button = Button(root, text="SIGNUP", font = other_font, command =  signup)
signup_button.grid(row=6, column=1)

root.mainloop()

# Creating main window
def expense_manager():
    # getting data from mysql table
    mycur.execute("SELECT * FROM outflow")
    table_outflow = mycur.fetchall()
    mycur.execute("SELECT * FROM inflow")
    table_inflow = mycur.fetchall()
    
    # making a window
    app = Tk()
    
    # defining its geometry and icon
    app.geometry("{0}x{1}+0+0".format(app.winfo_screenwidth(), app.winfo_screenheight()))
    app.iconbitmap("CommonCents1.ico")
    
    # Defining fonts
    my_font = Font(
        family = 'Cooper Black',
        size = 50,
        weight = 'bold',
        slant =  'roman',
        underline = True,
        overstrike = False  
    )

    other_font = Font(
        family="Bookman Old Style",
        size = 15,
        slant = 'roman',
        underline = False,
        overstrike= False,
    )

    # Giving the window a title
    app.title("WELCOME")

    # Adding welcome label 
    name = Label(app, text = "Welcome to CommonCents", font = my_font, anchor=CENTER)
    name.grid(row=0, column=0, columnspan=2)

    # Making a balace frame which will show the balance in the user's account
    frame2 = LabelFrame(app, text = "Balance")
    frame2.grid(row = 1, column = 1)

    # Making all the frames required for the GUI
    credit_details_frame = LabelFrame(app, text = "Credit Details")
    debit_details_frame = LabelFrame(app, text = "Debit Details")
    display_debit_frame = LabelFrame(app, text = "Table Display")
    display_credit_frame = LabelFrame(app, text = "Table Display")

    # Defining a function which will perform all the operations related to Credit details
    def credit_det():
        # Closing any other frame ( if any )
        if debit_details_frame.winfo_exists() == 1:
            debit_details_frame.grid_forget()
        if credit_details_frame.winfo_exists() == 1:
            credit_details_frame.grid_forget()
        if display_debit_frame.winfo_exists() ==1:
            display_debit_frame.grid_forget()
        if display_credit_frame.winfo_exists() == 1:
            display_credit_frame.grid_forget()
        
        # Adding Credit Frame in GUI
        credit_details_frame.grid(row = 2, column= 0, columnspan=2)

        # Putting Credit Details information frame in the window
        label3 = Label(credit_details_frame, text= "Enter the following details", foreground = "white", background = "black", font = other_font)
        label3.grid(row = 0, column = 0, columnspan=2)
        
        # Date label and entry
        credit_date = Label(credit_details_frame, text = "Date Credited (YYYY-MM-DD)", font = other_font)
        credit_date.grid(row = 1, column=0)
        credit_date_entry = Entry(credit_details_frame, textvariable=IntVar())
        credit_date_entry.grid(row=1, column=1)
        
        # Credit amount label and entry
        credited_amount = Label(credit_details_frame, text = "Credited Amount", font = other_font)
        credited_amount.grid(row = 1, column = 2, padx = 10)
        credited_amount_entry = Entry(credit_details_frame, textvariable=IntVar())
        credited_amount_entry.grid(row = 1, column = 3)

        # Mode of credit label and entry
        moc = Label(credit_details_frame, text = "Mode of Credit", font = other_font)
        moc.grid(row = 2, column =0)
        moc_list = ttk.Combobox(credit_details_frame, textvariable=StringVar())
        moc_list['values'] = ('Cash', 'Debit Card', 'Net Banking', 'UPI', 'Other')
        moc_list.grid(row = 2, column = 1)

        # Extra note label and entry
        note = Label(credit_details_frame, text = "Extra Note (*Optional)", font = other_font)
        note.grid(row=2, column=2)
        extra_note = Entry(credit_details_frame, textvariable=StringVar())
        extra_note.grid(row=2, column=3, columnspan=6)
        
        # Displaying the table
        
        display_credit_frame.grid(row=3, column=0, columnspan=2)
        
        # Defining a treeview
        trv = ttk.Treeview(display_credit_frame, selectmode='browse', height=22)
        style = ttk.Style()
        
        # Configuring a treeview
        style.configure('Treeview.Heading', font = other_font)
        style.configure('Treeview.column', font = other_font)
        
        trv.grid(row=0, column=0)
        
        # Specifying number of columns and heading
        trv['columns'] = ('1','2','3','4','5')
        trv['show'] = 'headings'
        
        # Defining the name of first row and column width
        trv.column('1', width=150)
        trv.column('2', width=300)
        trv.column('3', width=300)
        trv.column('4', width=300)
        trv.column('5', width=375)
        
        trv.heading('1', text = 'S No')
        trv.heading('2', text = 'Date')
        trv.heading('3', text = 'Amount Credited')
        trv.heading('4', text = 'Mode of Credit')
        trv.heading('5', text = 'Note')
        
        # Inserting the values in the treeview
        for dt in table_inflow:
            trv.insert("",'end',iid=dt[0], values=(dt[0], dt[1], dt[2], dt[3], dt[4]))
        
        # Defining a function which will put the values in the treeview and database
        def saving():
            # inserting the values in the table
            inserting = f"INSERT INTO inflow (Date, Credited_Amount, Mode_of_Credit, Note) VALUE ('{credit_date_entry.get()}',{int(credited_amount_entry.get())},'{moc_list.get()}','{extra_note.get()}')"
            mycur.execute(inserting)
            mydb.commit()

            # Getting data from mysql database
            mycur.execute("SELECT * FROM inflow")
            table_inflow = mycur.fetchall()
            
            # Re-defining the treeview
            trv = ttk.Treeview(display_credit_frame, selectmode='browse', height=22)
            style = ttk.Style()
            
            # Configuring a treeview
            style.configure('Treeview.Heading', font = other_font)
            style.configure('Treeview.column', font = other_font)
            
            trv.grid(row=0, column=0)
            
            # Specifying number of columns and heading
            trv['columns'] = ('1','2','3','4','5')
            trv['show'] = 'headings'
            
            # Defining the name of first row and column width
            trv.column('1', width=150)
            trv.column('2', width=300)
            trv.column('3', width=300)
            trv.column('4', width=300)
            trv.column('5', width=375)
            
            trv.heading('1', text = 'S No')
            trv.heading('2', text = 'Date')
            trv.heading('3', text = 'Amount Credited')
            trv.heading('4', text = 'Mode of Credit')
            trv.heading('5', text = 'Note')
            
            # Inserting the values in the treeview
            for dt in table_inflow:
                trv.insert("",'end',iid=dt[0], values=(dt[0], dt[1], dt[2], dt[3], dt[4]))
            
            # Emptying the entries after saving
            credit_date_entry.delete(0,END)
            credited_amount_entry.delete(0,END)
            moc_list.delete(0,END)
            extra_note.delete(0,END)
        
        # Making a button which will perform saving operation
        save_button = Button(credit_details_frame, text="SAVE", font = other_font, command=saving)
        save_button.grid(row = 4, column=0, columnspan=6)
        
    # Defining a function which will perform all the operations related to Debit details
    def debit_det():
        # Closing any other frame ( if any )
        if credit_details_frame.winfo_exists() == 1:
            credit_details_frame.grid_forget()
        if debit_details_frame.winfo_exists() == 1:
            debit_details_frame.grid_forget()
        if display_debit_frame.winfo_exists() ==1:
            display_debit_frame.grid_forget()
        if display_credit_frame.winfo_exists() == 1:
            display_credit_frame.grid_forget()
        
        # Adding Debit Frame in GUI
        debit_details_frame.grid(row = 2, column= 0, columnspan=2)
        
        # Putting Credit Details information frame in the window
        label3 = Label(debit_details_frame, text= "Enter the following details", foreground = "white", background = "black", font = other_font)
        label3.grid(row = 0, column = 0, columnspan=2)
        
        # Date label and entry
        debit_date = Label(debit_details_frame, text = "Date Debited (YYYY-MM-DD)", font = other_font)
        debit_date.grid(row = 1, column=0)
        debit_date_entry = Entry(debit_details_frame, textvariable=StringVar())
        debit_date_entry.grid(row=1, column=1)
        
        # Debit amount label and entry
        debited_amount = Label(debit_details_frame, text = "Debited Amount", font = other_font)
        debited_amount.grid(row = 1, column = 2, padx = 10)
        debited_amount_entry = Entry(debit_details_frame, textvariable=StringVar())
        debited_amount_entry.grid(row = 1, column = 3)
        
        # Mode of payment label and entry
        mop = Label(debit_details_frame, text = "Mode of Debit", font = other_font)
        mop.grid(row = 2, column =0)
        mop_list = ttk.Combobox(debit_details_frame, textvariable=StringVar())
        mop_list['values'] = ('Cash', 'Debit Card', 'Net Banking', 'UPI', 'Other')
        mop_list.grid(row = 2, column = 1)
        
        # Expenditure label and entry
        expenditure = Label(debit_details_frame, text = "Expenditure Type", font = other_font)
        expenditure.grid(row=2, column=2)
        expenditure_list = ttk.Combobox(debit_details_frame, textvariable=StringVar())
        expenditure_list['values'] = ('EMI', 'Maintenance', 'Shopping', 'Food', 'Health', 'Entertainment', 'Travelling', 'Other')
        expenditure_list.grid(row = 2, column=3)
        
        # Extra note label and entry
        note = Label(debit_details_frame, text = "Extra Note (*Optional)", font = other_font)
        note.grid(row=3, column=0, columnspan=2)
        extra_note = Entry(debit_details_frame, textvariable=StringVar())
        extra_note.grid(row=3, column=1, columnspan=2)
        
        # Making a frame where treeview will be places
        display_debit_frame.grid(row=3, column = 0, columnspan=2)
        
        # Defining the treeview
        trv = ttk.Treeview(display_debit_frame, selectmode='browse', height=21)
        style = ttk.Style()
        
        # Configuring the treeview
        style.configure('Treeview.Heading', font = other_font)
        style.configure('Treeview.column', font = other_font)
        
        trv.grid(row=1, column=1)
        
        # Specifying number of columns and heading
        trv['columns'] = ('1','2','3','4','5','6')
        trv['show'] = 'headings'
        
        # Defining the name of first row and column width
        trv.column('1', width=100)
        trv.column('2', width=250)
        trv.column('3', width=250)
        trv.column('4', width=250)
        trv.column('5', width=250)
        trv.column('6', width=350)
        
        trv.heading('1', text = 'S No')
        trv.heading('2', text = 'Date')
        trv.heading('3', text = 'Amount Debited')
        trv.heading('4', text = 'Mode of Payment')
        trv.heading('5', text = 'Expenditure')
        trv.heading('6', text = 'Note')
        
        # Inserting the values in the treeview
        for dt in table_outflow:
            trv.insert("",'end',iid=dt[0], values=(dt[0], dt[1], dt[2], dt[3], dt[4], dt[5]))
        
        # Defining a function which will put the values in the treeview and database
        def saving():
            # inserting the values in the table
            inserting = f"INSERT INTO outflow (Date, Debited_Amount, Mode_of_Payment, Expenditure, Note) VALUE ('{debit_date_entry.get()}',{int(debited_amount_entry.get())},'{mop_list.get()}','{expenditure_list.get()}','{extra_note.get()}')"
            mycur.execute(inserting)
            mydb.commit()
            
            # Getting data from mysql database
            mycur.execute("SELECT * FROM outflow")
            table_outflow = mycur.fetchall()
            
            # Re-defining the treeview
            trv = ttk.Treeview(display_debit_frame, selectmode='browse', height=21)
            style = ttk.Style()
            
            # Configuring a treeview
            style.configure('Treeview.Heading', font = other_font)
            style.configure('Treeview.column', font = other_font)
            
            trv.grid(row=1, column=1)
            
            # Specifying number of columns and heading
            trv['columns'] = ('1','2','3','4','5','6')
            trv['show'] = 'headings'
            
            # Defining the name of first row and column width
            trv.column('1', width=100)
            trv.column('2', width=250)
            trv.column('3', width=250)
            trv.column('4', width=250)
            trv.column('5', width=250)
            trv.column('6', width=350)
            
            trv.heading('1', text = 'S No')
            trv.heading('2', text = 'Date')
            trv.heading('3', text = 'Amount Debited')
            trv.heading('4', text = 'Mode of Payment')
            trv.heading('5', text = 'Expenditure')
            trv.heading('6', text = 'Note')
            
            # Inserting the values in the treeview
            for dt in table_outflow:         # type: ignore
                trv.insert("",'end',iid=dt[0], values=(dt[0], dt[1], dt[2], dt[3], dt[4], dt[5]))
            
            # Emptying the entries after saving
            debit_date_entry.delete(0,END)    
            debited_amount_entry.delete(0,END)
            mop_list.delete(0,END)
            expenditure_list.delete(0,END)
            extra_note.delete(0,END)
        
        # Making a button which will perform saving operation
        save_button = Button(debit_details_frame, text="SAVE", font = other_font, command=saving)
        save_button.grid(row = 4, column=0, columnspan=4)

    # Creating another frame for credit and debit button
    frame1 = LabelFrame(app, text = "Choose One")
    frame1.grid(row = 1, column = 0)
    
    # Debit and credit information label
    label1 = Label(frame1, text = "Click DEBIT if you want to enter money outflow details\nClick CREDIT if you want to enter money inflow details", font = other_font)
    label1.grid(row = 0, column=0, columnspan=2)
    
    # Debit and credit button
    debit_button = Button(frame1, text = 'DEBIT', font = other_font, command = debit_det)
    debit_button.grid(row = 1, column = 0)
    credit_button = Button(frame1, text = "CREDIT", font = other_font, command = credit_det)
    credit_button.grid(row =1, column = 1)

    # Creating another label and entry widget to display total balance
    label2 = Label(frame2, text = "Total Balance", font = other_font)
    label2.grid(row =1, column = 0, columnspan=2)
    balance = Entry(frame2, font=other_font)
    balance.grid(row = 2, column = 0, columnspan=2)

    # Defining update function which will update the value of total credit
    def update():
        # Getting credited amount from database
        mycur.execute("SELECT Credited_Amount from inflow")
        credit_amount_entries = mycur.fetchall()

        # Creating an empty list
        l1=[]

        # Looping through credit amount list and appending it to empty list l1
        for i in credit_amount_entries:
            a = i[0]
            l1.append(a)

        # Total credited amount is the sum of all credited amounts
        total_credited_amount = sum(l1)

        # Getting debited amount from the database
        mycur.execute("SELECT Debited_Amount from outflow")
        debit_amount_entries = mycur.fetchall()

        # Creating an empty list
        l2=[]

        # Looping through debit amount list and appending it to empty list l2
        for i in debit_amount_entries:
            a = i[0]
            l2.append(a)

        # Total debited amount is the sum of all debited amounts
        total_debited_amount = sum(l2)

        # Total balance is total credited amount minus total debited amount
        total_balance = (total_credited_amount - total_debited_amount)
        balance.insert(INSERT, total_balance)

        # Deleting the entry to prevent overlapping
        balance.delete(0, END)
        total_balance = (total_credited_amount - total_debited_amount)
        balance.insert(INSERT, total_balance)
    
    # Creating an update button
    update_button = Button(frame2, text = "UPDATE", font = other_font, command=update)
    update_button.grid(row = 3,columnspan=2)

    app.mainloop()

# Calling the function
expense_manager()