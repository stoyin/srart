The friut shop app is a simple python program that combines simple data structues,
functions and control flow logic to create an application for payment of friut items.
The use of indexing and for loops are very prominent in the structure of the program.

2 dictionary veriables are "shop" and "inventory" created to represnt friut items and 
their inventories respectively.

A list veriable "my_list" is used to store the friuts purchased by the user and a
veriable total_price is created to store the total expenses.

3 functions are created to help the process of the application:
 gen_price() helps in  listing the prices of all items available
 en_price() helps to show the price of an item on enquiry
 gen_enquiry() helps to list all the items and their corresponding inventory
 enquiry_item() helps to show the inventory of a particular item equired for

The real program happens in the loop. if the user inputs 'a' from the keyboard
the function "gen_price()" is executed, if the input is 'b' the function en_price() os 
executed and if the input is 'c' the program goes into another loop. In the inner loop
the program prompts the user for items.
if the item name is  "shop"  then the program prompts the user for the quantity of the item.
the items and quantity selected is appended into "my_list" in tuple pairings. The price of the items
is also indexed of the "shop" dictionary. The inventory veriable values has to duplicated based on the 
quantity item selected.

A for loop is used to print out the item selected, price perunit and final price. the total cost is calaulated
by updating the veriable "total_price". The number of items selected is determined by using the "len()" function 
on "my_list"

Finally in the outer loop the program prompts the user to perform another transaction or quit using "yes" or "no"
response if "yes" the whole program loop is re-executed again if "no" the program breaks out of the loop. And stops
execution.
