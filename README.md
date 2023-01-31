# finalCapstone

## Title: inventory.py

### Description
This program is a tool for a shoe retailer warehouse manager. It takes data recording stock and gives an overview of the stock taking results. The user can view a table of all the stock items, enter a new stock item, find a shoe using its code, identify the shoes with the lowest and highest quantity of stock for re-stock or sale or find the stock value for each item. The program uses OOP, with the class Shoe representing a shoe product.

### Table of contents 
- [finalCapstone](#finalcapstone)
  * [Title: inventory.py](#title--inventorypy)
    + [Description](#description)
    + [Table of contents](#table-of-contents)
    + [How to install](#how-to-install)
    + [How to use](#how-to-use)
    + [Credits](#credits)

### How to install


### How to use
#### Data source
The source of the data used by the program is a text file named 'inventory.txt'.  This first line of the text file is a header which gives the data categories of the data that follows: 'Country,Code,Product,Cost,Quantity'.  Below this, each line gives the data for a product (shoe in this case).  The data must be given in the format shown in the header, with no spaces and separated by commas, e.g. UK,SKU23423,CoolAir,55,4.  The 'inventory.txt' file must be in the same folder as the program file.
![image](https://user-images.githubusercontent.com/121255678/215777361-c42acf75-527f-4177-8e31-369b27ec5436.png)

#### 
When the program is initiated by the user, the user is presented with a menu from which to select and option. The program immediately reads the data from the 'inventory.txt' file.
<img width="425" alt="image" src="https://user-images.githubusercontent.com/121255678/215779978-65f83c96-262d-4cba-8396-d1610ec02ce1.png">

##### 1 - View all shoes
All the shoes in the 'inventory.txt' file and any new shoes that have been added by the user under option 2 (Enter a new shoe) are displayed in a table format, showing the country, code, product, cost and quantity data.
<img width="383" alt="image" src="https://user-images.githubusercontent.com/121255678/215780437-c556a6de-f2b5-45b6-9b45-ebcb778c18e2.png">

##### 2 - Enter a new shoe
If this option is selected, the user is prompted to enter the country, code, product, cost and quantity data for the shoe they wish to add. It is then added to the 'inventory.txt' file.
<img width="336" alt="image" src="https://user-images.githubusercontent.com/121255678/215781959-eb8de822-7001-4af5-8460-a702720e70a0.png">

##### 3 - Re-stock the shoe with the lowest stock
This option searches for the item(s) with the lowest stock levels. It displays the item(s) to the user and prompts the user to input a quantity of stock they wish to add for the item. The additional stock is added to the existing stock quantity and updated in the 'inventory.txt' file.

##### 4 - Search for a shoe using the code

##### 5 - View stock value for each item


##### 6 - View the item with the highest stock
This option searches for the item(s) with the highest stock levels. It displays the item(s) to the user and prints that they are 'for sale'.





### Credits
<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>
