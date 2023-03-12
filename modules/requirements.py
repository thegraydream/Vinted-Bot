# Import
import configparser
import os
import requests
import datetime
import re
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from fake_headers import Headers



# Get date
datenow = datetime.datetime.now()
date = ""
if date == "":date = datenow.strftime("%Y-%m-%d %H-%M-%S")


# Colors
def colors(color=None):
    if color == "cyan":return "\033[38;2;0;117;127m"
    elif color == "red":return "\033[31m"
    elif color == "green":return "\033[32m"
    else: return "\033[0m"

def clear():
    os.system('cls')

def asciivinted():
    print(f'{colors("cyan")}____   ____.__        __             .___ __________        __    ')
    print(f'{colors("cyan")}\   \ /   /|__| _____/  |_  ____   __| _/ \______   \ _____/  |_  ')
    print(f'{colors("cyan")} \   Y   / |  |/    \   __\/ __ \ / __ |   |    |  _//  _ \   __\ ')
    print(f'{colors("cyan")}  \     /  |  |   |  \  | \  ___// /_/ |   |    |   (  <_> )  |   ')
    print(f'{colors("cyan")}   \___/   |__|___|  /__|  \___  >____ |   |______  /\____/|__|   ')
    print(f'{colors("cyan")}                   \/          \/     \/          \/              ')
    print(f'{colors("cyan")}need help ? https://dsc.gg/tgdgithub\n')


def nbchoice(nb, text, TrueFalse=None):
    if TrueFalse == None:
        print(f'{colors()}[{colors("cyan")}{nb}{colors()}] {text}')
    elif TrueFalse == True:
        print(f'{colors()}[{colors("cyan")}{nb}{colors()}] {colors("green")}{text}')
    elif TrueFalse == False:
        print(f'{colors()}[{colors("cyan")}{nb}{colors()}] {colors("red")}{text}')

# Read configparser file
def readconfig(path, category, name, seeinlogs=True):
    config = configparser.ConfigParser()
    try:
        config.read(path)
        try:
            if seeinlogs == True:writeinlog(f'Read the "{name}" configuration in the "{category}" category of the "{path}" file.')
            return config[category][name]
        except:
            if seeinlogs == True:writeinlog(f'An error occurred while reading "{name}" in the "{category}" category of the "{path}" file. Please check that "{category}" and "{name}" exist in "{path}".')
            return ""
    except:
        if seeinlogs == True:writeinlog(f'An error occurred while reading the file "{path}". Please check that the file "{path}" exists.')
        return ""

def setconfig(path, category, name, config):
    config = configparser.ConfigParser()
    try:
        config.read(path)
        config.set(category, name, config)
        with open(path, 'w') as configfile:
            config.write(configfile)
        writeinlog(f'The configuration has been modified in the file "{path}" ("{category}": "{name}" = "{config}")')
        return True
    except:return False

# Create configparser file
def createconfigfile(path, write=None):
    try:
        with open(f'{path}', 'r') as f:None
    except:
        try:
            writeinlog(f'Creation of the configuration file "{path}".')
            with open(f'{path}', 'w') as f:
                writeinlog(f'The configuration file "{path}" has been created.')
                if write == None:None
                else:
                    f.write(f'{write}')
        except:writeinlog(f'An error occurred while creating the configuration file "{path}".')

# Create Folder
def createfolder(path, seeinlogs=True):
    try:
        if not os.path.exists(path):
            if seeinlogs == True:writeinlog(f'Creation of the "{path}" folder.')
            os.makedirs(path)
            if seeinlogs == True:writeinlog(f'The folder "{path}" has been created.')
    except:
        if seeinlogs == True:writeinlog(f'An error occurred while creating the "{path}" folder.')

# Default Config
def defaultconfig(path, category, name, names):
    config = configparser.ConfigParser()
    config.read(path)
    try:config[category][name]
    except:
        try:
            writeinlog(f'Create the default configuration of "{name}" in the "{category}" category of the "{path}" file.')
            config.set(category, name, names)
            with open(path, 'w') as configfile:
                config.write(configfile)
                writeinlog(f'The default configuration for "{name}" has been set to "{names}" in the "{path}" file.')
        except:writeinlog(f'An error occurred while creating the default configuration of "{name}" in the category "{category}" of the file "{path}".')

def createcategory(path, category):
    try:
        config = configparser.ConfigParser()
        try:config.read(path)
        except:writeinlog(f'An error occurred while reading the file "{path}". Please check that the file "{path}" exists.')
        if not config.has_section(category):
            writeinlog(f'Creation of the category "{category}" of the file "{path}".')
            config.add_section(category)
            writeinlog(f'The category "{category}" in the file "{path}" has been created.')
            with open(path, 'w', encoding='utf-8') as configfile:
                config.write(configfile)
    except:writeinlog(f'An error occurred while creating the category "{category}" in the file "{path}".')

