import tkinter
class App(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):

        global dev, label, Label1, Label2, Label3, Label4, Label5, Label6
    Label1 = tkinter.Label(self,text="Label1")
    Label2 = tkinter.Label(self,text="Label2")
    Label3 = Tkinter.Label(self,text="Label3")
    Label4 = Tkinter.Label(self,text="Label4")
    Label5 = Tkinter.Label(self,text="Label5")
    Label6 = Tkinter.Label(self,text="Label6")