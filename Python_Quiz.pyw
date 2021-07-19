from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title('Quiz')
root.geometry("1600x800")
a = Frame(root)
a.pack(side="top", expand=True, fill="both")



sports = {"Question":["Q1. In Australian football, what is the maximum number of players allowed on the field at a time?",
                 "Q2. What player was the first to win five straight Wimbledon tennis titles?",
                 "Q3. In polo, what is a period of play called?",
                 "Q4. In tennis, what follows a deuce?",
                 "Q5. What variation might one play in tennis?"],
     "Answer":[2,1,4,3,3],
     "Options":[['25', '36', '40','14'],
                ['Bjorn Borg', 'Andre Agassi', 'Roger Federer', 'Arthur Ashe'],
                ['half','set','quarter','chukka'],
                ['adverd','advection','advantage','advertisement'],
                ['Australian Rules','Australian Lager','Australian Doubles','Australian Crawl']]}


technology = {"Question":["Q1. Who was the first person to create a Computer?",
                 "Q2. Which computer language is the most widely used?",
                 "Q3. About how many computer languages are in use?",
                 "Q4. What does WWW stand for in a URL?",
                 "Q5. Which of these is not an early computer?"],
     "Answer":[4,2,3,2,4],
     "Options":[['Benjamin Franklin', 'Nikola Tesla', 'Thomas Edison', 'Charles Babbage'],
                ['SQL', 'Javascript', 'Python', 'HTML'],
                ['10', '5,000', '2,000', '50'],
                ['Western Washington World', 'World Wide Web', 'Wide Width Wickets', 'World With Water'],
                ['UNIVAC', 'SAGE', 'ENIAC', 'NASA']]}


geography = {"Question":["Q1. Which country has the longest coastline in the world?",
                 "Q2. What is the capital of the Algeria?",
                 "Q3. What is the World's Smallest River",
                 "Q4. What is the World's Most Largest Country?",
                 "Q5. What is the World's Most Smallest City?"],
     "Answer":[3,2,1,4,1],
     "Options":[['Russia', 'Indonesia', 'Canada', 'Australia'],
                ['Wellington', 'Algiers', 'Delhi', 'Ottawa'],
                ['Roe River', '', 'Nile River', 'Mississippi River','Congo River'],
                ['Brazil', 'USA', 'South Africa', 'Russia'],
                ['Vatican City', 'Canberra', 'Tokyo', 'Ajman']]}




que1 = (sports['Question'])
ans1 = (sports['Answer'])
opt1 = (sports['Options'])

que2 = (technology['Question'])
ans2 = (technology['Answer'])
opt2 = (technology['Options'])

que3 = (geography['Question'])
ans3 = (geography['Answer'])
opt3 = (geography['Options'])

xyz = que1
yxz = ans1
zyx = opt1


