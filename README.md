# Amazon Price Tracker
Sends e-mail alert if Amazon product drops below a certain price. Amazon has strong bot blocking systems in place that may require captcha if you ping their servers too often so some use CamelCamelCamel.com Amazon product URLs instead.

# Requirements
pip install beautifulsoup4<br>
pip install --upgrade lxml<br>

# Google Gmail Account
Enable 2-Step Verification on your Gmail Account (required to get an App Password)<br>
Gmail App Password (lets you sign in with apps like Python scripts)<br>
Gmail app password setup: https://myaccount.google.com/apppasswords<br>
documentation: https://support.google.com/accounts/answer/185833<br>

# Guide
1. Update the product URL in the code that you want to track.<br>
2. Update the buy price. An email alert will be sent if drops below the amount.<br>
   For initial test, place it above the current price to verify it sends an email.<br>
3. Update your Gmail address and Gmail app password in code.<br>
4. Launch by clicking run button in top right in VSCode or: py -3 main.py<br>
