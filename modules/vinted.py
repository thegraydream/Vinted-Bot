# Import
from requirements import *
import time
import keyboard

newproduct = 0
requestssend = 0
producterror = 0

while True:
    try:
        if keyboard.is_pressed(readconfig("settings/settings.ini", "settings", "exitkeybind")):break
        
        with open('settings/vintedconfig.json', "r") as f:
            product = json.load(f)
        for i in product:
            clear()
            asciivinted()
            print(f'{colors("cyan")}Remain press on "{readconfig("settings/settings.ini", "settings", "exitkeybind")}" to Exit')
            print(f'{colors("cyan")}Desired product:{colors()} {getnumberproduct()}')
            print(f'{colors("cyan")}Product:{colors()} {i}')
            print(f'{colors("cyan")}Requests sent:{colors()} {requestssend}')
            print(f'{colors("cyan")}New product:{colors()} {newproduct}')
            print(f'{colors("cyan")}Error:{colors()} {producterror}')

            requestssend+=1

            productwebhook = ""
            productpricemin = ""
            productpricemax = ""
            productemail = ""
            productcurrency = ""

            productname = i.replace(" ", "%20")
            if not readjson('settings/vintedconfig.json', i, 'Webhook') == "": productwebhook = readjson('settings/vintedconfig.json', i, 'Webhook')
            if not readjson('settings/vintedconfig.json', i, 'PriceMin') == "": productpricemin = f"&price_from={readjson('settings/vintedconfig.json', i, 'PriceMin')}"
            if not readjson('settings/vintedconfig.json', i, 'PriceMax') == "": productpricemax = f"&price_to={readjson('settings/vintedconfig.json', i, 'PriceMax')}"
            if not readjson('settings/vintedconfig.json', i, 'Email') == "": productemail = readjson('settings/vintedconfig.json', i, 'Email')
            if not readjson('settings/vintedconfig.json', i, 'Currency') == "": productcurrency = f"&currency={readjson('settings/vintedconfig.json', i, 'Currency')}"

            if productwebhook == "": productwebhook = readjson('settings/webhook.json', 'defaultwebhook', 'url') 

            link = f"https://www.vinted.fr/vetements?search_text={productname}{productpricemin}{productcurrency}{productpricemax}&order=newest_first"
            status = scrap(link,i, 0, productwebhook)[0]
            if status == True:newproduct+=1
            elif status == False:producterror+=1
            elif status == None:None
            time.sleep(int(readconfig("settings/settings.ini", "settings", "timebetweeneachrefresh")))
    except:producterror+=1
