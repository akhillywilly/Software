import tkinter as tk


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ρσкєямєη")
        self.geometry("400x300")

        # Create container to hold all frames
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        # Dictionary to hold references to all frames
        self.frames = {}

        # Initialize frames
        for F in (MenuScreen, StartScreen):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame

            # Put all frames in the same location
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the initial frame
        self.show_frame("MenuScreen")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class MenuScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = tk.Label(self,text="""
HELLO! and welcome to:

ρσкєямєη

""", font=("Arial",18))
        label.pack()

        buttonframe = tk.Frame(self)
        buttonframe.columnconfigure(0,weight=1)
        buttonframe.columnconfigure(1,weight=1)
        buttonframe.columnconfigure(2,weight=1)

        start_button = tk.Button(buttonframe,text="Start",height=2 ,width=10,font=('Arial',18), command=lambda: controller.show_frame("StartScreen"))
        start_button.grid(row=0,column=0,pady=4)
        help_button = tk.Button(buttonframe,text="Help ",height=2 ,width=10,font=('Arial',18))
        help_button.grid(row=1,column=0,pady=4)
        quit_button = tk.Button(buttonframe,text="Quit ",height=2 ,width=10,font=('Arial',18))
        quit_button.grid(row=2,column=0,pady=4)

        buttonframe.pack()


class StartScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="This is the start screen",font=('Arial',19))
        label.pack(side="top", fill="x", pady=10)
        buttonframe = tk.Frame(self)
        buttonframe.columnconfigure(0,weight=1)
        buttonframe.columnconfigure(1,weight=1)
        buttonframe.columnconfigure(2,weight=1)

        start_button = tk.Button(buttonframe,text="Start",height=2 ,width=10,font=('Arial',18), command=lambda: controller.show_frame("StartScreen"))
        start_button.grid(row=0,column=0,pady=4)
        help_button = tk.Button(buttonframe,text="Help ",height=2 ,width=10,font=('Arial',18))
        help_button.grid(row=1,column=0,pady=4)
        quit_button = tk.Button(buttonframe,text="Quit ",height=2 ,width=10,font=('Arial',18))
        quit_button.grid(row=2,column=0,pady=4)
        buttonframe.pack()

if __name__ == "__main__":
    app = Application()
    app.mainloop()


