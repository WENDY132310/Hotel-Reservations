from tkinter import *
from tkinter import messagebox as MessageBox
import administrador
import csv
import usuariotitular


class login():

    def __init__(self, root):
        self.window = root

        global verifica_usuario
        global verifica_clave
        vfr = BooleanVar()
        verifica_usuario = StringVar()
        verifica_clave = StringVar()

        # -------Message box----------
        def no_found(var):
            var_s = str(var)
            MessageBox.showinfo("No se encuentra el registro ",
                                "Usuario " + var_s + ' ' + "Por favor Ingrese correctamente los datos")

        def write_user():
            MessageBox.showinfo("Registro usuario",
                                "Registre los datos para la creacion de el nuevo usuario")

        # --------Funciones auxiliares

        def _clean_inbox(dato1, dato2):
            dato1.delete(0, 'end')
            dato2.delete(0, 'end')

        def _save(user, password):
            s_name = user
            s_phone = password

            with open('Lista_usuario.csv', 'a') as f:
                writer = csv.writer(f, lineterminator='\r', delimiter=',')
                writer.writerow((s_name, s_phone))

        def _search(var_inboxUser, var_inboxContra, possitionuser, possitioncontra):
            my_list = []
            s_var_inboxuser = str(var_inboxUser)
            var_possitionuser = int(possitionuser)
            s_var_inboxcon = str(var_inboxContra)
            var_possitioncon = int(possitioncontra)
            with open('Lista_usuario.csv', 'r') as f:
                reader = csv.reader(f)
                for i, row in enumerate(reader):
                    if s_var_inboxuser == row[var_possitionuser] and s_var_inboxcon == row[var_possitioncon]:
                        my_list = [row[0], row[1]]
                        break

                    else:
                        continue
            return my_list

        def _check(answer, var_search):
            list_answer = answer
            var_search = var_search
            if not list_answer:
                no_found(var_search)
            elif var_search == "":
                no_found(var_search)
            else:
                vrf = True
                name = str(list_answer[0])
                password = str(list_answer[1])
                if vfr:
                    administrador.admin(root)

            # -------------funcion boton acceder log in

        def search():
            answer = []
            var_inbox = StringVar()
            var_inbox1 = StringVar()
            var_inbox = inbox_contra.get()
            var_inbox1 = inbox_user.get()
            possition1 = 0
            possition = 1
            if _search(var_inbox1, var_inbox, possition1, possition):
                print("entro")
                if var_inbox1 == "" or var_inbox == "":
                    vrf = False

                vrf = False
                answer = _search(var_inbox1, var_inbox, possition1, possition)
                _check(answer, var_inbox1)
            else:
                write_user()

            _clean_inbox(inbox_user, inbox_contra)

        def Clientes():

            usuariotitular.user(root)

        # -------- Frame principal logIn---------
        inbox_frame = LabelFrame(self.window, bg="#53CDB8", width=300, height=80, padx=4, pady=5)
        inbox_frame.grid(row=0, column=0)

        button_frame = LabelFrame(self.window, bg="#53CDB8")
        button_frame.grid(row=3, column=0)

        Label(inbox_frame, text='Bienvenido!!!', bg="#53CDB8", font=("Comic Sans MS", "30", "bold")).grid(row=1,
                                                                                                          column=0)

        Label(inbox_frame, text='Usuario', bg="#53CDB8", font=("Comic Sans MS", "11", "bold")).grid(row=2, column=0)

        inbox_user = Entry(inbox_frame, textvariable=verifica_usuario, font=("Comic Sans MS", "11", "normal"), width=50)
        inbox_user.grid(row=3, column=0, padx=30, pady=5)
        inbox_user.focus()

        Label(inbox_frame, text='Contraseña', bg="#53CDB8", font=("Comic Sans MS", "11", "bold")).grid(row=5,
                                                                                                       column=0)
        inbox_contra = Entry(inbox_frame, textvariable=verifica_clave, font=("Comic Sans MS", "11", "normal"), width=50,
                             show='*')
        inbox_contra.grid(row=6, column=0, padx=30, pady=5)

        acceder_button = Button(button_frame, text='Acceder', width=20, command=lambda: search())
        acceder_button.configure(bg="#FFBB20", cursor='hand2', font=("Comic Sans MS", "10", "normal"))
        acceder_button.grid(row=0, column=1, padx=2, pady=3, sticky=W + E)

        usuario_button = Button(button_frame, text='Clientes', width=20, command=lambda: Clientes())
        usuario_button.configure(bg="#FFBB20", cursor='hand2', font=("Comic Sans MS", "10", "normal"))
        usuario_button.grid(row=0, column=2, padx=2, pady=3, sticky=W + E)
