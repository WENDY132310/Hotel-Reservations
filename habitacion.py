import tkinter
from idlelib.debugger import Idb
from tkinter import *
from tkinter import ttk, messagebox
from tkinter import messagebox as MessageBox, ttk
import pago
import tkinter as tk
from datetime import date
import psycopg2 as psycopg2

from datetime import datetime


class habitacion():
    global frame_habitacion
    def __init__(self, root,personas):
        dia = IntVar()
        mes = IntVar()
        year = IntVar()
        dias = IntVar()
        mess = IntVar()
        years = IntVar()
        valor= IntVar()
        servicio = IntVar()
        print(personas)

        frame_habitacion = Toplevel(root)

        frame_habitacion.configure(bg="#27AEF2")
        frame_habitacion.title("Selecciona tu habitacion")
        frame_habitacion.geometry("+350+80")
        frame_habitacion.resizable(0, 0)

        def write_user():

            MessageBox.showinfo("Registro habitacion",
                                "Registre los datos para la correcta seleccion de su habitacion")
            frame_habitacion.attributes('-topmost', True)

        inbox_frame = LabelFrame(frame_habitacion, bg="#53CDB8", width=300, height=80, padx=4, pady=5)
        inbox_frame.grid(row=1, column=0)
        inbox_ = LabelFrame(frame_habitacion, bg="#53CDB8", width=300, height=80, padx=4, pady=5)
        inbox_.grid(row=2, column=0)

        button_frame = LabelFrame(frame_habitacion, bg="#53CDB8")
        button_frame.grid(row=3, column=0)
        Label(inbox_frame, text='Elige tu habitacion', bg="#53CDB8", font=("Comic Sans MS", "30", "bold")).grid(row=0,
                                                                                                                column=0)
        Label(inbox_, text='Tipo', bg="#53CDB8", font=("Comic Sans MS", "11", "bold")).grid(row=1,
                                                                                            column=0, padx=30)

        combobox = ttk.Combobox(inbox_, state='readonly', width=17, justify='center',
                                font=("Comic Sans MS", "10", "normal"))
        combobox["values"] = ['', 'Sencilla', 'Doble', 'Matrimonial', 'suite']
        combobox.grid(row=1, column=1, padx=15)
        combobox.current(0)

        Label(inbox_, text='Sede Hotel', bg="#53CDB8", font=("Comic Sans MS", "11", "bold")).grid(row=2,
                                                                                                  column=0, padx=30)

        combobox_ = ttk.Combobox(inbox_, state='readonly', width=17, justify='center',
                                 font=("Comic Sans MS", "10", "normal"))
        combobox_["values"] = ['', 'Sheraton', 'Urban', 'Tequendama']
        combobox_.grid(row=2, column=1, padx=15)
        combobox_.current(0)

        Label(inbox_, text='Fecha llegada ', bg="#53CDB8", font=("Comic Sans MS", "11", "bold")).grid(row=3, column=0,
                                                                                                      padx=30)

        Label(inbox_, text='Dia ', bg="#53CDB8", font=("Comic Sans MS", "11", "bold")).grid(row=3, column=1,
                                                                                            padx=30, pady=5)

        inbox_diaent = Entry(inbox_, textvariable=dia, font=("Comic Sans MS", "11", "normal"), width=10,show="")
        inbox_diaent.grid(row=4, column=1, padx=30, pady=5)
        inbox_diaent.focus()
        Label(inbox_, text='Mes ', bg="#53CDB8", font=("Comic Sans MS", "11", "bold")).grid(row=3, column=2,
                                                                                            padx=30, pady=5)

        inbox_mesent = Entry(inbox_, textvariable=mes, font=("Comic Sans MS", "11", "normal"), width=10,)
        inbox_mesent.grid(row=4, column=2, padx=30, pady=5)
        inbox_mesent.focus()
        Label(inbox_, text='Año ', bg="#53CDB8", font=("Comic Sans MS", "11", "bold")).grid(row=3, column=3,
                                                                                            padx=30)
        inbox_yearent = Entry(inbox_, textvariable=year, font=("Comic Sans MS", "11", "normal"), width=10,show="")
        inbox_yearent.grid(row=4, column=3, padx=30, pady=5)
        inbox_yearent.focus()

        Label(inbox_, text='Fecha salida ', bg="#53CDB8", font=("Comic Sans MS", "11", "bold")).grid(row=5, column=0,
                                                                                                     padx=30)

        Label(inbox_, text='Dia ', bg="#53CDB8", font=("Comic Sans MS", "11", "bold")).grid(row=5, column=1,
                                                                                            padx=30, pady=5)

        inbox_diaSal = Entry(inbox_, textvariable=dias, font=("Comic Sans MS", "11", "normal"), width=10,show="")
        inbox_diaSal.grid(row=7, column=1, padx=30, pady=5)
        inbox_diaSal.focus()
        Label(inbox_, text='Mes ', bg="#53CDB8", font=("Comic Sans MS", "11", "bold")).grid(row=5, column=2,
                                                                                            padx=30, pady=5)

        inbox_mesSal = Entry(inbox_, textvariable=mess, font=("Comic Sans MS", "11", "normal"), width=10,show="")
        inbox_mesSal.grid(row=7, column=2, padx=30, pady=5)
        inbox_mesSal.focus()
        Label(inbox_, text='Año ', bg="#53CDB8", font=("Comic Sans MS", "11", "bold")).grid(row=5, column=3,
                                                                                            padx=30)
        inbox_yearSal = Entry(inbox_, textvariable=years, font=("Comic Sans MS", "11", "normal"), width=10,show="")
        inbox_yearSal.grid(row=7, column=3, padx=30, pady=5)
        inbox_yearSal.focus()

        Label(inbox_, text='Servicios adicionales ', bg="#53CDB8", font=("Comic Sans MS", "11", "bold")).grid(row=10,
                                                                                                              column=0,
                                                                                                              padx=30)

        comboboxS = ttk.Combobox(inbox_, state='readonly', width=17, justify='center',
                                 font=("Comic Sans MS", "10", "normal"))
        comboboxS["values"] = ['', 'SPA', 'Reserva en restaurantes', 'Alquier de carros']
        comboboxS.grid(row=10, column=1, padx=15)
        comboboxS.current(0)

        inbox_servicio = Entry(inbox_, textvariable=servicio, font=("Comic Sans MS", "11", "normal"), width=10)
        inbox_servicio.grid(row=10, column=2, padx=30, pady=5)
        inbox_servicio.focus()

        inbox_servicioHab = Entry(inbox_,textvariable=valor, font=("Comic Sans MS", "11", "normal"), width=10)
        inbox_servicioHab.grid(row=1, column=2, padx=30, pady=5)
        inbox_servicioHab.focus()
        Label(inbox_, text='Total de dias:  ', bg="#53CDB8", font=("Comic Sans MS", "11", "bold")).grid(row=8,
                                                                                                              column=1,
                                                                                                              padx=30)
        inbox_diases = Entry(inbox_, font=("Comic Sans MS", "11", "normal"), width=10)
        inbox_diases.grid(row=8, column=2, padx=30, pady=5)
        inbox_diases.focus()

        pagarSer_button = Button(inbox_, text='Confirmar servicio', width=30, command=lambda: valorservicio())
        pagarSer_button.configure(bg="#FFBB20", cursor='hand2', font=("Comic Sans MS", "10", "normal"))
        pagarSer_button.grid(row=10, column=3, padx=2, pady=3, sticky=W + E)

        hab_button = Button(inbox_, text='Confirmar tipo de habitacion', width=30, command=lambda: valorserviciohab())
        hab_button.configure(bg="#FFBB20", cursor='hand2', font=("Comic Sans MS", "10", "normal"))
        hab_button.grid(row=1, column=3, padx=2, pady=3, sticky=W + E)

        pagar_button = Button(button_frame, command=lambda: sel(), text='Pagar', width=30)
        pagar_button.configure(bg="#FFBB20", cursor='hand2', font=("Comic Sans MS", "10", "normal"))
        pagar_button.grid(row=0, column=1, padx=2, pady=3, sticky=W + E)

        def valorserviciohab():

            _clean_inbox(inbox_servicioHab)
            valor = StringVar()

            if combobox.get() == "Sencilla":
                valor = "90.000"
                inbox_servicioHab.insert(tk.END, valor)

            elif combobox.get() == "Doble":
                valor = "150.000"
                inbox_servicioHab.insert(tk.END, valor)

            elif combobox.get() == "Matrimonial":
                valor = "170.000"
                inbox_servicioHab.insert(tk.END, valor)
            elif combobox.get() == "suite":
                valor = "250.000"
                inbox_servicioHab.insert(tk.END, valor)


        def valorservicio():

            _clean_inbox(inbox_servicio)
            valor =StringVar()
            if comboboxS.get() == "SPA":
                valor= "50.000"
                inbox_servicio.insert(tk.END, valor)

            elif comboboxS.get() == "Reserva en restaurantes":
                valor = "30.000"
                inbox_servicio.insert(tk.END, valor)

            elif comboboxS.get() == "Alquier de carros":
                valor = "120.000"
                inbox_servicio.insert(tk.END, valor)
            elif comboboxS.get() == "":
                valor = "0"
                inbox_servicio.insert(tk.END, valor)


        def _clean_inbox(dato1):
            dato1.delete(0, 'end')

        fechaent = date
        def sel():
            seleccion = str(combobox.get())
            seleccion1 = str(combobox_.get())
            seleccion2 = str(comboboxS.get())

            if seleccion == "" or seleccion1 == "":
                write_user()
            else:
                print(seleccion)
                print(seleccion1)
                print(seleccion2)

                entrada=fechaen()
                fechaent=entrada

                salida=fechasal()
                diasestadia1=diferencia(entrada,salida)
                inbox_diases.insert(tk.END, str(diasestadia1))
                continuar()

        def fechaen():

            new_date = date(year.get(), mes.get(), dia.get())
            entrada = new_date.strftime('%d/%m/%Y')
            print (entrada)

            return new_date

        def fechasal():

            new_date = date(years.get(), mess.get(), dias.get())
            salida = new_date.strftime('%d/%m/%Y')
            print (salida)
            return new_date

        def diferencia(ent,sal):

            _clean_inbox(inbox_diases)
            diferenciaf=(sal-ent).days
            diasestadia1=diferenciaf

            return (diasestadia1)






        def continuar():
            pago.pagar(root, inbox_servicioHab.get(), inbox_servicio.get(), inbox_diases.get())
            frame_habitacion.destroy()


        def tipo_hab():

            sede=combobox_.get()
            servicios = comboboxS.get()
            opcion = combobox.get()
            conn = conexionU()
            cursor = conn.cursor()
            query = "SELECT id_tipo FROM Tipo_habitacion WHERE tipo_habitacion= %s"
            cursor.execute(query, (opcion,))
            for fila in cursor:
                print(fila)
            conn.commit()
            conn.close()

            conn = conexionU()
            cursor = conn.cursor()
            query = '''INSERT INTO Habitacion (Servicios_adicionales,Id_tipo) VALUES (%s,%s)'''
            cursor.execute(query, (servicios, fila))
            print("DATA SAVE")
            conn.commit()
            conn.close()

            conn2= conexionU()
            cursor2=conn2.cursor()
            query2= "SELECT nombre_sede FROM nombre_sede= %s"
            cursor.execute(query2,(sede,))
            for filaS in cursor2:
                print (filaS)
            conn.commit()
            conn.close()
            sel()
            continuar()


        def conexionU():
            try:
                conn = psycopg2.connect(dbname="proyecto_finalbd",
                                        user="postgres",
                                        password="basesdedatos",
                                        host="localhost",
                                        port="5432",
                                        )

                print("Conexion exitosa hab")
                return conn
            except Exception as ex:
                print(ex)

