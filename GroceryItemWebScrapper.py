
# coding: utf-8

# In[2]:

from urllib.request import urlopen as uReq                     #importing urllib and BeautifulSoup 
from bs4 import BeautifulSoup as soup


# In[5]:

my_url = 'https://www.aldi-nord.de/produkte/schnelle-kueche-fix-lecker.html'   #This is the URL of the site that I want to scrape
uClient = uReq(my_url)                                                 #This is Python requesting to go to that url. Notice that I called uReq which is urlopen. see first line of code
page_html=uClient.read()                                            #Python is reading all the data in the website which is written in html
uClient.close()
page_soup=soup(page_html,"html.parser")                                #I created a BeautifulSoup object to make life simpler


# In[6]:

containers=page_soup.findAll("div",{"class":"col-xs-6 col-sm-4 col-lg-3"})   #I find all the divs in the html which have the said class. This is how I find different fields for my data file; Price, quantity etc. Basically whenever you see a findAll what it is doing is that it is searching the html for all classes or spans or whatever tag I specify with an unique identifier I specify after that
container = containers[0]
container.findAll("div",{"class":"mod-article-tile__content"})


# In[26]:

unit=container.find_all("span",{"class":"price__unit"}) #See previous block. You should really check the site out to better understand things
unit[0].text.strip()
base=container.findAll("span",{"class":"price__base"})


# In[24]:

filename = "Products.csv" #I create a file to save all my data in
f=open(filename,"w")
headers = "Product_Name, Brand, Price in Euros,Available Quantity,Base Price\n"
f.write(headers)
for container in containers:   #I loop through all the data sets and print them onto my created file
    Product_Name = container.div.div.img["alt"]
    title_container=container.findAll("p",{"class":"mod-article-tile__brand"})
    brand = title_container[0].text.strip()
    price=container.findAll("span",{"class":"price__main"})
    price = price[0].text.strip()
    unit=container.find_all("span",{"class":"price__unit"})
    unit=unit[0].text.strip()
    base=container.findAll("span",{"class":"price__base"})
    if base==[]:
        b_price="NA"
    else:
        base=container.findAll("span",{"class":"price__base"})
        b_price=base[0].text
        
    
   
    
        
        
    f.write(Product_Name + "," + brand + "," + price+ "," +unit+","+b_price+"\n")
     
f.close() #You must close the file to be able to open it again


# In[ ]:




# In[ ]:



