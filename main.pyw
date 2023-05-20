from tkinter import *
import logIn


def main():
    root = Tk()
    root.title('AGENDA TU ESTADIA CON NOSOTROS')
    root.configure(bg="#27AEF2")
    root.geometry("+350+80")
    root.resizable(0, 0)
    logIn.login(root)
    root.mainloop()


if __name__ == "__main__":
    main()