def printerror(text):
    if not text == None:
        print(f"{colors('red')}{text}")

def convertstrtoin(text):
    try:
        strtoint = str(re.findall(r'\d+', text)[0])
        writeinlog(f'the string "{text}" has been successfully converted ("{strtoint}")')
        return strtoint
    except:return "-1"

def getnumberproduct():
    count = 0
    try:
        with open('settings/vintedconfig.json', "r") as fichier:
            product = json.load(fichier)
        for i in product:count += 1
        return count
    except:return 0

def verifyfile(path):
    try:
        writeinlog(f'check for the existence of the "{path}" file')
        with open (path, 'r'):return True
    except:return False

def readjson(path, category, name):
    try:   
        with open(path, "r") as fichier:
            data = json.load(fichier)
        writeinlog(f'read the "{path}" file in json format ("{category}": "{name}")')
        return data[category][name]
    except:return ""
    
def writejson(path, category, name, config):
    try:
        createconfigfile(path, '{}')
        with open(path, "r") as f:
            data = json.load(f)
        # Vérifier si la catégorie existe déjà
        if category not in data:
            data[category] = {}
        # Ajouter la nouvelle configuration à la catégorie
        data[category][name] = config
        with open(path, "w") as f:
            json.dump(data, f)
        writeinlog(f'write to the "{path}" file in json format ("{category}": "{name}" = "{config}")')
        return True
    except:
        return False


###########################################################################################
#                                                                                         #
# Discord Webhook # Discord Webhook # Discord Webhook # Discord Webhook # Discord Webhook #
#                                                                                         #
###########################################################################################

def sendwebhook(url=readjson('settings/webhook.json', 'defaultwebhook', 'url'), username=readjson('settings/webhook.json', 'defaultwebhook', 'name'), embedtitle="No title defined", embeddescription="No description defined",avatar=readjson('settings/webhook.json', 'defaultwebhook', 'profilepicture'), embedcolor=readjson('settings/webhook.json', 'defaultwebhook', 'color'), imageurl=readjson('settings/webhook.json', 'defaultwebhook', 'profilepicture'), author=readjson('settings/webhook.json', 'defaultwebhook', 'name'), authoricon=readjson('settings/webhook.json', 'defaultwebhook', 'profilepicture'), authorurl="https://dsc.gg/tgdgithub"):

    try:
        vintedfound = url
        data = {
            "username": username,
            "avatar_url": avatar,
            "embeds": [
                {
                    "title": embedtitle,
                    "description": embeddescription,
                    "color": int("0x" + embedcolor, 16),
                    "footer": {
                        "text": username,
                        "icon_url": avatar
                    },
                    "image": {
                        "url": imageurl
                    },
                    "author": {
                        "name": author,
                        "url": authorurl,
                        "icon_url": authoricon
                    },
                
                },
                
                ]
        }

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(vintedfound, json=data, headers=headers)

        if response.status_code == 204:
            writeinlog(f'The webhook "{username}" has been sent !')
            return True
        else:
            writeinlog(f'An error occurred while sending the webhook "{username}".')
            return False
    except: return False


    
