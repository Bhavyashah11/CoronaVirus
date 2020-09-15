import requests
from bs4 import BeautifulSoup

url="https://www.worldometers.info/coronavirus/"
r=requests.get(url)
s=BeautifulSoup(r.text,"html.parser")
data=s.find_all("div",class_="maincounter-number")
inp=0
while(True):
    
    try:
        country=input("Enter the country name:")
        country=country.split()
        country="-".join(country)
        url1="https://www.worldometers.info/coronavirus/country/"+country+"/"
        c=requests.get(url1)
        si=BeautifulSoup(c.text,"html.parser")
        data1=si.find_all("div",class_="maincounter-number")
    except Exception as e:
        print("Error "+e)
    #print(data)
    print("Total cases around the world: ",data[0].text.strip())
    print("Total Deaths around the world: ",data[1].text.strip())
    print("Total Recovered around the world: ",data[2].text.strip())
    try:
        country=country.capitalize()
        print("Total cases in "+country +": "+data1[0].text.strip())
        print("Total Deaths in  "+country+": "+data1[1].text.strip())
        print("Total Recovered in "+country+": "+data1[2].text.strip())
    except Exception as e:
        print("Error in finding the country please try again ")
    print("\n")
    inp=int(input("--------Press 1 to exit or any other number to continue-------- \n"))
    if(inp==1):
        break
