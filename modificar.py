import csv
from tkinter import *
from tkinter import messagebox as MessageBox, ttk

class modificarRegistro():
    def __init__(self, root, val_modify):

        self.root_window = root
        self.val_modify = val_modify
        self.name = str(self.val_modify[0])
        self.id = str(self.val_modify[1])
        self.nacionalidad = str(self.val_modify[2])
        self.telefono = str(self.val_modify[3])

        def modify_mesageBox(contact):
            var_name = str(contact[0])
            var_id = str(contact[1])
            var_naci = str(contact[2])
            var_tel= str(contact[3])

            search = MessageBox.askquestion("Alerta de modificacion",
                                            "Desea guardar los cambios realizados en este registro?\n" + " Nombre: " + var_name + "\n Id: " + var_id + "\n nacionalidad: "+ var_naci+ "\n Telefono: "+var_tel)
            if search == "yes":

                return True
            else:
                return False

        window_modify = Toplevel(self.root_window)
        window_modify.title("Modificar registro")
        window_modify.configure(bg="#53CDB8")
        window_modify.geometry("+400+100")
        window_modify.resizable(0, 0)

        # ---------------- FRAMES DECLARATION -----------------
        text_frame = LabelFrame(window_modify, bg="#53CDB8")
        text_frame.grid(row=0, column=0)

        button_frame = LabelFrame(window_modify, bg="#53CDB8")
        button_frame.grid(row=2, column=0)

        # --------------- LABELS WIDGETS ZONE -----------------
        Label(text_frame, text="Quiere modificar este registro?", bg="#53CDB8",
              font=("Comic Sans MS", "11", "normal")).grid(row=0, column=0, columnspan=3)
        Label(text_frame, text=self.name, bg="#53CDB8", font=("Comic Sans MS", "11", "bold")).grid(row=1,
                                                                                                   column=0)
        Label(text_frame, text=self.id, bg="#53CDB8", font=("Comic Sans MS", "11", "bold")).grid(row=1,
                                                                                                    column=1)
        Label(text_frame, text=self.nacionalidad, bg="#53CDB8", font=("Comic Sans MS", "11", "bold")).grid(row=1,
                                                                                                 column=2)

        Label(text_frame, text=self.telefono, bg="#53CDB8", font=("Comic Sans MS", "11", "bold")).grid(row=1,
                                                                                                 column=3)

        # --------------- INBOX WIDGETS ZONE ------------------
        Label(text_frame, text='Escriba el nombre', bg="#53CDB8", font=("Comic Sans MS", "11", "normal")).grid(
            row=2,
            column=0)
        n_inbox_name = Entry(text_frame, font=("Comic Sans MS", "11", "normal"), width=28)
        n_inbox_name.grid(row=3, column=0)
        n_inbox_name.focus()

        Label(text_frame, text='Escriba  numero de identificacion', bg="#53CDB8", font=("Comic Sans MS", "11", "normal")).grid(
            row=2,
            column=1)
        n_inbox_id = Entry(text_frame, font=("Comic Sans MS", "11", "normal"), width=20)
        n_inbox_id.grid(row=3, column=1)

        Label(text_frame, text='Escriba  nacionalidad', bg="#53CDB8",
              font=("Comic Sans MS", "11", "normal")).grid(
            row=2,
            column=2)
        n_inbox_nac = Entry(text_frame, font=("Comic Sans MS", "11", "normal"), width=20)
        n_inbox_nac.grid(row=3, column=2)

        Label(text_frame, text='Escriba  numero de telefono', bg="#53CDB8",
              font=("Comic Sans MS", "11", "normal")).grid(
            row=2,
            column=3)
        n_inbox_tel = Entry(text_frame, font=("Comic Sans MS", "11", "normal"), width=20)
        n_inbox_tel.grid(row=3, column=3)


        # --------------- BUTTON WIDGETS ZONE -----------------
        yes_button = Button(button_frame, command=lambda: yes(), text='Yes', width=20)
        yes_button.configure(bg="#F26262", cursor='hand2', font=("Comic Sans MS", "10", "normal"))
        yes_button.grid(row=1, column=0, padx=2, pady=3, sticky=W + E)

        no_button = Button(button_frame, command=window_modify.destroy, text='No', width=20, bg="yellow",
                           cursor='hand2')
        no_button.configure(bg="#FFBB20", cursor='hand2', font=("Comic Sans MS", "10", "normal"))
        no_button.grid(row=1, column=1, padx=2, pady=3, sticky=W + E)

        cancel_button = Button(button_frame, command=window_modify.destroy, text='Cancel', width=20, bg="green",
                               cursor='hand2')
        cancel_button.configure(bg="#FFBB20", cursor='hand2', font=("Comic Sans MS", "10", "normal"))
        cancel_button.grid(row=1, column=2, padx=2, pady=3, sticky=W + E)

        # ----------------- BUTTON FUNCTIONS ------------------
        def yes():
            contact = self.val_modify
            new_name = n_inbox_name.get()
            new_id = n_inbox_id.get()
            new_nac = n_inbox_nac.get()
            new_tel= n_inbox_tel.get()

            a = modify_mesageBox(contact)
            if a == True:
                _del_old(contact[0])
                _add_new(new_name, new_id,new_nac,new_tel)
            window_modify.destroy()

        def _add_new(name, id,nac,tel):
            s_name = name
            s_id = id
            s_nac = nac
            s_tel =tel

            with open('People_list.csv', 'a') as f:
                writer = csv.writer(f, lineterminator='\r', delimiter=',')
                writer.writerow((s_name, s_id, s_nac,s_tel))

        def _del_old(old_name):
            name = old_name
            with open('People_list.csv', 'r') as f:
                reader = list(csv.reader(f))
            with open('People_list.csv', 'w') as f:
                writer = csv.writer(f, lineterminator='\r', delimiter=',')
                for i, row in enumerate(reader):
                    if name != row[0]:
                        writer.writerow(row)
