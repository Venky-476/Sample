#functions to define -- def

'''def great():
    print("hello world")
great()'''

'''def add(a,b):
    print(a+b)
add(2,7)
add(10,30)'''

'''def square(num):
    return num*num
print(square(6))'''

'''def student(*name,age):
    print(name,age)
student("venky", "ven", age=22)'''

'''def greet(name):
    print("Hello", name)
greet("venky")
greet("sneha")'''

'''def total(*num):
    print(sum(num))
total(1,23,5,6,7)'''

'''def total(a,b):
    print(a-b)
total(99,43)

def multi(c,d):
    print(c*d)
multi(65,44)'''

'''def num(a):
    if a%2==0:
        print("even")
    else:
        print("odd")
num(77)'''

#Write a function register_user(name, email, password) that: 
# Validates all fields. Returns: "Registration Successful" if all validations pass. 
# Otherwise returns an appropriate error message.

'''def register_user(name,email,password):
    if name=="":
        return "enter your name"
    if "@" not in email or "." not in email:
        return "invalid email"
    if len(password)<8:
        return "enter correct password"
    return "Success"
print(register_user("venky","venky123@gmail.com","Venkatesh123"))'''

'''def check_user_name(name):
    user_name=["venky", "sneha", "admin", "rahul"]
    if name in user_name:
        print("user exists")
    else:
        print("user avaiable")
name=input()
check_user_name(name)'''

'''def check_gmail_user(gmail):
    gmail_user=("venky@gmail.com", "sneha@gmail.com")
    if "@" not in gmail_user:
        print("invalid gmail")
    if "@" in gmail_user:
        print("gmail success")
    else:
        print("enter correct gmail")
gmail=input()
check_gmail_user(gmail)'''



'''def check_gmail(email):

    registered_emails = [
        "sneha@gmail.com",
        "venky@gmail.com",
        "admin@gmail.com"
    ]

    if email in registered_emails:
        print("Email Already Exists")

    if email not in registered_emails:

        if "@" not in email:
            print("@ symbol is missing")

        if "@gmail.com" not in email:
            print("Invalid Gmail Address")

        if "@" in email and "@gmail.com" in email and email != "@gmail.com":
            print("Email Available")


email = input("Enter Email: ")
check_gmail(email)
    



def register_user(name,email,password):
    if name=="":
        print("enter your name")
    if "@" not in email or "." not in email:
        print("invalid email")
    if len(password)<8:
        print("enter correct password")
    return "Success"
register_user("venky","venky123@gmail.com","Venkatesh@123")'''



cart = []

def add_product():
    product = input("Enter product name: ")
    cart.append(product)
    print(product, "added to cart.")

def remove_product():
    product = input("Enter product name to remove: ")
    if product in cart:
        cart.remove(product)
        print(product, "removed from cart.")
    else:
        print("Product not found in cart.")

def display_cart():
    if len(cart) == 0:
        print("Your cart is empty.")
    else:
        print("\nProducts in Cart:")
        for item in cart:
            print("-", item)

def total_items():
    print("Total items in cart:", len(cart))


while True:
    print("\n===== Shopping Cart =====")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Display Cart")
    print("4. Total Items")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        remove_product()
    elif choice == "3":
        display_cart()
    elif choice == "4":
        total_items()
    elif choice == "5":
        print("Thank you for shopping!")
        break
    else:
        print("Invalid choice. Please try again.")



'''orders = {
    101: "Placed",
    102: "Packed",
    103: "Shipped",
    104: "Delivered",
    105: "Packed"
}

def track_order(order_id):
    if order_id in orders:
        print("Order Status:", orders[order_id])
    else:
        print("Invalid Order ID")

order_id = int(input("Enter Order ID: "))
track_order(order_id)'''


playlist=[]

print("=====Music Playlist Manager=====")
print("1. Add Song")
print("2. Remove Song")
print("3. Display Playlist")
print("4. Search Song")
print("5. Exit")

choice = input("Enter your choice: ")
if choice =="1":
    playlist.append("song")
    print(song ,"added to playlist")
elif choice =="2":  
    playlist.remove("song")
    print("remove song in playlist")
elif choice =="3":
    playlist.display("display playlist")
    print()