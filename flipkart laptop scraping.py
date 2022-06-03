
from bs4 import *
from urllib.request import urlopen as ureq
uclient=ureq("https://www.flipkart.com/search?q=apple%20iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
page_html=uclient.read()
uclient.close()
soup=BeautifulSoup(page_html,"html.parser")
containers=soup.find_all("div",class_="_2kHMtA")

filename= "products.csv"
f=open(filename,"w",encoding='utf-8')
headers="product_name,price,ratings\n"
f.write(headers)
for container in containers:

    name_container = container.find("div", class_="_4rR01T")
    name=name_container.get_text()

    price_container = container.find("div", class_="_30jeq3 _1_WHN1")
    price=price_container.get_text()

    rating_container= container.find("div", class_="_3LWZlK")
    rating=rating_container.get_text()

    split_price=price.split(',')
    final_price=split_price[0]+split_price[1]
    print(name.replace(",","|")+","+final_price+","+rating)
    f.write(name.replace(",", "|") + "," + final_price + "," + rating + '\n')

f.close()


