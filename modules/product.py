# Import
from requirements import *
import subprocess

error = None

while True:
    try:
        clear()
        asciivinted()
        nbchoice('0', 'Back')
        nbchoice('1', 'Add a product')
        nbchoice('2', 'Edit a product')
        nbchoice('3', 'Delete a product')
        printerror(error)

        choice = int(input(f'\n{colors("cyan")}Select the number corresponding to the choice above > {colors()}'))
        
        # Exit
        if choice == 0:break

        # Add Product
        elif choice == 1:
            error = None
            subprocess.run(['python', 'modules/addproduct.py'])
        elif choice == 2:
            error = None
            subprocess.run(['python', 'modules/editproduct.py'])
        elif choice == 3:
            error = None
            subprocess.run(['python', 'modules/deleteproduct.py'])  

        else:error = "Please select a number from the list above!"
    except:error = "Please select a number from the list above!"