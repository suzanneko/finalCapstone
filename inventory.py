
# This program is a tool for a shoe retailer warehouse manager.
# It takes data recording stock and gives an overview of the stock taking results.
# The user can view a table of all the stock items, enter a new stock item, find a shoe using its code,
# identify the shoes with the lowest and highest quantity of stock for re-stock or sale,
# or find the stock value for each item.

from tabulate import tabulate

# Below, the class Shoe has been created to represent each shoe product.
# Each shoe object takes on the attributes: country, code, product, cost and quantity.
# Get and set methods are created within the class.

class Shoe:
    '''
    A class used to represent a shoe product.

    Attributes
    ----------
    country: str
        country associated with the shoe product
    code: str
        the product code 
    product: str
        the product name
    cost: int
        the product cost
    quantity: int
        the product quantity

    Methods
    -------

    __init__
        Constructor for the class Shoe

    get_country
        returns the shoe product's country
    
    get_code
        returns the shoe product's code
    
    get_product
        returns the shoe products name
    
    get_cost
        returns the shoe product's cost
    
    get_quantity
        returns the shoe product's quantity of stock
    
    set_quantity
        sets the shoe product's quantity of stock

    __str__
        This special method is called by Python when you use the 'print' command
        on an object.

    '''

    def __init__(self, country, code, product, cost, quantity):
        '''
        Constructor for the class Shoe

        Parameters
        ----------
        country: str
            country associated with the shoe product
        code: str
            the product code 
        product: str
            the product name
        cost: int
            the product cost
        quantity: int
            the product quantity

        '''
        self.country=country
        self.code=code
        self.product=product
        self.cost=cost
        self.quantity=quantity

    def get_country(self):
        '''
        returns the shoe product's country        
        '''
        return self.country

    def get_code(self):
        '''
        returns the shoe product's code
        '''
        return self.code
    
    def get_product(self):
        '''
        returns the shoe product's name
        '''
        return self.product

    def get_cost(self):
        '''
        returns the shoe product's cost
        '''
        return self.cost
    
    def get_quantity(self):
        '''
        returns the shoe product's quantity of stock
        '''
        return self.quantity

    def set_quantity(self,quantity):
        '''
        sets the shoe product's quantity of stock
        '''
        self.quantity=quantity

    def __str__(self):
        '''
        what is printed when you use the 'print' command on an object
        '''
        return (f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}\n")

# 'shoe_list' stores a list of Shoe objects

shoe_list = []

# Below, functions are defined outside of the class. 

# Data is read from 'inventory.txt' file and organised into a list where each item is data for a shoe product.
# A for loop ignores the first line of data (header) and splits each item into a list.
# This is used to create a Shoe object which is added to 'shoe_list'.

def read_shoes_data(shoe_list):
    '''
    Creates shoe objects using data read from 'inventory.txt' and adds the objects to the shoes list.
    
    '''
    f=open("inventory.txt","r")
    data=f.read()
    data_list=data.split("\n")
    for i in range(1,len(data_list)):
        try:
            item=data_list[i].split(",")
            item=Shoe(item[0],item[1],item[2],item[3],item[4])
            shoe_list.append(item)
        except:
            continue
    f.close()

# The capture_shoes function elicits information from the user and creates a new Shoe object.
# It is added to the shoes list and the original data file.

def capture_shoes(shoe_list):
    '''
    Allows user to enter data to add a new shoe product.
    '''
    country_new=input("Enter the country:")
    code_new=input("Enter the product code:")
    product_new=input("Enter the product name:")
    cost_new=input("Enter the cost:")
    quantity_new=input("Enter the quantity of stock:")
    new_item=Shoe(country_new,code_new,product_new,cost_new,quantity_new)
    shoe_list.append(new_item)

    f=open("inventory.txt","a")
    f.write(f"{str(new_item)}")

    f.close()

# The view_all function uses a for loop to convert each Shoe object into its String format.
# Each item is split into a list and added to 'table'.
# The tabulate function is then used to present the data.

def view_all(shoe_list):
    '''
    Prints all shoe data in a table.
    '''
    table=[]
    print('''
================================================================================
                        Stock Data for All Shoe Items
================================================================================
    
    ''')
    for item in shoe_list:
        item=str(item).split(",")
        table.append(item)
    header=["Country","Code","Product","Cost","Quantity"]
    print(tabulate(table,headers=header))