############################################################################
#                                                                          #
# Vinted Scrap # Vinted Scrap # Vinted Scrap # Vinted Scrap # Vinted Scrap #
#                                                                          #
############################################################################

    
def scrap(url, product, type, webhook):
    try:
        ua = Headers().generate()  
        browser_option = ChromeOptions()
        browser_option.add_experimental_option("excludeSwitches", ["enable-logging"])
        if not readconfig('settings/settings.ini', 'settings', 'seewebbrowser') == "true":
            browser_option.add_argument('--headless')
        browser_option.add_argument('--disable-extensions')
        browser_option.add_argument('--incognito')
        browser_option.add_argument('--disable-gpu')
        browser_option.add_argument('--log-level=3')
        browser_option.add_argument(f'user-agent={ua}')
        browser_option.add_argument('--disable-notifications')
        browser_option.add_argument('--disable-popup-blocking')
        try:driver = webdriver.Chrome(options=browser_option)
        except:
            printerror('An error occurred while loading the driver, do you have the chrome browser? If yes, download the drivers related to your version of chrome: https://sites.google.com/chromium.org/driver/')
            writeinlog('An error occurred while loading the driver, do you have the chrome browser? If yes, download the drivers related to your version of chrome: https://sites.google.com/chromium.org/driver/')
        driver.get(url)
        driver.implicitly_wait(.2)
        # Vérification
        if type == 0:
            try:
                pageSource = driver.page_source
                soup = BeautifulSoup(pageSource, 'html.parser')

                list_items = soup.find_all("div", {"class": "feed-grid"})
                for item in list_items:

                    # Récupération du nom du vendeur
                    try:seller_name = soup.find('h4', {'class': 'web_ui__Text__text web_ui__Text__caption web_ui__Text__left'}).text.strip()
                    except:seller_name = "N/A"

                    # Récupération de la photo de profile du vendeur
                    try:
                        seller_picture = soup.find('div', {'class': 'web_ui__Image__image web_ui__Image__regular web_ui__Image__circle web_ui__Image__scaled web_ui__Image__cover'})
                        seller_picture = seller_picture.find('img')['src'].strip()
                    except:seller_picture = "N/A"

                    # Récupération de l'url du produit
                    try:product_url = soup.find('a', {'class': 'web_ui__ItemBox__overlay'})['href'].strip()
                    except:product_url = "N/A"

                    # Récupération du lien vers le profil du vendeur
                    try:seller_profile_link = soup.find('a', {'class': 'web_ui__Cell__cell web_ui__Cell__narrow web_ui__Cell__link'})['href'].strip()
                    except:seller_profile_link = "N/A"

                    # Récupération du lien vers l'image du produit
                    try:
                        product_image_link = soup.find('div', {'class': 'web_ui__ItemBox__image'})
                        product_image_link = product_image_link.find('img')['src'].strip()
                    except:product_image_link = "N/A"

                    # Récupération du titre du produit
                    try:product_title = soup.find('a', class_='web_ui__ItemBox__overlay')['title'].split(',')[0].strip()
                    except:product_title = "N/A"

                    # Récupération du prix du produit
                    try:product_price = soup.find('h3', {'class': 'web_ui__Text__text web_ui__Text__subtitle web_ui__Text__left web_ui__Text__amplified web_ui__Text__bold'}).text.strip()
                    except:product_price = "N/A"

                    # Récupération de la marque du produit
                    try:product_brand = soup.find('a', class_='web_ui__ItemBox__overlay')['title'].split(',')[3].split(':')[1].strip()
                    except:product_brand = "N/A"
                        
                    # Récupération du nombre de like
                    try:product_size = soup.find('a', class_='web_ui__ItemBox__overlay')['title'].split(',')[4].split(':')[1].strip()
                    except:product_size = "N/A"


                    createfolder('temp')
                    createconfigfile(f'temp/{product}.temp')
                    with open(f'temp/{product}.temp', 'r', encoding='utf-8') as f:
                        if not product_url in f.read():
                            with open(f'temp/{product}.temp', 'a', encoding='utf-8') as f:
                                f.write(f'{product_url}\n')

                                if readconfig('settings/settings.ini', 'settings', 'discord') == "true":
                                    if not webhook == "":
                                        sendwebhook(webhook, readjson('settings/webhook.json', 'defaultwebhook', 'name'), product_title, f"**💰 Price:** ```{product_price}```\n**📑 Brand:** ```{product_brand}```\n**🎈 Size:** ```{product_size}```\n**Url:** {product_url}",embedcolor=readjson('settings/webhook.json', 'defaultwebhook', 'color'), author=seller_name, authorurl=seller_profile_link, authoricon=seller_picture, imageurl=product_image_link, avatar=readjson('settings/webhook.json', 'defaultwebhook', 'profilepicture') )

                                print(f"\n{colors('cyan')}Product:{colors()} {product}")
                                print(f"{colors('cyan')}URL:{colors()}", url)
                                print(f"{colors('cyan')}Seller's name:{colors()}", seller_name)
                                print(f"{colors('cyan')}Seller's profile picture:{colors()}", seller_picture)
                                print(f"{colors('cyan')}Product URL:{colors()}", product_url)
                                print(f"{colors('cyan')}Link to the seller's profile:{colors()}", seller_profile_link)
                                print(f"{colors('cyan')}Link to product image:{colors()}", product_image_link)
                                print(f"{colors('cyan')}Product title:{colors()}", product_title)
                                print(f"{colors('cyan')}Product price:{colors()}", product_price)
                                print(f"{colors('cyan')}Product brand:{colors()}", product_brand)
                                print(f"{colors('cyan')}Product size:{colors()}", product_size)
                                writeinlog(f'A new product has been tracked "{product_url}"')
                                return [True, url, seller_name, seller_picture, product_url, seller_profile_link, product_image_link, product_title, product_price, product_brand, product_size]
                        else:
                            driver.close()
                            return [None]
                    
                                
            except:return [False]
    except: return [False]





############################################################################################
#                                                                                          #
# Logs # Logs # Logs # Logs # Logs # Logs # Logs # Logs # Logs # Logs # Logs # Logs # Logs #
#                                                                                          #
############################################################################################

def writeinlog(text):
    datenow = datetime.datetime.now()
    datenow = datenow.strftime("%Y-%m-%d %H-%M-%S")
    createfolder('logs', False)
    with open(f'logs/{date}', 'a', encoding='utf-8') as f:
        f.write(f'{datenow} | {text}\n')
    if readconfig('settings/settings.ini', 'settings', 'logsincmd', False) == "true":
        print(f'{datenow} | {text}')

