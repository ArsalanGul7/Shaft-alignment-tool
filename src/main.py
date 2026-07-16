"""
main.py
----------------
Application launcher
for Shaft Alignment Tool.
"""
import tkinter as tk
from gui import ShaftAlignmentGUI
def main():
    root = tk.Tk()
    app = ShaftAlignmentGUI(root)
    root.mainloop()
if __name__ == "__main__":
    main()