# Import
from requirements import *

error = None
config = configparser.ConfigParser()
config.read('settings/settings.ini')

while True:
    count = 1
    try:
        clear()
        asciivinted()
        nbchoice('0', 'Cancel')
        nbchoice('1', 'Confirm')
        print()
        try:
            for i in config['settings']:
                count += 1
                nbchoice(count, f'{i} = {config["settings"][i]}')
        except:None
        printerror(error)

        choice = int(input(f'\n{colors("cyan")}Select the number corresponding to the parameter you want to change > {colors()}'))

        # Exit
        if choice == 0:break
        
        # Confirm
        if choice == 1:
            with open('settings/settings.ini', 'w') as configfile:
                config.write(configfile)
            break
        count = 1
        for i in config['settings']:
            count += 1
            if choice == count:
                clear()
                asciivinted()

                choice = str(input(f'\n{colors("cyan")}By what do you want to modify "{i} = {config["settings"][i]}" > {colors()}'))
                config.set('settings', f'{i}', f'{choice}')
                error = None


    except:error = "Please select a number from the list above!"
