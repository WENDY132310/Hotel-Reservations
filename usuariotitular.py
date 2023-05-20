import csv
from tkinter import *
from tkinter import messagebox as MessageBox, ttk

import psycopg2 as psycopg2

import habitacion
import pago

import orden
import usuario


class user():
    global frame_user_titular

    def __init__(self, root):


        frame_user_titular = Toplevel(root)

        frame_user_titular.configure(bg="#27AEF2")
        frame_user_titular.title("Bievenido es un placer atenderte")
        frame_user_titular.geometry("+350+80")
        frame_user_titular.resizable(0, 0)


        Cantidadper= StringVar()
        Cantidadper = 1


        def no_found(var):
            var_s = str(var)
            MessageBox.showinfo("No se encuentra el registro ",
                                "Usuario " + var_s + ' ' + "Por favor Ingrese correctamente los datos")

        def write_user():
            MessageBox.showinfo("Registro usuario titular",
                                "Registre los datos de el  usuario")
            frame_user_titular.attributes('-topmost', True)

        # -------- Frame principal cliente---------
        inbox_frame = LabelFrame(frame_user_titular, bg="#53CDB8", width=300, height=80, padx=4, pady=5)
        inbox_frame.grid(row=0, column=0)

        button_frame = LabelFrame(frame_user_titular, bg="#53CDB8")
        button_frame.grid(row=3, column=0)

        # ------------------ MENU declaracion -----------------


        menubar = Menu(frame_user_titular)
        frame_user_titular.config(menu=menubar)

        filemenu = Menu(menubar, tearoff=0, bg="#FFBB20")
        filemenu.add_command(label="mostrar registro",
                             font=("Helveltica", "9", "normal"))
        filemenu.add_command(label="User manual", font=("Helveltica", "9", "normal"))
        filemenu.add_separator()
        filemenu.add_command(label="Close", command=frame_user_titular, font=("Helveltica", "9", "normal"))

        menubar.add_cascade(label="Menu", menu=filemenu)

        # ----------------------------Frame agregar --------------------------

        Label(inbox_frame, text='Bienvenido a el hotel Hospedaje Real ', bg="#53CDB8",
              font=("Comic Sans MS", "30", "bold")).grid(row=1,
                                                         column=0)
        Label(inbox_frame, text='Nombre', bg="#53CDB8", font=("Comic Sans MS", "11", "bold")).grid(row=2, column=0)
        inbox_user1 = Entry(inbox_frame, font=("Comic Sans MS", "11", "normal"), width=50)
        inbox_user1.grid(row=3, column=0, padx=30, pady=5)
        inbox_user1.focus()

        Label(inbox_frame, text='Identificacion', bg="#53CDB8", font=("Comic Sans MS", "11", "bold")).grid(row=4,
                                                                                                           column=0)
        inbox_id = Entry(inbox_frame, font=("Comic Sans MS", "11", "normal"), width=50)
        inbox_id.grid(row=5, column=0, padx=30, pady=5)
        inbox_id.focus()

        Label(inbox_frame, text='Nacionalidad', bg="#53CDB8", font=("Comic Sans MS", "11", "bold")).grid(row=6,
                                                                                                         column=0)
        inbox_from = Entry(inbox_frame, font=("Comic Sans MS", "11", "normal"), width=50)
        inbox_from.grid(row=7, column=0, padx=30, pady=5)
        inbox_from.focus()

        Label(inbox_frame,  text='telefono', bg="#53CDB8", font=("Comic Sans MS", "11", "bold")).grid(row=8, column=0)
        inbox_phone = Entry(inbox_frame, font=("Comic Sans MS", "11", "normal"), width=50)
        inbox_phone.grid(row=9, column=0, padx=30, pady=5)
        inbox_phone.focus()

        Add_person_button = Button(button_frame, command=lambda: add(), text='Agregar mas personas a la reserva',
                                   width=30)
        Add_person_button.configure(bg="#FFBB20", cursor='hand2', font=("Comic Sans MS", "10", "normal"))
        Add_person_button.grid(row=0, column=0, padx=2, pady=3, sticky=W + E)

        continuar_button = Button(button_frame, command=lambda: continuar(), text='continuar', width=30)
        continuar_button.configure(bg="#FFBB20", cursor='hand2', font=("Comic Sans MS", "10", "normal"))
        continuar_button.grid(row=0, column=1, padx=2, pady=3, sticky=W + E)

        # --------------- TREE TABLE ZONE -----------------

        def _clean_inbox():
            # Delete from first position (0) to the last position ('end')
            inbox_user1.delete(0, 'end')
            inbox_phone.delete(0, 'end')
            inbox_id.delete(0, 'end')
            inbox_from.delete(0, 'end')

        def _clean_treeview():
            tree_list = frame_user_titular.tree.get_children()
            for item in tree_list:
                frame_user_titular.tree.delete(item)

        def _view_csv():
            contacts = orden.alphabetic_order()
            for i, row in enumerate(contacts):
                name = str(row[0])
                id = str(row[1])
                nacion = str(row[2])
                phone = str(row[3])
                frame_user_titular.tree.insert("", 0, text=name, values=(id, nacion, phone))

        def _save(name, id, nacion, phone):
            s_name = name
            s_id = id
            s_nacion = nacion
            s_phone = phone

            with open('People_list.csv', 'a') as f:
                writer = csv.writer(f, lineterminator='\r', delimiter=',')
                writer.writerow((s_name, s_id, s_nacion, s_phone))

        def _search(var_inbox, possition):
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

        def _check(answer, var_search):
            list_answer = answer
            var_search = var_search
            if list_answer == []:
                no_found(var_search)
            else:
                name = str(list_answer[0])
                id = str(list_answer[1])
                nacion = str(list_answer[2])
                phone = str(list_answer[3])
                frame_user_titular.tree.insert("", 0, text="------------------------------",
                                               values=(
                                                   "------------------------------", "------------------------------"))
                frame_user_titular.tree.insert("", 0, text=name, values=(id, nacion, phone))
                frame_user_titular.tree.insert("", 0, text="Search result of name",
                                               values=("Search result of phone", "Search result of email"))
                frame_user_titular.tree.insert("", 0, text="------------------------------",
                                               values=(
                                                   "------------------------------", "------------------------------"))

        def _check_1(answer, var_search):
            val_modify = answer
            var = var_search
            if not val_modify:
                no_found(var)

        # else:
        #    TopLevelModify(frame_user_titular, val_modify)

        Cantidad = IntVar()

        def continuar():
            if inbox_user1.get() == "" or inbox_id.get() == "" or inbox_from.get() == "" or inbox_phone.get() == "":
                write_user()
            else:

                name = inbox_user1.get()
                id = inbox_id.get()
                nacion = inbox_from.get()
                phone = inbox_phone.get()
                contact_check = [name, id, nacion, phone]
                if contact_check == ['', '', '', '']:
                    write_user()
                else:
                    if name == '':
                        name = '<Default>'
                    if id == '':
                        id = '<Default>'
                    if nacion == '':
                        nacion = '<Default>'
                    if phone == '':
                        phone = '<Default>'
                    _save(name, id, nacion, phone)

                    contact_check = []


                    conn = conexion()
                    cursor = conn.cursor()
                    cursor2 = conn.cursor()
                    query = '''INSERT INTO huesped (id_huesped,nombre,nacionalidad) VALUES (%s,%s,%s)'''
                    cursor.execute(query, (id, name, nacion))
                    query2 = '''INSERT INTO telefonos_huesped (id_huesped,telefonos) VALUES (%s,%s)'''
                    cursor2.execute(query2, (id, phone))
                    print("Data save")
                    conn.commit()
                    conn.close()
                    habitacion.habitacion(root,Cantidadper)
                    frame_user_titular.destroy()
        def add():
            if inbox_user1.get() == "" or inbox_id.get() == "" or inbox_from.get() == "" or inbox_phone.get() == "":
                write_user()

            else:
                name = inbox_user1.get()
                id = inbox_id.get()
                nacion = inbox_from.get()
                phone = inbox_phone.get()
                contact_check = [name, id, nacion, phone]
                if contact_check == ['', '', '', '']:
                    write_user()
                else:
                    if name == '':
                        name = '<Default>'
                    if id == '':
                        id = '<Default>'
                    if nacion == '':
                        nacion = '<Default>'
                    if phone == '':
                        phone = '<Default>'
                    _save(name, id, nacion, phone)

                    contact_check = []
                    usuario.user(root)
                    _clean_inbox()
                    conn = conexion()
                    cursor = conn.cursor()
                    cursor2 = conn.cursor()
                    query = '''INSERT INTO huesped (id_huesped,nombre,nacionalidad) VALUES (%s,%s,%s)'''
                    cursor.execute(query, (id, name, nacion))
                    query2 = '''INSERT INTO telefonos_huesped (id_huesped,telefonos) VALUES (%s,%s)'''
                    cursor2.execute(query2, (id, phone))
                    print("Data save")
                    conn.commit()
                    conn.close()

        def conexion():
            try:
                conn = psycopg2.connect(dbname="proyecto_finalbd",
                                        user="postgres",
                                        password="basesdedatos",
                                        host="localhost",
                                        port="5432",
                                        )

                print("Conexion exitosa")
                return conn
            except Exception as ex:
                print(ex)
