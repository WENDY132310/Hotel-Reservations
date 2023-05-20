from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import ttk
import orden
import csv
import modificar


class admin():
    def __init__(self, root):
        global frame_admin

        frame_admin = Toplevel(root)

        frame_admin.configure(bg="#27AEF2")
        frame_admin.title("Bievenido Administrador")
        frame_admin.geometry("+350+80")
        frame_admin.resizable(0, 0)

        def no_found(var):
            var_s = str(var)
            MessageBox.showinfo("No se encuentra el registro", var_s + ' ' + "no se encuentra el registro")

        def write_user():
            MessageBox.showinfo("Registro ",
                                "Registre los datos correctos ")

        def write_name():
            MessageBox.showinfo("No se encuentra", "por favor escriba un contacto")

        def delete_mesageBox(name):
            var_name = str(name)
            if var_name == '':
                write_name()
            else:
                search = MessageBox.askquestion("Alerta!!", "desea borrar este registro?\n" + var_name)
                if search == "yes":
                    return True
                else:
                    return False

        inbox_frame = LabelFrame(frame_admin, bg="#53CDB8")
        inbox_frame.grid(row=0, column=0)

        button_frame = LabelFrame(frame_admin, bg="#53CDB8")
        button_frame.grid(row=2, column=0)

        three_frame = LabelFrame(frame_admin, bg="#53CDB8")
        three_frame.grid(row=4, column=0)

        three_button_frame = LabelFrame(frame_admin, bg="#53CDB8")
        three_button_frame.grid(row=5, column=0)

        menubar = Menu(frame_admin)
        frame_admin.config(menu=menubar)

        filemenu = Menu(menubar, tearoff=0, bg="#FFBB20")
        filemenu.add_command(label="registro nuevo usuario", command=lambda: registro(),
                             font=("Helveltica", "9", "normal"))
        filemenu.add_command(label="User manual", font=("Helveltica", "9", "normal"))
        filemenu.add_separator()
        filemenu.add_command(label="Close", command=frame_admin.quit, font=("Helveltica", "9", "normal"))

        menubar.add_cascade(label="Menu", menu=filemenu)
        # --------------- INBOX WIDGETS ZONE ------------------
        Label(inbox_frame, text='Nombre usuario', bg="#53CDB8", font=("Comic Sans MS", "11", "normal")).grid(row=0,
                                                                                                             column=0)
        inbox_name = Entry(inbox_frame, font=("Comic Sans MS", "11", "normal"), width=28)
        inbox_name.grid(row=1, column=0)
        inbox_name.focus()

        Label(inbox_frame, text='identificacion usuario', bg="#53CDB8", font=("Comic Sans MS", "11", "normal")).grid(
            row=0, column=1)
        inbox_id = Entry(inbox_frame, font=("Comic Sans MS", "11", "normal"), width=20)
        inbox_id.grid(row=1, column=1)

        Label(inbox_frame, text='Nacionalidad', bg="#53CDB8", font=("Comic Sans MS", "11", "normal")).grid(row=0,
                                                                                                           column=2)
        inbox_nac = Entry(inbox_frame, font=("Comic Sans MS", "11", "normal"), width=30)
        inbox_nac.grid(row=1, column=2)

        Label(inbox_frame, text='Telfono usuario', bg="#53CDB8", font=("Comic Sans MS", "11", "normal")).grid(row=0,
                                                                                                              column=3)
        inbox_phone = Entry(inbox_frame, font=("Comic Sans MS", "11", "normal"), width=20)
        inbox_phone.grid(row=1, column=3)

        # --------------- BUTTON WIDGETS ZONE -----------------
        Add_contact_button = Button(button_frame, command=lambda: add(), text='Agregar al registro', width=20)
        Add_contact_button.configure(bg="#FFBB20", cursor='hand2', font=("Comic Sans MS", "10", "normal"))
        Add_contact_button.grid(row=0, column=0, padx=2, pady=3, sticky=W + E)

        search_button = Button(button_frame, command=lambda: search(), text='Buscar', width=20)
        search_button.configure(bg="#FFBB20", cursor='hand2', font=("Comic Sans MS", "10", "normal"))
        search_button.grid(row=0, column=1, padx=2, pady=3, sticky=W + E)

        delete_button = Button(button_frame, command=lambda: delete(), text='Borrar registro', width=20)
        delete_button.configure(bg="#F26262", cursor='hand2', font=("Comic Sans MS", "10", "normal"))
        delete_button.grid(row=1, column=0, padx=2, pady=3, sticky=W + E)

        modify_button = Button(button_frame, command=lambda: modify(), text='Modificar registro')
        modify_button.configure(bg="#FFBB20", cursor='hand2', font=("Comic Sans MS", "10", "normal"))
        modify_button.grid(row=1, column=1, padx=2, pady=3, sticky=W + E)

        show_contacts_button = Button(button_frame, command=lambda: show_contacts(), text='Mostrar registro',
                                      width=20)
        show_contacts_button.configure(bg="#FFBB20", cursor='hand2', font=("Comic Sans MS", "10", "normal"))
        show_contacts_button.grid(row=0, column=2, padx=2, pady=3, sticky=W + E)

        save_changes_button = Button(button_frame, command=lambda: clean(), text='limpiar', width=20)
        save_changes_button.configure(bg="#FFBB20", cursor='hand2', font=("Comic Sans MS", "10", "normal"))
        save_changes_button.grid(row=1, column=2, padx=2, pady=3, sticky=W + E)

        # Table for database
        frame_admin.tree = ttk.Treeview(three_frame, height=20, columns=("one", "two", "three"))
        frame_admin.tree.grid(padx=5, pady=5, row=0, column=0, columnspan=1)
        frame_admin.tree.heading("#0", text='Name', anchor=CENTER)
        frame_admin.tree.heading("one", text='Identificacion', anchor=CENTER)
        frame_admin.tree.heading("two", text='Nacionalidad', anchor=CENTER)
        frame_admin.tree.heading("three", text='Telefono', anchor=CENTER)

        # Scroll
        scrollVert = Scrollbar(three_frame, command=frame_admin.tree.yview)
        frame_admin.tree.configure(yscrollcommand=scrollVert.set)
        scrollVert.grid(row=0, column=1, sticky="nsew")

        scroll_x = Scrollbar(three_frame, command=frame_admin.tree.xview, orient=HORIZONTAL)
        frame_admin.tree.configure(xscrollcommand=scroll_x.set)
        scroll_x.grid(row=2, column=0, columnspan=1, sticky="nsew")

        # -------------- COMBOBOX WIDGETS ZONE ----------------
        Label(button_frame, text='Buscar/Modificar', bg="#53CDB8",
              font=("Comic Sans MS", "10", "normal")).grid(
            row=0, column=3, columnspan=3)

        combo = ttk.Combobox(button_frame, state='readonly', width=17, justify='center',
                             font=("Comic Sans MS", "10", "normal"))
        combo["values"] = ['Name', 'id']
        combo.grid(row=1, column=3, padx=15)
        combo.current(0)

        def write_user():
            MessageBox.showinfo("Registro usuario",
                                "Registre los datos para la creacion de el nuevo usuario")

        def _clean_inbox(dato1, dato2):
            dato1.delete(0, 'end')
            dato2.delete(0, 'end')

        def _save(user, password):
            s_name = user
            s_phone = password

        def registro():
            global frame_registro
            frame_registro = Toplevel(root)

            frame_registro.configure(bg="#27AEF2")
            frame_registro.title("Registro")
            frame_registro.geometry("+350+80")
            frame_registro.resizable(0, 0)

            inbox_frame = LabelFrame(frame_registro, bg="#53CDB8", width=300, height=80, padx=4, pady=5)
            inbox_frame.grid(row=0, column=0)

            button_frame = LabelFrame(frame_registro, bg="#53CDB8")
            button_frame.grid(row=3, column=0)

            global nombre_usuario
            global clave
            global entrada_nombre
            global entrada_clave
            nombre_usuario = StringVar()
            clave = StringVar()
            Label(inbox_frame, text="Introduzca datos", bg="#53CDB8", font=("Comic Sans MS", "20", "bold")).grid(
                row=1,
                column=0, padx=2, pady=3, sticky=W + E)

            Label(inbox_frame, text="Nombre de usuario ", bg="#53CDB8",
                  font=("Comic Sans MS", "11", "bold")).grid(row=2, column=0, padx=2, pady=3, sticky=W + E)
            entrada_nombre = Entry(inbox_frame, textvariable=nombre_usuario, font=("Comic Sans MS", "11", "normal"),
                                   width=50)
            entrada_nombre.grid(row=3, column=0, padx=30, pady=5)
            entrada_nombre.focus()

            Label(inbox_frame, text="Contraseña ", bg="#53CDB8",
                  font=("Comic Sans MS", "11", "bold")).grid(row=4, column=0, padx=2, pady=3, sticky=W + E)

            entrada_clave = Entry(inbox_frame, textvariable=clave,
                                  show='*', font=("Comic Sans MS", "11", "normal"),
                                  width=50)
            entrada_clave.grid(row=5, column=0, padx=30, pady=5)
            entrada_clave.focus()

            reg_button = Button(button_frame, text='Registrar', width=20, command=lambda: registro_user())
            reg_button.configure(bg="#FFBB20", cursor='hand2', font=("Comic Sans MS", "10", "normal"))
            reg_button.grid(row=6, column=0, padx=2, pady=3, sticky=W + E)

            def registro_user():
                frame_admin.destroy()
                usuario = entrada_nombre.get()
                clav = entrada_clave.get()

                contact_check = [usuario, clav]
                if contact_check == ['', '']:
                    write_user()
                else:
                    _save(usuario, clav)

                contact_check = []
                _clean_inbox(entrada_nombre, entrada_clave)

                Label(frame_registro, text="¡Registro completado con éxito!", fg="green", font=("calibri", 15)).grid(
                    row=11, column=0)

        def _clean_inbox_u():

            inbox_name.delete(0, 'end')
            inbox_phone.delete(0, 'end')
            inbox_id.delete(0, 'end')
            inbox_nac.delete(0, 'end')

        def _clean_treeview():
            tree_list = frame_admin.tree.get_children()
            for item in tree_list:
                frame_admin.tree.delete(item)

        def _view_csv():
            contacts = orden.alphabetic_order()
            for i, row in enumerate(contacts):
                name = str(row[0])
                ident = str(row[1])
                nacion = str(row[2])
                phone = str(row[3])
                frame_admin.tree.insert("", 0, text=name, values=(ident, nacion, phone))

        def _save_u(name, id, nac, phone):
            s_name = name
            s_Id = id
            s_nac = nac
            s_phone = phone
            with open('People_list.csv', 'a') as f:
                writer = csv.writer(f, lineterminator='\r', delimiter=',')
                writer.writerow((s_name, s_Id, s_nac, s_phone))

        def _search_u(var_inbox, possition):
            my_list = []
            s_var_inbox = str(var_inbox)
            var_possition = int(possition)
            with open('People_list.csv', 'r') as f:
                reader = csv.reader(f)
                for i, row in enumerate(reader):
                    if s_var_inbox == row[var_possition]:
                        my_list = [row[0], row[1], row[2], row[3]]
                        break
                    else:
                        continue
            return my_list

        def _check_u(answer, var_search):
            list_answer = answer
            var_search = var_search
            if list_answer == []:
                no_found(var_search)
            else:
                name = str(list_answer[0])
                id = str(list_answer[1])
                nac = str(list_answer[2])
                phone = str(list_answer[3])
                frame_admin.tree.insert("", 0, text="------------------------------",
                                        values=("------------------------------", "------------------------------",
                                                "------------------------------"))
                frame_admin.tree.insert("", 0, text=name, values=(id, nac, phone))

        def _check_1(answer, var_search):
            val_modify = answer
            var = var_search
            if val_modify == []:
                no_found(var)
            else:
                modificar.modificarRegistro(frame_admin, val_modify)

        # ----------------- BUTTON FUNCTIONS ------------------
        def add():
            name = inbox_name.get()
            id = inbox_id.get()
            nac = inbox_nac.get()
            phone = inbox_phone.get()
            contact_check = [name, id, nac, phone]
            if contact_check == ['', '', '', '']:
                write_user()
            else:
                if name == '':
                    name = '<Default>'
                if id == '':
                    id = '<Default>'
                if nac == '':
                    nac = '<Default>'
                if phone == '':
                    phone = '<Default>'
                _save_u(name, id, nac, phone)
                frame_admin.tree.insert("", 0, text="------------------------------",
                                        values=("------------------------------", "------------------------------",
                                                "------------------------------"))
                frame_admin.tree.insert("", 0, text=str(name), values=(str(id), str(nac), str(phone)))

            contact_check = []
            _clean_inbox_u()

        def search():
            answer = []
            var_search = str(combo.get())
            if var_search == 'Name':
                var_inbox = inbox_name.get()
                possition = 0
                answer = _search_u(var_inbox, possition)
                _check_u(answer, var_search)
            elif var_search == 'id':
                var_inbox = inbox_id.get()
                possition = 1
                answer = _search_u(var_inbox, possition)
                _check_u(answer, var_search)

            _clean_inbox_u()

        def modify():
            answer = []
            var_search = str(combo.get())
            if var_search == 'Name':
                var_inbox = inbox_name.get()
                possition = 0
                answer = _search_u(var_inbox, possition)
                _check_1(answer, var_search)
            elif var_search == 'id':
                var_inbox = inbox_id.get()
                possition = 1
                answer = _search_u(var_inbox, possition)
                _check_1(answer, var_search)

            _clean_inbox_u()

        def show_contacts():
            frame_admin.tree.insert("", 0, text="------------------------------",
                                    values=("------------------------------", "------------------------------",
                                            "------------------------------"))
            _view_csv()
            frame_admin.tree.insert("", 0, text="------------------------------",
                                    values=("------------------------------", "------------------------------",
                                            "------------------------------"))

        def delete():
            name = str(inbox_name.get())
            a = delete_mesageBox(name)
            if a == True:
                with open('People_list.csv', 'r') as f:
                    reader = list(csv.reader(f))
                with open('People_list.csv', 'w') as f:
                    writer = csv.writer(f, lineterminator='\r', delimiter=',')
                    for i, row in enumerate(reader):
                        if name != row[0]:
                            writer.writerow(row)
            clean()
            show_contacts()

        def clean():
            _clean_inbox_u()
            _clean_treeview()
