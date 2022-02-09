from bs4 import BeautifulSoup
import requests
import smtplib

my_email = "sina_eshrati@yahoo.com"
my_password = "euolagjhjfqaiddm"

amazon_url = "https://www.amazon.com/Sceptre-DisplayPort-Edge-Less-FreeSync-C275B-1858RN/dp/B089V2R9WW/ref=sr_1_6?crid=1WMICVUTD8DQL&dchild=1&keywords=curved+computer+monitor&qid=1622557760&sprefix=cur%2Caps%2C341&sr=8-6"
headers = {
    "Accept-Language": "en-US,en;q=0.9,la;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
}
response = requests.get(url=amazon_url, headers=headers)
content = response.text

soup = BeautifulSoup(content, "html.parser")
price = soup.select_one(".priceBlockBuyingPriceString").getText()
product = soup.select_one(".product-title-word-break").getText()

if float(price.split("$")[1]) < 300:
    with smtplib.SMTP_SSL("smtp.mail.yahoo.com") as connection:
        connection.login(my_email, my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="eshratisina@gmail.com",
                            msg=f"Subject:Low Price Alert!\n\n{product}\n{price}\n{amazon_url}")
