# Import
from requirements import *
import subprocess

error = None


Name = readjson('settings/webhook.json', 'defaultwebhook', 'name')
defaulturl = readjson('settings/webhook.json', 'defaultwebhook', 'url')
ProfilePictureURL = readjson('settings/webhook.json', 'defaultwebhook', 'profilepicture')
Color = readjson('settings/webhook.json', 'defaultwebhook', 'color')

if Name == "":Nametf = False
else:
    Nametf = True
if defaulturl == "":defaulturltf = False
else:defaulturltf = True
if ProfilePictureURL == "":ProfilePictureURLtf = False
else:ProfilePictureURLtf = True
if Color == "":Colortf = False
else:Colortf = True


while True:
    try:
        clear()
        asciivinted()
        nbchoice('0', 'Cancel')
        nbchoice('1', 'Confirm')
        nbchoice('2', f'Default Url {defaulturl}', defaulturltf)
        nbchoice('3', f'Name {Name}', Nametf)
        nbchoice('4', f'Profile picture {ProfilePictureURL}', ProfilePictureURLtf)
        nbchoice('5', f'Embed Color {Color}', Colortf)
        printerror(error)

        choice = int(input(f'\n{colors("cyan")}Select the number corresponding to the choice above > {colors()}'))
        
        # Exit
        if choice == 0:break

        # Confirm
        elif choice == 1:
            if sendwebhook(defaulturl, readjson('settings/webhook.json', 'defaultwebhook', 'name'), "Verification", "The configuration has been successfully saved!",readjson('settings/webhook.json', 'defaultwebhook', 'profilepicture'), readjson('settings/webhook.json', 'defaultwebhook', 'color')) == True:            
                createconfigfile('settings/webhook.json', '{}')
                writejson('settings/webhook.json', 'defaultwebhook', 'name', Name)
                writejson('settings/webhook.json', 'defaultwebhook', 'url', defaulturl)
                writejson('settings/webhook.json', 'defaultwebhook', 'profilepicture', ProfilePictureURL)
                writejson('settings/webhook.json', 'defaultwebhook', 'color', Color)
                writejson('settings/webhook.json', 'defaultwebhook', 'active', 'True')
                break
            else:error = "The webhook parameters are invalid!"


        
        # Default URL
        elif choice == 2:
            error = None
            while True:
                try:
                    clear()
                    asciivinted()
                    nbchoice('0', 'Exit')
                    printerror(error)
                    choice = str(input(f"\n{colors('cyan')}Please enter the url of the Webhook > {colors()}"))
                    try:
                        if int(choice) == 0:break
                    except:None
                    if sendwebhook(choice, readjson('settings/webhook.json', 'defaultwebhook', 'name'), "Verification", "The webhook has been verified!",readjson('settings/webhook.json', 'defaultwebhook', 'profilepicture'), readjson('settings/webhook.json', 'defaultwebhook', 'color')) == True:
                        defaulturltf = True
                        defaulturl = choice
                        break
                    else:error = "The url of the Webhook is not valid !"
                except:error = "The url of the Webhook is not valid !"
        
        elif choice == 3:
            error = None
            while True:
                try:
                    clear()
                    asciivinted()
                    nbchoice('0', 'Exit')
                    printerror(error)
                    choice = str(input(f"\n{colors('cyan')}Please enter the name of the bot > {colors()}"))
                    try:
                        if int(choice) == 0:break
                    except:None
                    Nametf = True
                    Name = choice
                    break
                except:error = "The name is not valid!"

        elif choice == 4:
            error = None
            while True:
                try:
                    clear()
                    asciivinted()
                    nbchoice('0', 'Exit')
                    printerror(error)
                    choice = str(input(f"\n{colors('cyan')}Please enter the link of the bot's profile picture > {colors()}"))
                    try:
                        if int(choice) == 0:break
                    except:None
                    ProfilePictureURLtf = True
                    ProfilePictureURL = choice
                    break
                except:error = "The url of the profile picture is not valid !"

        elif choice == 5:
            error = None
            while True:
                try:
                    clear()
                    asciivinted()
                    nbchoice('0', 'Exit')
                    printerror(error)
                    choice = str(input(f"\n{colors('cyan')}Please enter the embed color in HEX (example: '00767F') > {colors()}"))
                    try:
                        if int(choice) == 0:break
                    except:None
                    Colortf = True
                    Color = choice
                    break
                except:error = "The url of the profile picture is not valid !"
    except:error = "Please select a number from the list above!"