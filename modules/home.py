# Import
from requirements import *
import subprocess
import json

error = None

while True:
    try:
        clear()
        asciivinted()
        nbchoice('0', 'Run')
        nbchoice('1', f'Product ({getnumberproduct()})')
        nbchoice('2', f'Discord Webhook (Active: {readjson("settings/webhook.json", "defaultwebhook", "active")})')
        nbchoice('3', 'Settings')
        printerror(error)
    
        choice = int(input(f'\n{colors("cyan")}Select the number corresponding to the choice above > {colors()}'))

        # Run
        if choice == 0:
            error = None
            count = 0
            try:
                with open('settings/vintedconfig.json', "r") as f:
                    product = json.load(f)
                    for i in product:count+=1
                    if not count == 0:subprocess.run(['python', 'modules/vinted.py']) 
                    else:error = "please select at least 1 product!"
            except:error = "please select at least 1 product!"

        # Product Manager
        elif choice == 1:
            error = None
            subprocess.run(['python', 'modules/product.py'])

        elif choice == 2:
            error = None
            subprocess.run(['python', 'modules/webhook.py'])


        elif choice == 3:
            error = None
            subprocess.run(['python', 'modules/settings.py'])
            

        else:error = "Please select a number from the list above!"
    except:error = "Please select a number from the list above!"