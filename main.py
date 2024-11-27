from tkinter import *

class birthyear:
    
    def birthyear(self):
        
        self.screen=Tk()
        self.screen.title("age calculator app")
        self.screen.config(bg="Aquamarine")
        self.screen.geometry("500x500")
        
        self.agewelcome=Label(self.screen,text="Welcome to Age Calculator",font=("alice",20,"bold"),fg="black",bg="Aquamarine")
        self.agewelcome.pack()
        Label(self.screen,font=("alice",15,"bold"),bg="aquamarine").pack()


        self.agelabel=Label(self.screen,text="enter your birth year:",font=("alice",20,"bold"),fg="black",bg="Aquamarine")
        self.agelabel.pack()
        

        self.ageentry=Entry(self.screen,font=("alice",20,"bold"))
        self.ageentry.pack()
        Label(self.screen,font=("alice",15,"bold"),bg="aquamarine").pack()

        

        
        
        def confirmage():
            mybirth=int(self.ageentry.get())
            age=(2024-mybirth)
            my_age.config(text=f"you are {age} years old!")
            
        self.confirmage=Button(self.screen,text="calculate",font=("alice",20,"bold"),fg="black",bg="antiquewhite",command=confirmage)
        self.confirmage.pack()
       
        
        def refresh():
         my_age.config(text="")
        Label(self.screen,font=("alice",15,"bold"),bg="aquamarine").pack()

        reset=Button(self.screen,text="Reset",font=("Alice",10,"bold"),fg="black",bg="white",command=refresh)
        reset.pack()
        my_age=Label(self.screen,font=("Alice",10,"bold"),fg="black",bg="aquamarine")
        my_age.pack()


        self.screen.mainloop()


birthyear1=birthyear()
birthyear1.birthyear()