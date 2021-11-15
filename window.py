
#-*- codding:utf-8 -*-
from tkinter import *
from logic import Search_engine

class Window(Tk):
    def __init__(self):
        super().__init__()
        self.db_search = Search_engine()
        Label(self ,text="Введіть пошуковий запит:").grid(
           row = 0, column=0, columnspan=2 
        )
        self.search_text = StringVar()
        self.entry_search = Entry(self, width=60, 
                                  textvariable=self.search_text)
        self.search_but = Button(self, text="Пошук",
                                 command=self.search)
        self.entry_search.grid(row=1, column=0,
                               columnspan=2)
        self.search_but.grid(row=1, column=2)
                                   
    def search(self):
        print("Text from entry:",self.search_text.get())
        text = self.search_text.get()
        result = self.db_search.search_track(text)
        print (result)
if __name__=="__main__":
    root = Window()
    root.geometry("600x400")
    root.mainloop()