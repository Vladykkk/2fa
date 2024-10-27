import tkinter as tk
from ui.main_interface import MainInterface

def main():
    root = tk.Tk()
    app = MainInterface(root)
    root.mainloop()

if __name__ == "__main__":
    main()
