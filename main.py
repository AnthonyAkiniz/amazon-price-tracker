#########################################################################################
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
# * ################################################################################# * #
# * #                             Amazon Price Tracker                              # * #
# * #                          project by: Anthony Akiniz                           # * #
# * #                          github.com/anthonyakiniz                             # * #
# * ################################################################################# * #
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
#########################################################################################
# Info:                                                                                 #
# Sends e-mail alert if Amazon product drops below a certain price.                     #
# Amazon has strong bot blocking systems in place that may require captcha if you ping  #
# their servers too often so some use CamelCamelCamel.com Amazon product URLs instead.  #
#                                                                                       #
# Requirements:                                                                         #
# pip install beautifulsoup4                                                            #
# pip install --upgrade lxml                                                            #
#                                                                                       #
# Google Gmail Account:                                                                 #
# Enable 2-Step Verification on your Gmail Account (required to get an App Password)    #
# Gmail App Password (lets you sign in with apps like Python scripts)                   #
# Gmail app password setup: https://myaccount.google.com/apppasswords                   #
# documentation: https://support.google.com/accounts/answer/185833                      #
#                                                                                       #
# Guide:                                                                                #
# 1. Update the product URL below that you want to track.                               #
# 2. Update the buy price below. An email alert will be sent if drops below the amount. #
#    For initial test, place it above the current price to verify it sends an email.    #
# 3. Update your Gmail address and Gmail app password below.                            #
# 2. Launch by clicking run button in top right in VSCode or: py -3 main.py             #
#########################################################################################

import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

# price is set above current price to verify e-mail alert is sent
# lower it to desired price after confirmed e-mail alert is sent
BUY_PRICE = 1500

URL = "https://www.amazon.com/Apple-MacBook-13-inch-256GB-Storage/dp/B08N5KWB9H/"

# This is your browser request headers data that Amazon uses to tell what browser you're on.
# I am on Chrome in the US, Version 102.0.5005.115 (Official Build) (64-bit).
# It doesn't have to match your browser but just displays the bot like it's a browser.
# You can use mine below or use your own by getting your browser data here: http://myhttpheader.com
header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}

response = requests.get(URL, headers=header)
soup = BeautifulSoup(response.content, "lxml")
find_price = soup.find("span", class_="a-price-whole")
price_as_float = float(find_price.text.split("$")[0])
# print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
# print(title)

if price_as_float < BUY_PRICE:
    message = f"{title} is now ${price_as_float}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(
            user="YOUR GMAIL ADDRESS", password="YOUR GMAIL APP PASSWORD")
        connection.sendmail(
            from_addr="SENDER EMAIL",
            to_addrs="RECEIVER EMAIL",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode(
                "utf-8")
        )
