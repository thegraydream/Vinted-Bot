#Import
from requirements import *
import json

error = None

while True:
    try:
        count = 0
        with open('settings/vintedconfig.json', "r") as f:
            product = json.load(f)
        clear()
        asciivinted()
        nbchoice('0', 'Back')

        for i in product:
            count += 1
            nbchoice(count, i)
        printerror(error)
        try:choice = int(input(f'\n{colors("cyan")}Select the number corresponding to the product you want to delete > {colors()}'))
        except:error = "Please select a number from the list above !"

        if choice == 0:break

        count = 0
        for i in product:
            count += 1
            if choice == count:
                del product[i]
                with open('settings/vintedconfig.json', "w") as f:
                    json.dump(product, f)

    except:None