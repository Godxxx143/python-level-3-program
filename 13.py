print("sundar computer market")
print("tindivanam, villupuram distric")
print("------------------------------")
print("bill receipt")
no=int(input("Enter the item No:"))
prt=input("Enter the particular:")
rate=int(input("Enter the rate:"))
Qty=int(input("Enter the quantity:"))
total=rate*Qty
print("total Amount in Rupees:",total)
if(total >= 100000):
    gst=total*10/100
elif(total >= 50000):
    gst=total*5/100
elif(total >=20000):
    gst=total*3/100
elif(total >=10000):
    gst=total*2/100
else:
    gst=total*1/100
print("Gst(goods and service 10%):",gst)
amt=total+gst
print("amount to be paid:",amt)
