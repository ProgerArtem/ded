#-*- codding:utf-8 -*-
from tkinter import *
from logic import Search_engine
from tkinter import messagebox
#skoro konez
class Window(Tk):
    def __init__(self):
        super().__init__()
        self.db_search = Search_engine()

        Label(self ,text="Введіть пошуковий запит:").grid(
           row = 0, column=0, columnspan=2, rowspan=3 
        )
        self.search_text = StringVar()
        self.entry_search = Entry(self, width=60, 
                                  textvariable=self.search_text)
        self.search_but = Button(self, text="Пошук",
                                 command=self.search)
        self.entry_search.grid(row=3, column=0,
                               columnspan=2)
        self.search_but.grid(row=3, column=2)
        self.db_search = Search_engine()
        self.ganre_var = StringVar()
        self.ganre_var.set("Genre:")
        self.avtor_var = StringVar()
        self.avtor_var.set("Author")
    
        Label(self ,textvariable= self.avtor_var).grid(
           row = 5, column=2, columnspan=1 
        )
        Label(self ,textvariable= self.ganre_var).grid(
           row = 6, column=2, columnspan=1 
        )
        

        self.list_track = Listbox(self, width=60, height=15)
        self.list_track.grid(row=4, column=0, columnspan=2,
                             rowspan=3,
                             sticky=W)
        self.mode_var = StringVar()
        self.mode_var.set("tracks")
        dict_modes = { "Search in tracks": "tracks",
                       "Search in authors": "authors",
                       "Search in genres": "genres"


        }
        for i, (text, val) in enumerate(dict_modes.items()):
            r1 = Radiobutton(self, text=text,
                              variable=self.mode_var,
                              value=val)
            r1.grid(row=i, column=2, sticky=W) 
        self.list_track.bind('<<ListboxSelect>>',   self.on_change)
    def on_change(self, event):
        widget = event.widget
        selection = widget.curselection()
        if selection:
            text = widget.get(selection[0])  
            print(text)
            self.ganre_var.set(self.db_search.select(text))
            self.avtor_var.set(self.db_search.albom(text))
        
        messagebox.showinfo('Title', self.db_search.select(text))
        print()
    def search(self):
        print("Text from entry:",self.search_text.get())
        text = self.search_text.get()
        result = self.db_search.search_track(text)
        print (result)
        self.list_track.delete(0, END)
        for row in result:
            self.list_track.insert(END, row[0])
        
    def new_window(self):
        Window().mainloop()
if __name__=="__main__":
    root = Window()
    root.geometry("600x400")
    root.mainloop()