class quiz:
    def __init__(self):
        self.qno = 0
        self.cor = 0
        self.length = len(xyz)
        self.optselected = IntVar()
        self.menubar()
        self.displaytitle("XYZ Quiz")
        self.welcome_screen()
    def welcome_screen(Self):
        l1 = Label(a, text = "Welcome To XYZ Quiz ", width = 50, bg = 'green',fg = 'black', font = ('arial',30,'bold'))
        l1.place(x = 120, y = 100)
      
        #Setting it up
        #img = ImageTk.PhotoImage(Image.open("quiz-time.jpg"))


        #Displaying it
        #imglabel = Label(a, image=img, width = 700, height =500)
        #imglabel.image = img
        #imglabel.place(x=400, y = 200)
       

    def clear_frame(self):
        for widgets in a.winfo_children():
            widgets.destroy()
        self.qno = 0
        self.cor = 0

    def createradiobutton(self):
        v1 = []
        v2 = 150
        while len(v1) < 4:
            abc = Radiobutton(a, text = ' ', variable = self.optselected , fg = 'black', font = ('Metropolis',18,''), value = len(v1) + 1)
            abc.place(x = 100, y = v2)
            v1.append(abc)
            v2 = v2 + 40
        return v1
    def dest(self):
        messagebox.showinfo("Bye!","Thank You For Playing XYZ Quiz! \n Have A Good Day!")
        root.destroy()
    def displayoptions(self):
        count = 0
        for v3 in zyx[self.qno]:
            self.radiobuttoncontrol[count]['text'] = v3
            count = count + 1
    def displaytitle(self, title):
        l1 = Label(a, text = title, width = 100, bg = 'red',fg = 'black', font = ('Metropolis',20,'bold'))
        l1.place(x = -150, y = 0)
    def displayquestion(self):
        l2 = Label(a, text = xyz[self.qno], width = 100, bg = 'green', fg = 'white', font = ('Metropolis',15,''))
        l2.place(x = 100, y = 70)
    def createbutton(self):
        b1 = Button(a, text = 'Next', command = self.nextbutton, width = 10,height = 2, bg = 'red', fg = 'white',font = ('Metropolis',20,'bold'))
        b2 = Button(a, text = 'Exit', command = self.dest, width = 10,height = 2, bg = 'green', fg = 'white',font = ('Metropolis',20,'bold'))
        b1.place(x = 350, y = 350)
        b2.place(x = 600, y = 350)
    def checkanswer(self, questiono):
        if self.optselected.get() == yxz[questiono]:
            return True
    def displayresult(self):
        wrong = self.length - self.cor
        wrong = f"Wrong: {wrong}"
        abc = f"correct: {self.cor}"
        percentage = self.cor / self.length * 100
        Result = f"percentage: {percentage}%"
        messagebox.showinfo("Result",f"{abc}\n{wrong}\n{Result}")
    def nextbutton(self):
        if self.checkanswer(self.qno):
            self.cor = self.cor + 1
        self.qno = self.qno + 1
        if self.qno == self.length:
            self.displayresult()
            self.clear_frame()
            self.displaytitle("XYZ Quiz")
            self.welcome_screen()
        else:
            self.displayquestion()
            self.displayoptions()

    def sports1(self):

        global xyz
        global yxz
        global zyx
        global l1
        xyz = que1
        yxz = ans1
        zyx = opt1
        self.clear_frame()
        
        self.radiobuttoncontrol = self.createradiobutton()
        self.displaytitle("Sports Quiz")
        self.displayquestion()
        self.displayoptions()
        self.createbutton()
       
        
    def technology1(self):

        global xyz
        global yxz
        global zyx
        xyz = que2
        yxz = ans2
        zyx = opt2
        
        self.clear_frame()
        self.radiobuttoncontrol = self.createradiobutton()
        self.displaytitle("Technology Quiz")
        self.displayquestion()
        self.displayoptions()
        self.createbutton()
    
    def geography1(self):
        global xyz
        global yxz
        global zyx
        xyz = que3
        yxz = ans3
        zyx = opt3

        self.clear_frame()
        self.radiobuttoncontrol = self.createradiobutton()
        self.displaytitle("Geography Quiz")
        self.displayquestion()
        self.displayoptions()
        self.createbutton()       
        
    def about(self):
        messagebox.showinfo("About Quiz","Instructions:\n -The Category menu is used to change the topic of your choice \n -The Next button is to go to the next question \n -The Exit button is to leave the game ") 
    def menubar(self):
        MenuBar1 = Menu(root)
        SubMenu1 = Menu(MenuBar1, tearoff = 0)
        MenuBar1.add_cascade(label = 'Category', menu = SubMenu1)
        SubMenu1.add_command(label = 'Sports', command = self.sports1)
        SubMenu1.add_command(label = 'Technology', command = self.technology1)
        SubMenu1.add_command(label = 'Geography', command = self.geography1)

        SubMenu2 = Menu(MenuBar1, tearoff = 0)
        MenuBar1.add_cascade(label = 'Help', menu = SubMenu2)
        SubMenu2.add_command(label = 'About', command = self.about)

        root.config(menu = MenuBar1)
          
obj1 = quiz()
a.mainloop()
