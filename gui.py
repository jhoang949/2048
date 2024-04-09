import tkinter as tk


class Game(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title('2048')
        self.geometry('600x800')
        self.mainloop()
                

if __name__ == "__main__":
    Game()