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
        try:choice = int(input(f'\n{colors("cyan")}Select the number corresponding to the product you want to edit > {colors()}'))
        except:error = "Please select a number from the list above !"

        if choice == 0:break

        count = 0
        for i in product:
            count += 1
            if choice == count:
                error = None
                while True:
                    productwebhook = readjson('settings/vintedconfig.json', i, 'Webhook')
                    productpricemin = readjson('settings/vintedconfig.json', i, 'PriceMin')
                    productpricemax = readjson('settings/vintedconfig.json', i, 'PriceMax')
                    productcurrency = readjson('settings/vintedconfig.json', i, 'Currency')
                    clear()
                    asciivinted()
                    nbchoice('0', 'Back')
                    nbchoice('1', f'Webhook: {productwebhook}')
                    nbchoice('2', f'Price min: {productpricemin}')
                    nbchoice('3', f'Price max: {productpricemax}')
                    nbchoice('4', f'Currency: {productcurrency}')
                    printerror(error)
                    try:choice = int(input(f'\n{colors("cyan")}Select the number corresponding to the product you want to edit > {colors()}'))
                    except:error = "Please select a number from the list above !"

                    if choice == 0:break
                    if choice == 1:
                        error = None
                        while True:
                            clear()
                            asciivinted()
                            nbchoice('0', 'Back')
                            printerror(error)
                            choice = str(input(f'\n{colors("cyan")}By what do you want to modify Webhook ? > {colors()}'))

                            if choice == "0":break
                            if sendwebhook(choice, readjson('settings/webhook.json', 'defaultwebhook', 'name'), "Verification", "The webhook has been verified!",readjson('settings/webhook.json', 'defaultwebhook', 'profilepicture'), readjson('settings/webhook.json', 'defaultwebhook', 'color')) == True:
                                writejson('settings/vintedconfig.json', i, 'Webhook', choice)
                                error = None
                                break
                            else:error = "The url of the Webhook is not valid !"

                    if choice == 2:
                        error = None
                        while True:
                            try:
                                clear()
                                asciivinted()
                                printerror(error)
                                choice = int(input(f'\n{colors("cyan")}By what do you want to modify price min ? > {colors()}'))
                                if not readjson('settings/vintedconfig.json', i, 'PriceMax') == "":
                                    if not choice > int(readjson('settings/vintedconfig.json', i, 'PriceMax')):
                                        writejson('settings/vintedconfig.json', i, 'PriceMin', choice)
                                        error = None
                                        break
                                    else:error=f"The price must be lower than the maximum price (maximum price '{readjson('settings/vintedconfig.json', i, 'PriceMax')}')"
                                else:
                                    writejson('settings/vintedconfig.json', i, 'PriceMin', choice)
                                    error = None
                                    break
                            except:error = "The minimum price must contain numbers!"

                    if choice == 3:
                        error = None
                        while True:
                            try:
                                clear()
                                asciivinted()
                                printerror(error)
                                choice = int(input(f'\n{colors("cyan")}By what do you want to modify price max ? > {colors()}'))
                                if not readjson('settings/vintedconfig.json', i, 'PriceMin') == "":
                                    if choice > int(readjson('settings/vintedconfig.json', i, 'PriceMin')):
                                        writejson('settings/vintedconfig.json', i, 'PriceMax', choice)
                                        error = None
                                        break
                                    else:error=f"The price must be higher than the minimum price (minimum price '{readjson('settings/vintedconfig.json', i, 'PriceMin')}')"
                                else:
                                    writejson('settings/vintedconfig.json', i, 'PriceMax', choice)
                                    error = None
                                    break
                            except:error = "The minimum price must contain numbers!"
                    if choice == 4:
                        error = None
                        while True:
                            try:
                                clear()
                                asciivinted()
                                nbchoice('0', 'Back')
                                printerror(error)
                                choice = str(input(f'\n{colors("cyan")}By what do you want to modify Currency (example: EUR, USD...)? > {colors()}')).upper()
                                if choice == "0":break
                                writejson('settings/vintedconfig.json', i, 'Currency', choice)
                                error = None
                                break
                            except:error = "An error has occurred"
    except:error = "Please select a number from the list above !"