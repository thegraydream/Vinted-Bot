# Import
from requirements import *
import subprocess

createfolder('settings')
createconfigfile('settings/settings.ini')

# Settings Category
createcategory('settings/settings.ini', 'settings')
defaultconfig('settings/settings.ini', 'settings', 'exitkeybind', 'e')
defaultconfig('settings/settings.ini', 'settings', 'timebetweeneachrefresh', '5')
defaultconfig('settings/settings.ini', 'settings', 'discord', 'true')
defaultconfig('settings/settings.ini', 'settings', 'seewebbrowser', 'false')

createconfigfile('settings/vintedconfig.json', '{}')

if verifyfile('settings/webhook.json') == False:
    createconfigfile('settings/webhook.json', '{}')
    with open('settings/webhook.json', "r") as f:
        data = json.load(f)
    data['defaultwebhook'] = {
        "active": "False",
        "name": f"Vinted Bot", 
        "url": f"",
        "profilepicture": f"https://c.clc2l.com/t/v/i/vinted-eIg4kp.png",
        "color": f"00757F"
        }
    with open('settings/webhook.json', "w") as f:
        json.dump(data, f)

if sendwebhook(readjson('settings/webhook.json', 'defaultwebhook', 'url'), readjson('settings/webhook.json', 'defaultwebhook', 'name'), "Startup", "The bot is started correctly !",readjson('settings/webhook.json', 'defaultwebhook', 'profilepicture'), readjson('settings/webhook.json', 'defaultwebhook', 'color')) == True:
    writejson('settings/webhook.json', 'defaultwebhook', 'active', 'True')
else: writejson('settings/webhook.json', 'defaultwebhook', 'active', 'False')


subprocess.run(['python', 'modules/home.py'])