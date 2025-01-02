product=[]


while True:
    choice =int(input(f"1. Add\n2. Remove\n3. Display Items\n4. Total Cost\n Input Your Choice :"))
    if choice==1:
        #adding item to the list
       name= input(f"Input product Name: ") 
       price= float(input(f"input(Input product price: "))
       quantity= int(input(f"input product quantity: "))
       item={
           "name" : name,
           "price" : price,
           "quantity" : quantity,
       }
       product.append(item)
       print("item added sucessfully")

    elif choice ==2:
        name_rem = input("Enter the name that you want to remove: ")
        is_removed = False
        for item in product:
            if item['name']==name_rem :
                product.remove(item)
                print("Product removed sucessfully" )
                is_removed=True
                break
            if not is_removed:
                print(f"the product {name_rem} is not found")



            elif choice == 3:
                #Displaying records
                if not product:
                    print("Product are not available.")  
                else :
                    for item in product:
                        print(f"name: {item['name']} quantity : {item['quantity']}price :{item['price']} total cost :{item['quantity']*item['price']}")
            elif choice == 4:
                total_cost = sum(item['price']*item['quantity'] for item in product )
                print(f"the total cost is rs. {total_cost}")
            else :
                print("invalid input please enter valid number")
                break




   

