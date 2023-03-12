#Import
from requirements import *
import json

error = None

webhookurl = readjson('settings/webhook.json', 'defaultwebhook', 'url')
prixmax = ""
prixmin = ""
email = ""
Product = ""
currency = ""



while True:
    try:
        if not prixmax==""and not prixmax=="":ProductPrice = True
        else:ProductPrice = False
        if not webhookurl=="":ProductWebhook=True
        else: ProductWebhook=False
        if not email=="":ProductEmail=True
        else: ProductEmail=False
        if not Product=="":ProductName=True
        else: ProductName=False
        if not currency=="":Productcurrency=True
        else: Productcurrency=False
        if not prixmin == "":prixminandmax = f"{prixmin} - {prixmax}"
        else:prixminandmax = ""

        clear()
        asciivinted()
        nbchoice('0', 'Cancel')
        nbchoice('1', 'Confirm')
        nbchoice('2', f'Webhook {webhookurl}', ProductWebhook)
        nbchoice('3', f'Product* {Product}', ProductName)
        nbchoice('4', f'Price {prixminandmax}', ProductPrice)
        nbchoice('5', f'Currency {currency}', Productcurrency)
        printerror(error)


        choice = int(input(f'\n{colors("cyan")}Select the number corresponding to the choice above > {colors()}'))

        # Exit
        if choice == 0:break

        # Confirm
        elif choice == 1:
            if Product == "":error = 'To confirm you must define a Product!'
            else:
                with open('settings/vintedconfig.json', "r") as f:
                    data = json.load(f)
                data[Product] = {
                            "Webhook": f"{webhookurl}", 
                            "Email": f"{email}",
                            "PriceMin": f"{prixmin}",
                            "PriceMax": f"{prixmax}",
                            "Currency": f"{currency}"
                            }
                with open('settings/vintedconfig.json', "w") as f:
                    json.dump(data, f)
                break


        # Webhook
        elif choice == 2:
            error = None
            while True:
                try:
                    clear()
                    asciivinted()
                    nbchoice('0', 'Back')
                    printerror(error)
                    choice = str(input(f"\n{colors('cyan')}Enter the url of the Webhook > {colors()}"))
                    try:
                        if int(choice) == 0:break
                    except:None
                    if sendwebhook(choice, readjson('settings/webhook.json', 'defaultwebhook', 'name'), "Verification", "The webhook has been verified!",readjson('settings/webhook.json', 'defaultwebhook', 'profilepicture'), readjson('settings/webhook.json', 'defaultwebhook', 'color')) == True:
                        ProductWebhook = True
                        webhookurl = choice
                        break
                    else:error = "The url of the Webhook is not valid !"
                except:error = "The url of the Webhook is not valid !"


        # Product
        elif choice == 3:
            error = None
            while True:
                try:
                    clear()
                    asciivinted()
                    nbchoice('0', 'Back')
                    printerror(error)
                    choice = str(input(f"\n{colors('cyan')}Enter the name of the product > {colors()}"))
                    try:
                        if int(choice) == 0:break
                    except:None
                    ProductName = True
                    Product = choice
                    break
                

                except:error = "The product name is not valid!"
        elif choice == 4:
            while True:
                error = None
                while True:
                    clear()
                    asciivinted()
                    printerror(error)
                    choice = str(input(f"\n{colors('cyan')}Enter the minimum price of the product > {colors()}"))
                    if not convertstrtoin(choice)== "-1": 
                        prixmin = convertstrtoin(choice)
                        break
                    error('The price must be a number!')
                error = None
                while True:
                    clear()
                    asciivinted()
                    print(f'{colors("cyan")}Minimum price: {prixmin} ')
                    printerror(error)
                    choice = str(input(f"\n{colors('cyan')}Enter the maximum price of the product > {colors()}"))
                    if not convertstrtoin(choice)== "-1":
                        if int(convertstrtoin(choice)) > int(prixmin):
                            prixmax = convertstrtoin(choice)
                            ProductPrice = True
                            break
                        else:error = "The maximum price must be higher than the minimum price!"
                break

        elif choice == 5:
            error = None
            while True:
                clear()
                asciivinted()
                nbchoice('0', 'Back')
                printerror(error)
                choice = str(input(f"\n{colors('cyan')}Enter the type of currency (EUR, USD...) > {colors()}"))
                if choice == 0:break
                currency = choice.upper()
                break
        else:error = "Please select a number from the list above!"
    except:error = "Please select a number from the list above!"

