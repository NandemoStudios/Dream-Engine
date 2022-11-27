from customtkinter import *

usernames = ['Swyftl', 'ADMIN', 'TESTER']
passwords = ['PASS', 'ADMINPASS', 'TESTERPASS']

def Prompt(TextEntered, OneText, TwoText, OneCommand, TwoCommand):
    global PromptRoot
    PromptRoot = CTk()
    PromptRoot.title(TextEntered)
    PromptRoot.geometry("300x150")

    Question = CTkLabel(PromptRoot, text=TextEntered)

    ButtonOne = CTkButton(PromptRoot, text=OneText, command=OneCommand)
    ButtonTwo = CTkButton(PromptRoot, text=TwoText, command=TwoCommand)

    Question.place(relheight=0.5, relwidth=1.0)
    ButtonOne.place(relheight=0.25, relwidth=0.3, relx=0.1, rely=0.5)
    ButtonTwo.place(relheight=0.25, relwidth=0.3, relx=0.6, rely=0.5)

    PromptRoot.mainloop()

    return PromptRoot

'''

LOGIN FUNCTION

'''

def Login():
    global UsernameEntry
    global PasswordEntry
    global LoginRoot

    usernameCorrect = False
    passwordCorrect = False

    username = ""

    for usernamePoint in range(0,len(usernames)):
        if usernames[usernamePoint] == UsernameEntry.get():
            username = usernames[usernamePoint]
            usernameCorrect = True
    
    for passwordPoint in range(0,len(passwords)):
        if passwords[passwordPoint] == PasswordEntry.get():
            passwordCorrect = True

    if passwordCorrect == True and passwordCorrect == usernameCorrect:
        print("Logged in as", username)
        BuildMain(username)
    else:
        print("Username Or Password Not Found!")

'''

LOGIN BUILD

'''        

        
def BuildLogin():
    global LoginRoot
    global UsernameEntry
    global PasswordEntry

    LoginRoot = CTk()
    LoginRoot.title("Dream Window")
    LoginRoot.geometry("900x600")

    UsernameLabel = CTkLabel(LoginRoot, text="Username: ")
    UsernameEntry = CTkEntry(LoginRoot)

    PasswordLabel = CTkLabel(LoginRoot, text="Password: ")
    PasswordEntry = CTkEntry(LoginRoot)

    LoginButton = CTkButton(LoginRoot, text="Login", command=Login)

    ForgotPassword = CTkButton(LoginRoot, text="Forgot Password")

    UsernameLabel.place(relwidth=0.25, relheight=0.05, rely=0.1, relx=0.375)
    UsernameEntry.place(relwidth=0.25, relheight=0.05, rely=0.15, relx=0.375)

    PasswordLabel.place(relwidth=0.25, relheight=0.05, rely=0.25, relx=0.375)
    PasswordEntry.place(relwidth=0.25, relheight=0.05, rely=0.3, relx=0.375)

    LoginButton.place(relwidth=0.25, relheight=0.05, rely=0.4, relx=0.375)

    ForgotPassword.place(relwidth=0.25, relheight=0.05, rely=0.5, relx=0.375)

    LoginRoot.mainloop()

'''

BUILD MAIN WINDOW FUNCTION

'''

def BuildMain(username):
    global root
    LoginRoot.destroy()

    root = CTk()
    root.title(username+" | Dream Engine")
    root.geometry("900x600")

    root.protocol("WM_DELETE_WINDOW", on_closing_root)

    '''
    
    OPTION BAR CREATION
    
    '''

    global ModeOption

    ModeOption = CTkOptionMenu(root, values=['Dark', 'Light', 'System'], command=ModeChange)

    ModeOption.pack()

    root.mainloop()

'''

MODE CHANGE FUNCTION

'''

def ModeChange(choice):
    root.set_appearance_mode(choice.lower())
   
'''

MANAGE THE CLOSING OF THE WINDOW

'''

def CloseMainRoot():
    global root
    global PromptRoot
    root.destroy()
    PromptRoot.destroy()
    quit()

def CancelCloseRoot():
    global PromptRoot
    PromptRoot.destroy()

def on_closing_root():
    global PromptRoot
    wouldExit = 0
    ExitPrompt = Prompt("Would you like to exit?", "Yes", "Cancel", CloseMainRoot, CancelCloseRoot)

BuildLogin()
