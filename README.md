![Vinted Bot by TheGrayDream](https://user-images.githubusercontent.com/125685786/224554572-565b189a-6c3f-4539-805b-ffaab7bf37a5.png)![Vinted Bot by TheGrayDream1](https://user-images.githubusercontent.com/125685786/224557401-39498704-92a7-49c3-a5e1-6dd6a4194c7e.png)

# Vinted-Bot
Vinted bot that works with discord webhook

This vinted bot is complete, it allows you to choose several products to track, you can choose the price, the currency and other parameters, it is very easy to use.

# How to install it
first of all you will need to run the bat file "install.bat", it will install all the modules necessary for the functioning of the vinted bot, once you have installed it you will need to install chrome, if it is already installed you will need to go to https://sites.google.com/chromium.org/driver/ and install the same version as your chrome browser (to see the version "chrome://version"), once you have downloaded it you will need to extract it and place chromedriver.exe in the same folder as main.py

# How to use it
To add a product you will have to go to (Product > Add a product) once in this page you can add the webhook, the product, the price and the currency)

To delete a product you will have to go to (Product > Delete a product) once in this page you can delete the product corresponding to the number displayed on the left of the name.

To modify a product you will have to go to (Product > Edit a product > product name) once in this page you can modify all the parameters of the product.

To modify the parameters of the webhook and add a default webhook you will have to go in (Discord Webhook), once in this page you can modify the name of the bot, the default url, the profile picture, the color of the embed (when you will create a product the default url will be proposed, you can put another webhook it will work !)

To modify the parameters of the vinted bot you will have to go in (Settings), once in this page you can modify the integrality of the parameters of the vinted bot (more parameters will arrive)

To launch the bot you will have to go to (Run, Need to have at least 1 product!), the bot will then start to retrieve the first ad that it will store in a temporary file in the temp folder to not display the same product, if it detects a new product it will send a webhook.