# The re_stock function uses a for loop to retrieve the quantity of stock for each item.
# This is used to create a list of quantities, 'quantity'. The lowest quantity of stock is found.
# Another for loop finds items with the lowest quantity and asks the user to enter how much to restock.
# The set_quantity method updates the quantity for the object and the original data file is updated.

def re_stock(shoe_list):
    '''
    Allows the user to increase the stock of the item(s) with the lowest stock.
    '''
    quantity=[]
    for item in shoe_list:
        quantity.append(int(item.get_quantity()))

    min_stock=min(quantity)
    
    print("The item(s) with the lowest stock levels:")

    for item in shoe_list:
        if int(item.get_quantity())==min_stock:

            stock_increase=int(input(f'''
    
    Country: {item.get_country()}
    Code: {item.get_code()}
    Product: {item.get_product()}
    Cost: {item.get_cost()}
    Quantity: {item.get_quantity()}
        
    Please enter the quantity of shoes that you would like to add:'''))

            item.set_quantity(min(quantity)+stock_increase)

    f=open("inventory.txt","w")
    f.write("Country,Code,Product,Cost,Quantity\n")
    for item in shoe_list:
        f.write(str(item))

    f.close()

# The search_shoe function allows the user to enter the shoe code they wish to view the details for.
# A for loop goes through each item and the get_code method is used to find the item and print it. 

def search_shoe(shoe_list,search_code):
    '''
    Allows the user to search for an item by code and prints its data.
    '''
    
    for item in shoe_list:
        if search_code==item.get_code():
            return item

# The value_per_item function uses a for loop to iterate against each item.
# Stock value of each item is found by cost x quantity (found using get_cost and get_quantity methods)
# This is printed in table form.

def value_per_item(shoe_list):
    '''
    Calculates the total stock value for each item and prints.
    '''

    table=[]
    for item in shoe_list:
        stock_value=int(item.get_cost())*int(item.get_quantity())
        item=str(item)+","+str(stock_value)
        item=item.split(",")
        table.append(item)
    header=["Country","Code","Product","Cost","Quantity","Stock Value"]
    print("\n\n")
    print(tabulate(table,headers=header))

# The highest_qty function uses a for loop to retrieve the quantity of stock for each item.
# This is used to create a list of quantities, 'quantity'. The highest quantity of stock is found.
# Another for loop finds items with the highest quantity and prints them.

def highest_qty(shoe_list):
    '''
    Identifies the item(s) with the highest stock levels and prints that they are for sale.
    '''
    quantity=[]
    for item in shoe_list:
        quantity.append(int(item.get_quantity()))
    max_stock=max(quantity)
    print(f"\n\nThe following item(s) have the highest stock levels:")

    for item in shoe_list:
        if int(item.get_quantity())==max_stock:
            print(f'''
    This item is for sale:

    Country: {item.get_country()}
    Code: {item.get_code()}
    Product: {item.get_product()}
    Cost: {item.get_cost()}
    Quantity: {item.get_quantity()}
        
    ''')

def main():
    '''
    Displays the main menu and calls the required functions as selected by the user.
    '''
    shoe_list=[]
    read_shoes_data(shoe_list)
    while True:
        user_choice=input('''
        
=======================================================================
                            MAIN MENU
=======================================================================
Please select from the following options:

1 - View all shoes
2 - Enter a new shoe
3 - Re-stock shoe with the lowest stock
4 - Search for a shoe using the code
5 - View stock value for each item
6 - View the item with the highest stock
7 - Exit

Enter the number of the option you would like to select (1-7):''').strip()

        if user_choice=="1":
            view_all(shoe_list)
        elif user_choice=="2":
            capture_shoes(shoe_list)
        elif user_choice=="3":
            re_stock(shoe_list)
        elif user_choice=="4":
            search_code=input("Enter the code of the shoes that you wish to view the details for:")
            print(f'''
Country:\t{search_shoe(shoe_list,search_code).get_country()}
Code:\t\t{search_shoe(shoe_list,search_code).get_code()}
Product:\t{search_shoe(shoe_list,search_code).get_product()}
Cost:\t\t{search_shoe(shoe_list,search_code).get_cost()}
Quantity:\t{search_shoe(shoe_list,search_code).get_quantity()}
            ''')

        elif user_choice=="5":
            value_per_item(shoe_list)
        elif user_choice=="6":
            highest_qty(shoe_list)
        elif user_choice=="7":
            "Goodbye"
            break
        else:
            print("You have entered an invalid option. Please try again.")


main()