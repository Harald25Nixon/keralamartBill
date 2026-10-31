cName=input("Enter the Customer Name")
iNam=input("Enter the Item Name")
qtyy=int(input("Enter the Quantity"))
ppu=int(input("Enter the Price Per Unit"))
lMem=input("Enter the loyalty member[yes/no]")
pMod=input("Enter the Paymemt Mode")
amt=(qtyy*ppu)
print("="*60)
print("Kerala Fresh Mart".center(60))
print("Smart Billing".center(60))
print("="*60)
print(f'Customer Name : {cName}')
print(f'Item Name : {iNam}')
print(f"Quantity : {qtyy}")
print(f"Price per unit (Rs) : {ppu}")
print(f"Loyalty member? (yes/no) : {lMem}")
print(f"Payment mode (cash/upi/card) : {pMod}")
print()
print(f"Customer : {cName}")
print("-"*60)
print(f"{"Item"}{"Qty":>23}{"Price":>13}{"Amount":>20}")
print(f"{iNam}{qtyy:>23}{ppu:>13}{amt:>20,.2f}")
print("-"*60)
print(f"Amount: {amt:>52,.2f}")
if(amt<500):
  dis=(0.0*amt)
  print(f"{"Discount rate:"}{"0%":>46}")
  print(f"{"Discount:"}{dis:>51,.2f}")
else:
  if(amt>=2000):
    dis=(0.1*amt)
    print(f"{"Discount rate:"}{"10%":>46}")
    print(f"{"Discount:"}{dis:>51,.2f}")
  elif(amt>=1000):
    dis=(0.05*amt)
    print(f"{"Discount rate:"}{"5%":>46}")
    print(f"{"Discount:"}{dis:>51,.2f}")
  else:
    dis=(0.02*amt)
    print(f"{"Discount rate:"}{"2%":>46}")
    print(f"{"Discount:"}{dis:>51,.2f}")
if(amt>=500 and lMem=="yes"):
  lBo=25
  print(f"{"Loyalty bonus:"}{lBo:>46,.2f}")
else:
  lBo=0
  print(f"{"Loyalty bonus:"}{lBo:>46,.2f}")
tamt=(amt-dis-lBo)
print(f"{"Taxable amount:"}{tamt:>45,.2f}")
gst=(0.05*tamt)
gTo=(tamt+gst)
print(f"{"GST (5%):"}{gst:>51,.2f}")
print(f"{"Grand Total:"}{gTo:>48,.2f}")
print("="*60)
if(gTo>10000 and (pMod.lower()=="upi" or pMod.lower()=="card")):
  print(f"{"Bonus: free cloth bag with this order!"}")
  print(f"{"Payment accepted via "}{pMod}")
elif(gTo>10000 and (pMod.lower()=="cash")):
  print(f"{"Bonus: free cloth bag with this order!"}")
  print(f"Cash limit of Rs 10,000 exceeded. Please pay by UPI or card")
elif(gTo<=10000 and (pMod.lower()=="upi" or pMod.lower()=="card" or pMod.lower()=="cash")):
  print(f"payment accepted via {pMod}")
else:
  print("Invalid payment mode. Bill not settled")