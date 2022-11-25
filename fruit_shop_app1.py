shop={'oranges':20,'pinnaple':150,'eggs':80,'banana':200}
inventory={'oranges':120,'pinnaple':300,'eggs':1000,'banana':400}
my_items=[]
total_price=0

fhand=open('receipt.txt','w')



def gen_price():
    d_list=list(shop.items())
    for x,y in d_list:
        print(f"{x} is {y}$")
        
def en_price(item):
    x=shop[item]
    print(f"{item} is {x}$")

def gen_enquiry():
    d_list=list(inventory.items())
    for x,y in d_list:
        print(f"{x} remains {y}")
   
def enquiry_item(item):
    x=inventory[item]
    print(f"the amount of {item} remaining is {x}")






        


while True:
    enter_1= input("to make enquires press 'a'\nto check price press 'b'\nto buy press'c'\nto check out press 'x' ")
    if enter_1== 'a':
        gen_enquiry()
    elif enter_1 =='b':
        gen_price()
    elif enter_1 =='c':
        while True:
            item_name=input("enter your items")
            if item_name=="x":
                break
            if item_name not in shop.keys():
                continue
            else:
                units=float(input("how many ?"))
                price=shop[item_name]
                my_items.append((item_name,price,units))
                inventory[item_name]-=units
                
                        
        for a,b,c in my_items:
            print(f"{c} units of  {a}:{b} price {c*b}")
            fhand.write(f"{c} units of  {a}: price = {c*b} \n")
            p=b*c
            total_price+=p
            num_items=len(my_items)
            
        fhand.write(f"total price = {total_price}, number of items = {num_items}")   
        fhand.close()
        
        

                
    options=input ("do you want to perform another transactuon: 'yes' or 'no'")
    if options=="yes":
        continue
    elif options =="no":
        print("THANK YOU FOR YOUR PATRONAGE")
        break
    



  



