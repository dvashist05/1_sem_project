from tkinter import*
import random
import time
import datetime

root=Tk()
root.geometry("1600x8000")
root.title("Laundary Management System")

Tops=Frame(root, width=1600,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

#=================================================================================
#                  TIME
#================================================================================
localtime=time.asctime(time.localtime(time.time()))

lblInfo=Label(Tops,font=('arial',50,'bold'),text="Bennett Laundary System ",fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)

lblInfo=Label(Tops,font=('arial',20,'bold'),text="**extra charges for winter cloths",fg="green",bd=10,anchor='w')
lblInfo.grid(row=2,column=0)

def Ref():
    rand.get()==""

    if (Shirt.get()==""):
        CoShirt=0
    else:
        CoShirt=float(Shirt.get())


    
    if (Pant.get()==""):
        CoPant=0
    else:
        CoPant=float(Pant.get())



    if (Shorts.get()==""):
        CoShorts=0
    else:
        CoShorts=float(Shorts.get())



    if (Sweater.get()==""):
        CoSweater=0
    else:
        CoSweater=float(Sweater.get())

        
    if (Hoodie.get()==""):
        CoHoodie=0
    else:
        CoHoodie=float(Hoodie.get())

     
    if (Blanket.get()==""):
        CoBlanket=0
    else:
        CoBlanket=float(Blanket.get())

                   
    CostofShirt =CoShirt * 0
    CostofPant=CoPant * 0
    CostofShorts = CoShorts* 0
    CostofSweater = CoSweater * 100
    CostHoodie = CoHoodie* 150
    CostBlanket=CoBlanket * 200

    Costofwashing= "Rs", str('%.2f' % (CostofShirt+CostofPant+CostofShorts+CostofSweater+CostHoodie+CostBlanket))

    PressCost=((CoBlanket*30)+(CoSweater*10)+(CoHoodie*15))

    TotalCost=((CostofShirt+CostofPant+CostofShorts+CostofSweater+CostHoodie+CostBlanket)+((CoBlanket*30)+(CoSweater*10)+(CoHoodie*15)))
    Totalnumber=(int)(CoShirt+CoPant+CoHoodie+CoShorts+CoBlanket+CoSweater)
 
    Ser_Charge= ((CostofShirt+CostofPant+CostofShorts+CostofSweater+CostHoodie+CostBlanket)* (2/10))

    Service = "Rs", str ('%.2f' % Ser_Charge)

    Total_Cost="Rs", str ('%.2f' % (PressCost+TotalCost+Ser_Charge))

    ExtraPaid= "Rs", str ('%.2f' % (PressCost+Ser_Charge))

    Service_Charge.set(Service)
    Cost.set(Costofwashing)
    Press.set(PressCost)
    SubTotal.set(Totalnumber)
    Total.set(Total_Cost)
    
def qExit():
    root.destroy()

def Reset():
    rand.set("") 
    Shirt.set("")
    Pant.set("")
    Shorts.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Sweater.set("")
    Press.set("")
    Cost.set("")
    Hoodie.set("")
    Blanket.set("")
    
#====================================Restaraunt Info 1===========================================================
rand = StringVar()
Shirt=StringVar()
Pant=StringVar()
Shorts=StringVar()
SubTotal=StringVar()
Total=StringVar()
Service_Charge=StringVar()
Sweater=StringVar()
Press=StringVar()
Cost=StringVar()
Hoodie=StringVar()
Blanket=StringVar()



lblReference= Label(f1, font=('arial', 16, 'bold'),text="Bennett ID",bd=16,anchor="w")
lblReference.grid(row=0, column=0)
txtReference=Entry(f1, font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtReference.grid(row=0,column=1)

lblShirt= Label(f1, font=('arial', 16, 'bold'),text="Shirt",bd=16,anchor="w")
lblShirt.grid(row=1, column=0)
txtShirt=Entry(f1, font=('arial',16,'bold'),textvariable=Shirt,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtShirt.grid(row=1,column=1)


lblPant= Label(f1, font=('arial', 16, 'bold'),text="Pant",bd=16,anchor="w")
lblPant.grid(row=2, column=0)
txtPant=Entry(f1, font=('arial',16,'bold'),textvariable=Pant,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtPant.grid(row=2,column=1)


lblShorts= Label(f1, font=('arial', 16, 'bold'),text="Shorts",bd=16,anchor="w")
lblShorts.grid(row=3, column=0)
txtShorts=Entry(f1, font=('arial',16,'bold'),textvariable=Shorts,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtShorts.grid(row=3,column=1)

lblSweater= Label(f1, font=('arial', 16, 'bold'),text="Sweater",bd=16,anchor="w")
lblSweater.grid(row=4, column=0)
txtSweater=Entry(f1, font=('arial',16,'bold'),textvariable=Sweater,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSweater.grid(row=4,column=1)

lblHoodie= Label(f1, font=('arial', 16, 'bold'),text="Hoodie",bd=16,anchor="w")
lblHoodie.grid(row=5, column=0)
txtHoodie=Entry(f1, font=('arial',16,'bold'),textvariable=Hoodie,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtHoodie.grid(row=5,column=1)

#============================================================================================================
#                                RESTAURANT INFO 2
#========================================================================================

lblBlanket= Label(f1, font=('arial', 16, 'bold'),text="Blanket",bd=16,anchor="w")
lblBlanket.grid(row=0, column=2)
txtBlanket=Entry(f1, font=('arial',16,'bold'),textvariable=Blanket,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtBlanket.grid(row=0,column=3)

lblCost= Label(f1, font=('arial', 16, 'bold'),text="Cost of Washing",bd=16,anchor="w")
lblCost.grid(row=1, column=2)
txtCost=Entry(f1, font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtCost.grid(row=1,column=3)


lblService= Label(f1, font=('arial', 16, 'bold'),text="Service Charge",bd=16,anchor="w")
lblService.grid(row=2, column=2)
txtService=Entry(f1, font=('arial',16,'bold'),textvariable=Service_Charge,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtService.grid(row=2,column=3)


lblPressCost= Label(f1, font=('arial', 16, 'bold'),text="Ironing Charge",bd=16,anchor="w")
lblPressCost.grid(row=3, column=2)
txtPressCost=Entry(f1, font=('arial',16,'bold'),textvariable=Press,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtPressCost.grid(row=3,column=3)

lblSubTotal= Label(f1, font=('arial', 16, 'bold'),text="Number Of Cloths",bd=16,anchor="w")
lblSubTotal.grid(row=4, column=2)
txtSubTotal=Entry(f1, font=('arial',16,'bold'),textvariable=SubTotal,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSubTotal.grid(row=4,column=3)

lblTotalCost= Label(f1, font=('arial', 16, 'bold'),text="Total Cost",bd=16,anchor="w")
lblTotalCost.grid(row=5, column=2)
txtTotalCost=Entry(f1, font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtTotalCost.grid(row=5,column=3)

#==========================================Buttons==========================================================================================
btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="powder blue",command=Ref).grid(row=7,column=1)

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="powder blue",command=Reset).grid(row=7,column=2)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="powder blue",command=qExit).grid(row=7,column=3)


root.mainloop()


