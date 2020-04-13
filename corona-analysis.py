import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
my_url="https://www.medtalks.in/live-corona-counter-india"
uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()
page_soup=soup(page_html,"html.parser")
print("CORONA Analysis")
master=page_soup.findAll("td")
n=int((len(master)/6)-1)
#webscracping deaths according to states
s_cured=master[5::6]
state_cured=[]
for i in range(0,n):
    ele=int(s_cured[i].text)
    state_cured.append(ele)
#webscracping deaths according to states
s_deaths=master[2::6]
state_deaths=[]
for i in range(0,n):
    ele=int(s_deaths[i].text)
    state_deaths.append(ele)
print("Total Confirmed cases in India are: ",master[-5].text)
print("\nTotal Deaths in India are: ",master[-4].text)
print("\nTotal Cured people in India are: ",master[-1].text)
print("\n")
#calculating confirmed cases in each state
state=master[1::6]
state_confir=[]
#a list with commas
state_con=[]
for i in range(0,n):
    ele=state[i].text
    state_con.append(ele)

for i in range(len(state_con)):
    if len(state_con[i])>3:
        s=state_con[i]
        d=""
        c=[]
        for i in range(len(s)):
            if s[i]!=",":
                d=d+s[i]
                c.append(d)
        state_confir.append(c[-1])
    else:
        state_confir.append(state_con[i])
state_confirmed=[]
for i in state_confir:
    stat=int(i)
    state_confirmed.append(stat)
#print(state_confirmed)
#webscraping name of each state
statelist=[]
for i in range(0,n):
    ele=master[i+i*5].text
    statelist.append(ele)
#dictionary for the names and population 
state_dict={"Maharashtra ":112374333,
            "Tamil Nadu ":72147030,
            "Delhi  ":16787941,
            "Kerala ":33406061,
            "Telangna  ":35003674,
            "Uttar Pradesh ":199812341,
            "Rajasthan ":68548437,
            "Andra Pradesh ":49577103,
            "Madya Pradesh ":72626809,
            "Karnataka ":61095297,
            "Gujarat ":60439692,
            "Jammu and Kashmir ":12267032,
            "Haryana ":25351462,
            "Punjab ":27743338,
            "West Bengal ":91276115,
            "Bihar ":104099452,
            "Assam ":31169272,
            "Uttarakhand ":10086292,
            "Orissa ":46143782,
            "Chandigarh ":1055450,
            "Ladakh ":274289,
            "Andaman and Nicobar Islands ":380581,
            "Chhattisgarh ":25545198,
            "Goa ":1458545,
            "Himachal Pradesh ":6864602,
            "Pondicherry ":1394467,
            "Jharkhand ":32988134,
            "Manipur ":2855794,
            "Mizoram ":1091014,
            "Dadar and Nagar Haveli ":343709,
            "Tripura ":1871867,
            "Sikkim ":610577,
            "Arunachal Pradesh ":1383727,
            "Nagaland ":1978502,
            "Meghalaya ":2966889,
            "Lakshadweep ":64473}
#calculating the maximum and minimum confirmed states
max_state=max(state_confirmed)
min_state=min(state_confirmed)
for i in range(0,n):
    if state_confirmed[i]==max_state:
        print("Maximum confirmed patients are in state : ",statelist[i]," with ",max_state," cases." )
    if state_confirmed[i]==min_state:
        print("Minimum confirmed patients are in state : ",statelist[i]," with ",min_state," cases.")
#removing hindi names
eng_states=[]
for i in range(len(statelist)):
    s=statelist[i].split("(")
    eng_states.append(s[0])
#list for total populaton of the states
#arranging statewise population
population=[]
for i in eng_states:
    s=i
    for j in range(len(state_dict)):
        if s in state_dict:
            ele=state_dict[i]
            population.append(ele)
            break

ratios=[]
#calculating ratio        
print("\nPercentage of confirmed cases according to the population\n")              
for i in range(0,n):
    ratio=(state_confirmed[i]/population[i])*100
    ratios.append(ratio)

#making tables using pandas library
new_data={"State name":eng_states,"Confirmed":state_confirmed,"Deaths":state_deaths,"Cured":state_cured}
df=pd.DataFrame.from_dict(new_data)
print(df)
print("\n\n")
ratios_data={"State name":eng_states,"Percentage of Confirmed cases":ratios}
md=pd.DataFrame.from_dict(ratios_data)
print(md)
print("\n\n")
#calculating maxratio
max_ratio=max(ratios)
for i in range(len(eng_states)):
    if max_ratio==ratios[i]:
        print("\n\n\n",statelist[i]," has the maximum percentage of confirmed cases (according to population).")
#printing graph
#making space for graph
fig=plt.figure(figsize=(9,6))
ax1=plt.subplot(111)
#giving arrays as input to the graph
ax1.barh(df['State name'],df['Confirmed'])
#giving count at the end of the graph
for pY,pX in enumerate(df.Confirmed):
    ax1.annotate(pX, xy=(pX,pY))
#displaying the graph
plt.show()





