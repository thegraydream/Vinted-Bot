# Import
from requirements import *
import subprocess

createfolder('settings', False)
createconfigfile('settings/settings.ini', None, False)

# Settings Category
createcategory('settings/settings.ini', 'settings', False)
defaultconfig('settings/settings.ini', 'settings', 'exitkeybind', 'e', False)
defaultconfig('settings/settings.ini', 'settings', 'timebetweeneachrefresh', '3', False)
defaultconfig('settings/settings.ini', 'settings', 'discord', 'true', False)
defaultconfig('settings/settings.ini', 'settings', 'seewebbrowser', 'false', False)
defaultconfig('settings/settings.ini', 'settings', 'logs', 'true', False)
defaultconfig('settings/settings.ini', 'settings', 'runonlaunch', 'false', False)


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


if readconfig('settings/settings.ini', 'settings', 'runonlaunch') == "true":
    subprocess.run(['python', 'modules/vinted.py'])
else:subprocess.run(['python', 'modules/home.py'])