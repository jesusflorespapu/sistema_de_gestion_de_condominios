from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox

class UDI:
    def __init__(self, root):
        self.root = root
        self.root.title("SISTEMA DE GESTION DE CONDOMINIOS")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root, text="SISTEMA DE GESTION DE CONDOMINIOS", bd=10, relief=GROOVE, font=("times new roman", 40, "bold"), bg="darkred", fg="white")
        title.pack(side=TOP, fill=X)


        #==================LAS VARIABLES===========================
        self.condominios_no = StringVar()
        self.residentes_no = StringVar()
        self.valor_no = StringVar()
        self.deuda_no = StringVar()
        self.infraccion_no = StringVar()
        self.desalojo_no = StringVar()
        self.motivo_no = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        #================MANAGE FRAME======================
        Manage_frame = Frame(self.root, bd=4, relief=RIDGE, bg="light blue")
        Manage_frame.place(x=20, y=100, width=450, height=600)

        m_title = Label(Manage_frame, text="CONDOMINIOS", bg="light blue", 
                        fg="black", font=("times new roman", 30, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)




        lbl_condominio = Label(Manage_frame, text="Condominio", bg="light blue", 
                               fg="black", font=("times new roman", 20, "bold"))
        lbl_condominio.grid(row=1, column=0, pady=10, padx=20, sticky='w')


        txt_condominio = Entry(Manage_frame, textvariable=self.condominios_no, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_condominio.grid(row=1, column=1, pady=10, padx=20, sticky='w')

        lbl_residente = Label(Manage_frame, text="residente", bg="light blue", 
                              fg="black", font=("times new roman", 20, "bold"))
        lbl_residente.grid(row=2, column=0, pady=10, padx=20, sticky='w')


        txt_residente = Entry(Manage_frame, textvariable=self.residentes_no, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_residente.grid(row=2, column=1, pady=10, padx=20, sticky='w')


        lbl_valor = Label(Manage_frame, text="valor", bg="light blue", 
                          fg="black", font=("times new roman", 20, "bold"))
        lbl_valor.grid(row=3, column=0, pady=10, padx=20, sticky='w')


        txt_valor = Entry(Manage_frame, textvariable=self.valor_no, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_valor.grid(row=3, column=1, pady=10, padx=20, sticky='w')

        lbl_deuda = Label(Manage_frame, text="deuda", bg="light blue", 
                          fg="black", font=("times new roman", 20, "bold"))
        lbl_deuda.grid(row=4, column=0, pady=10, padx=20, sticky='w')


        txt_deuda = Entry(Manage_frame, textvariable=self.deuda_no, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_deuda.grid(row=4, column=1, pady=10, padx=20, sticky='w')

        lbl_infraccion = Label(Manage_frame, text="infraccion", bg="light blue", 
                          fg="black", font=("times new roman", 20, "bold"))
        lbl_infraccion.grid(row=5, column=0, pady=10, padx=20, sticky='w')

        combo_infraccion = ttk.Combobox(Manage_frame, textvariable=self.infraccion_no, font=("times new roman", 13, "bold"), state='readonly')
        combo_infraccion['values'] =("Aprobada", "Denegada")
        combo_infraccion.grid(row=5, column=1, pady=10, padx=20, sticky='w')

        lbl_desalojo = Label(Manage_frame, text="desalojo", bg="light blue", 
                          fg="black", font=("times new roman", 20, "bold"))
        lbl_desalojo.grid(row=6, column=0, pady=10, padx=20, sticky='w')

        combo_desalojo = ttk.Combobox(Manage_frame, textvariable=self.desalojo_no, font=("times new roman", 13, "bold"), state='readonly')
        combo_desalojo['values'] =("Si", "No")
        combo_desalojo.grid(row=6, column=1, pady=10, padx=20, sticky='w')

        lbl_motivo = Label(Manage_frame, text="motivo", bg="light blue", 
                          fg="black", font=("times new roman", 20, "bold"))
        lbl_motivo.grid(row=7, column=0, pady=10, padx=20, sticky='w')

        combo_motivo = ttk.Combobox(Manage_frame, textvariable=self.motivo_no, font=("times new roman", 13, "bold"), state='readonly')
        combo_motivo['values'] =("Deudor", "incumplimiento de normas", "destruccion de propiedad privada")
        combo_motivo.grid(row=7, column=1, pady=10, padx=20, sticky='w')


        #================BUTTON FRAME===============

        btn_frame = Frame(Manage_frame, bd=4, relief=RIDGE, bg="orange")
        btn_frame.place(x=10, y=520, width=425)


        Addbtn = Button(btn_frame, text="Registrar", width=10, 
                        command=self.add_condominio).grid(row=0, column=0, padx=10, pady=20)
        updatebtn = Button(btn_frame, text="Modificar", width=10, 
                           command=self.update_data).grid(row=0, column=1, padx=10, pady=20)
        deletebtn = Button(btn_frame, text="Eliminar", width=10, 
                           command=self.delete_data).grid(row=0, column=2, padx=10, pady=20)
        clearbtn = Button(btn_frame, text="Limpiar", width=10, 
                          command=self.clear).grid(row=0, column=3, padx=10, pady=20)
        
        #===========DETAIL FRAME=============
        Detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg="orange")
        Detail_frame.place(x=500, y=100, width=820, height=600)


        lbl_search = Label(Detail_frame, text="BUSCAR", bg="orange", fg="black", font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky='w')

        combo_search = ttk.Combobox(Detail_frame, textvariable=self.search_by, width=10, font=("times new roman", 13, "bold"), state='readonly')
        combo_search['values'] =("condominio", "residente", "valor", )
        combo_search.grid(row=0, column=1, pady=10, padx=20, sticky='w')

        txt_search = Entry(Detail_frame, textvariable=self.search_txt, width=15, font=("times new roman", 10, "bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky='w')


        searchbtn = Button(Detail_frame, text="Buscar", width=10, pady=5, command=self.search_data).grid(
            row=0, column=3, padx=10, pady=20)
        showallbtn = Button(Detail_frame, text="consulta", width=10, 
                            pady=5, command=self.fetch_data).grid(row=0, column=4, padx=10, pady=20)
        



        #==================TABLE FRAME==========================
        Table_frame = Frame(Detail_frame, bd=4, relief=RIDGE, bg="light blue")
        Table_frame.place(x=10, y=70, width=760, height=500)

        scroll_x = Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_frame, orient=VERTICAL)
        self.condominios_table = ttk.Treeview(Table_frame, column=("condominio_no", "residente", "valor", "deuda", "infraccion", "desalojo", "motivo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.condominios_table.xview)
        scroll_y.config(command=self.condominios_table.yview)
        self.condominios_table.heading("condominio_no", text="condominio_no")
        self.condominios_table.heading("residente", text="residente")
        self.condominios_table.heading("valor", text="valor")
        self.condominios_table.heading("deuda", text="deuda")
        self.condominios_table.heading("infraccion", text="infraccion")
        self.condominios_table.heading("desalojo", text="desalojo")
        self.condominios_table.heading("motivo", text="motivo")

        self.condominios_table['show'] = 'headings'
        self.condominios_table.column('condominio_no', width=100)
        self.condominios_table.column('residente', width=100)
        self.condominios_table.column('valor', width=100)
        self.condominios_table.column('deuda', width=100)
        self.condominios_table.column('infraccion', width=100)
        self.condominios_table.column('desalojo', width=100)
        self.condominios_table.column('motivo', width=100)

        self.condominios_table.pack(fill=BOTH, expand=1)
        self.condominios_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()


    def add_condominio(self):
        if self.condominios_no.get() == "" or self.residentes_no.get() == "" or self.valor_no.get() == "" or self.deuda_no.get() == "" or self.infraccion_no.get() == "" or self.desalojo_no.get() == "" or self.motivo_no.get() == "":
            messagebox.showinfo("Error", "Todos los campos requeridos")

        else:

            con = pymysql.connect(
                host="localhost",user="root",password="",database="gestiones")
            cur = con.cursor()
            cur.execute("insert curso values (%s,%s,%s,%s,%s,%s,%s)", (self.condominios_no.get(),
                                                                       self.residentes_no.get(),
                                                                       self.valor_no.get(),
                                                                       self.deuda_no.get(),
                                                                       self.infraccion_no.get(),
                                                                       self.desalojo_no.get(),
                                                                       self.motivo_no.get(),
                                                                       
                                                                       ))
            

            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Exito", "Los datos han sido registrados")


    def fetch_data(self):
        con = pymysql.connect(
                host="localhost",user="root",password="",database="gestiones")
        cur = con.cursor()
        cur.execute("select * from curso")
        rows = cur.fetchall()
        if len(rows) !=0:
            self.condominios_table.delete(*self.condominios_table.get_children())
            for row in rows:
                self.condominios_table.insert('', END, values=row)
            con.commit()
        con.close()


    def clear(self):
        self.condominios_no.set(""),
        self.residentes_no.set(""),
        self.valor_no.set(""),
        self.deuda_no.set(""),
        self.infraccion_no.set(""),
        self.desalojo_no.set(""),
        self.motivo_no.set(""),


    def get_cursor(self, ev):
        cursor_row = self.condominios_table.focus()
        contents = self.condominios_table.item(cursor_row)
        row = contents['values']
        self.condominios_no.set(row[0]),
        self.residentes_no.set(row[1]),
        self.valor_no.set(row[2]),
        self.deuda_no.set(row[3]),
        self.infraccion_no.set(row[4]),
        self.desalojo_no.set(row[5]),
        self.motivo_no.set(row[6]),



    def update_data(self):
        con = pymysql.connect(
            host="localhost",user="root",password="",database="gestiones")
        cur = con.cursor()
        cur.execute("update curso set residente=%s, valor=%s, deuda=%s, infraccion=%s, desalojo=%s, motivo=%s where condominios_no=%s", (
        self.residentes_no.get(),
        self.valor_no.get(),
        self.deuda_no.get(),
        self.infraccion_no.get(),
        self.desalojo_no.get(),
        self.motivo_no.get(),
        self.condominios_no.get()
                            ))

        con.commit()
        self.fetch_data()
        self.clear()
        con.close()


    def delete_data(self):
        con = pymysql.connect(
            host="localhost",user="root",password="",database="gestiones")
        cur = con.cursor()
        cur.execute("delete from curso where residente=%s",
                    self.residentes_no.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()


    def search_data(self):
        con = pymysql.connect(
            host="localhost",user="root",password="",database="gestiones")
        cur = con.cursor()
        cur.execute("select * from curso where " +str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+ "%'")

        rows = cur.fetchall()
        if len(rows) !=0:
            self.condominios_table.delete(*self.condominios_table.get_children())
            for row in rows:
                self.condominios_table.insert('', END, values=row)
                con.commit()
                con.close()




root = Tk()
ob = UDI(root)
root.mainloop()