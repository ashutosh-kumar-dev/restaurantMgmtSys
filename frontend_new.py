
from tkinter import *
from backend_new import  Database
import time

database = Database("restaurant.db")

class Window(object):
    def __init__(self,window):
        self.window = window
        self.window.wm_title("Shoping Mall Rent Details")
        self.window.geometry ('1350x750+0+0')
        self.window.config(bg ='powder blue' )

        self.frame= Frame(self.window, bg='powder blue')
        self.frame.pack(side=TOP)

        self.lblTitle = Label(self.frame,text="Restaurant management System",
                              font=("Magneto bold",45,"bold"),bg="powder blue",
                              fg="blue")
        self.lblTitle.grid(row=0,column=0,columnspan=1,pady=20)


        localtime=time.asctime(time.localtime(time.time()))
        lblInfo=Label(self.frame,font=('arial',20,'bold'),text=localtime,
                      fg="Steel Blue",bd=10,anchor='w',bg="powder blue")
        lblInfo.grid(row=1,column=0,pady=1)

        #======================================
        self.Frame1=Frame(self.window,width=1350,height=700,relief=RIDGE,
                          bg="cadet blue",bd=20)
        
        self.Frame1.pack(side=LEFT,padx=40)

        self.Frame2=Frame(self.window,width=1350,height=600,relief=RIDGE,
                          bg="powder blue",bd=20)
        
        self.Frame2.pack(side=RIGHT)
        #======================================

		#label names 
        l1 = Label(self.Frame1, text="idli", font=('arial', 16, 'bold'),
                   bg="cadet blue",fg="cornsilk")
        l1.grid(row=2, column=0,pady=10)

        l2 = Label(self.Frame1, text="dosa", font=('arial', 16, 'bold'),
                   bg="cadet blue",fg="cornsilk")
        l2.grid(row=3, column=0,pady=10)

        l3 = Label(self.Frame1, text="cold drink ", font=('arial', 16, 'bold'),
                   bg="cadet blue",fg="cornsilk")
        l3.grid(row=4, column=0,pady=10)

        l4 = Label(self.Frame1, text="burger", font=('arial', 16, 'bold'),
                   bg="cadet blue",fg="cornsilk")
        l4.grid(row=5, column=0,pady=10)
        
        l5 = Label(self.Frame1, text="net Amount", font=('arial', 16, 'bold'),
                   bg="cadet blue",fg="cornsilk")
        l5.grid(row=8, column=2,pady=10)
        
        l6 = Label(self.Frame1, text="reference id", font=('arial', 16, 'bold'),
                   bg="cadet blue",fg="cornsilk")
        l6.grid(row=1, column=0,pady=10)
        
        l7 = Label(self.Frame1, text="service charge", font=('arial', 16, 'bold'),
                   bg="cadet blue",fg="cornsilk")
        l7.grid(row=5, column=2,pady=10)
        
        l8 = Label(self.Frame1, text="GST", font=('arial', 16, 'bold'),bg="cadet blue",
                   fg="cornsilk")
        l8.grid(row=4, column=2,pady=10)

        l9 = Label(self.Frame1, text="french fries", font=('arial', 16, 'bold'),
                   bg="cadet blue",fg="cornsilk")
        l9.grid(row=1, column=2,pady=10)

        t = Label(self.Frame1, text="pizza", font=('arial', 16, 'bold'),bg="cadet blue",
                  fg="cornsilk")
        t.grid(row=3, column=2,pady=1)

        a = Label(self.Frame1, text="pasta", font=('arial', 16, 'bold'),
                  bg="cadet blue",fg="cornsilk")
        a.grid(row=2, column=2,pady=10)

        b = Label(self.Frame1, text="GEMINI", font=('algerian', 20, 'bold'),
                  bg="cadet blue",fg="cornsilk")
        b.grid(row=8, column=0,pady=10)

        c = Label(self.frame, text="Order List", font=('algerian', 20, 'bold'),
                  bg="cadet blue",fg="cornsilk")
        c.grid(row=3, column=2,padx=20)

		#label textbox
    

        self.reference = StringVar()
        self.e1 = Entry(self.Frame1, textvariable=self.reference,font=('arial',8,'bold'),
                        bd=10,insertwidth=4,bg="powder blue",justify='right')
        self.e1.grid(row=1, column=1,padx=20)

        self.net_amount = StringVar()
        self.e2 = Entry(self.Frame1, font=('arial',10,'bold'),textvariable=self.net_amount,
                        bd=10,insertwidth=4,bg="powder blue",justify='right')
        self.e2.grid(row=8, column=3,padx=20)

        self.service_charge = StringVar()
        self.e3 = Entry(self.Frame1, textvariable=self.service_charge,font=('arial',8,'bold'),
                        bd=10,insertwidth=4,bg="powder blue",justify='right')
        self.e3.grid(row=5, column=3,padx=20)

        self.idli = StringVar()
        self.e4= Entry(self.Frame1, textvariable=self.idli,font=('arial',8,'bold'),bd=10,
                       insertwidth=4,bg="powder blue",justify='right')
        self.e4.grid(row=2, column=1,padx=20)
        
        self.dosa = StringVar()
        self.e5= Entry(self.Frame1, textvariable=self.dosa,font=('arial',8,'bold'),bd=10,
                       insertwidth=4,bg="powder blue",justify='right')
        self.e5.grid(row=3, column=1,padx=20)

        self.cold_drink  = StringVar()
        self.e6= Entry(self.Frame1, textvariable=self.cold_drink ,font=('arial',8,'bold'),
                       bd=10,insertwidth=4,bg="powder blue",justify='right')
        self.e6.grid(row=4, column=1,padx=20)

        self.burger = StringVar()
        self.e7= Entry(self.Frame1, textvariable=self.burger,font=('arial',8,'bold'),bd=10,
                       insertwidth=4,bg="powder blue",justify='right')
        self.e7.grid(row=5, column=1,padx=20)
        
        self.french_fries = StringVar()
        self.e8= Entry(self.Frame1, textvariable=self.french_fries,font=('arial',8,'bold'),
                       bd=10,insertwidth=4,bg="powder blue",justify='right')
        self.e8.grid(row=1, column=3,padx=20)

        self.tax = StringVar()
        self.e9= Entry(self.Frame1, textvariable=self.tax,font=('arial',8,'bold'),bd=10,
                       insertwidth=4,bg="powder blue",justify='right')
        self.e9.grid(row=4, column=3,padx=20)

        self.pizza = StringVar()
        self.e10= Entry(self.Frame1, textvariable=self.pizza,font=('arial',8,'bold'),bd=10,
                        insertwidth=4,bg="powder blue",justify='right')
        self.e10.grid(row=3, column=3,padx=20)
        
        self.pasta = StringVar()
        self.e11= Entry(self.Frame1, textvariable=self.pasta,font=('arial',8,'bold'),bd=10,
                        insertwidth=4,bg="powder blue",justify='right')
        self.e11.grid(row=2, column=3,padx=20)

        self.list1 = Listbox(self.Frame2, height=20, width=50,font=('arial',10,'bold'),bg="powder blue")
        self.list1.grid(row=0, column=0, rowspan=4, columnspan=2)

        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        #  scrollbar 
        #sb1 = Scrollbar(self.Frame2)
        #sb1.grid(row=2, column=2, rowspan=16)
        #self.list1.config(yscrollcommand=sb1.set)
        #sb1.config(command=self.list1.yview)
		#button code 
        b1 = Button(self.Frame1, text="View all", width=14,
                    command=self.view_command)
        b1.grid(row=1, column=4)

        b2 = Button(self.Frame1, text="Search entry", width=14,
                    command=self.search_command)
        b2.grid(row=2, column=4)

        b3 = Button(self.Frame1, text="Add New entry", width=14,
                    command=self.add_command)
        b3.grid(row=3, column=4)

        b4 = Button(self.Frame1, text="Update selected", width=14,
                    command=self.update_command)
        b4.grid(row=4, column=4)

        b5 = Button(self.Frame1, text="Delete selected", width=14,
                    command=self.delete_command)
        b5.grid(row=5, column=4)

        b6 = Button(self.Frame1, text="Close", width=14, command=window.destroy)
        b6.grid(row=8, column=4,pady=10)

        b7 = Button(self.Frame1, text="CLEAR", width=14, command=self.cleardata)
        b7.grid(row=6, column=4,pady=10)
        
        b8 = Button(self.Frame1, text="total", width=14, command=self.Ref)
        b8.grid(row=7, column=4,pady=10)


    def Ref(self):
        
         
        

        if (self.idli.get()==""):
            CoIdly=0
        else:
            CoIdly=float(self.idli.get())

        if (self.french_fries.get()==""):
            CoFrench=0
        else:
            CoFrench=float(self.french_fries.get())
            
        if (self.cold_drink.get()==""):
            CoCold=0
        else:
            CoCold=float(self.cold_drink.get())

        
        if (self.dosa.get()==""):
            CoDosa=0
        else:
            CoDosa=float(self.dosa.get())



        if (self.pizza.get()==""):
            CoPizza=0
        else:
            CoPizza=float(self.pizza.get())

        if (self.burger.get()==""):
            CoBurger=0
        else:
            CoBurger=float(self.burger.get())



         
        if (self.pasta.get()==""):
            CoD=0
        else:
            CoD=float(self.pasta.get())

                       
        CostofIdly =CoIdly * 50
        CostofBurger=CoBurger * 20
        CostofDosa = CoDosa* 35
        CostofPizza = CoPizza * 25
        COstofCold_drink=CoCold*15
        CostofFrench_fries=CoFrench*50
        CostofPasta=CoD*15
        

        CostofMeal= "Rs", str('%.2f' % (CostofIdly+CostofBurger+CostofDosa+
                                        CostofPasta+CostofFrench_fries+
                                        CostofPizza+COstofCold_drink))

        PayTax=((CostofIdly+CostofBurger+CostofDosa+CostofPasta+
                 CostofFrench_fries+CostofPizza+COstofCold_drink) * 0.2)

        TotalCost=(CostofIdly+CostofBurger+CostofDosa+CostofPasta+
                   CostofFrench_fries+CostofPizza+COstofCold_drink)
     
        Ser_Charge= ((CostofIdly+CostofBurger+CostofDosa+CostofPasta+
                      CostofFrench_fries+CostofPizza+COstofCold_drink)/99)

        Service = "Rs", str ('%.2f' % Ser_Charge)

        OverAllCost ="Rs", str ('%.2f' % (PayTax+TotalCost+Ser_Charge))

        PaidTax= "Rs", str ('%.2f' % PayTax)

        self.service_charge.set(Service)
        self.tax.set(PaidTax)
        
        self.net_amount.set(OverAllCost)

    
    

    def get_selected_row(self,event): 
        try:
            index = self.list1.curselection()[0]
            self.selected_tuple = self.list1.get(index)
            self.e1.delete(0,END)
            self.e1.insert(END,self.selected_tuple[1])
            self.e3.delete(0, END)
            self.e3.insert(END,self.selected_tuple[2])
            self.e9.delete(0, END)
            self.e9.insert(END,self.selected_tuple[3])
            self.e2.delete(0, END)
            self.e2.insert(END,self.selected_tuple[4])
            self.e11.delete(0,END)
            self.e11.insert(END,self.selected_tuple[5])
            
        except IndexError:
            pass                

    def view_command(self):
        self.list1.delete(0, END)  
        for row in database.view():
            self.list1.insert(END, row)


    def cleardata(self):
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e4.delete(0, END)
        self.e5.delete(0, END)
        self.e6.delete(0, END)
        self.e7.delete(0, END)
        self.e8.delete(0, END)
        self.e9.delete(0, END)
        self.e10.delete(0, END)
        self.e11.delete(0, END)

    def search_command(self):
        self.list1.delete(0, END)
        for row in database.search(self.reference.get(),
                                   self.net_amount.get(),
                                   self.service_charge.get(),
                                   self.tax.get(),self.pasta.get()):
            self.list1.insert(END, row)


    def add_command(self):
        database.insert(self.reference.get(), self.net_amount.get(),
                        self.service_charge.get(), self.tax.get(),
                        self.pasta.get())
        self.list1.delete(0, END)
        self.list1.insert(END, self.reference.get(),self.pasta.get(),
                          self.net_amount.get(), self.service_charge.get(),
                          self.tax.get(),self.pasta.get())

    def delete_command(self):
        database.delete(self.selected_tuple[0])
        self.view_command()

    def update_command(self):
        
        database.update(self.selected_tuple[0],self.reference.get(),
                        self.net_amount.get(), self.service_charge.get(),
                        self.tax.get(),self.pasta.get())
        self.view_command()


window = Tk()
Window(window)

window.mainloop()
