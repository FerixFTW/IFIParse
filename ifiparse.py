#########
#
#   IFI PARSE
#
#   Author: FerixFTW
#   Desc: Take Capital.com CSV Trades report and parse out the
#         info needed for Slovene tax filings
#   Date: 24/12/2021
#
#########

import re
import sys
import time
import random
import requests
from bs4 import BeautifulSoup

try:
    num_lines = sum(1 for line in open(sys.argv[1]))
except:
    print("Pass file as argument to script.")
    exit()

file = open(sys.argv[1],"r")
writeFile = open("tradesReport.txt","w")

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
         "Language":"en-GB,en;q=0.9",
         "Encoding":"gzip, deflate"}

file.readline() #Skip the header line
counter = 0
winner = 0
loser = 0
loss = 0
profit = 0
dateComparison = 0
dateVariable = 0
exRate = 0

#Functions

def spacer():
    return("-----------------------------------------------|")

def getRate(date):
    time.sleep(15+random.randint(0,15))
    convertedDate = date[8:10]+"."+date[5:7]+"."+date[0:4]
    url = 'https://www.bsi.si/statistika/devizni-tecaji-in-plemenite-kovine/dnevna-tecajnica-referencni-tecaji-ecb/'+convertedDate
    page = requests.get(url,headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    exRate = str(soup.findAll("td")[4].text)
    exRate = exRate.replace(",",".")
    return float(exRate)

#Body
while(counter != num_lines-1):
    #Convert csv data to array
    parsedData = re.findall('"([^"]*)"',file.readline())
    #Extract data, assign varnames
    try:
        marketInfo = parsedData[7]
        quantity = parsedData[15]
        openClosePrice = parsedData[17]
        openCloseStatus = parsedData[27]
        USD = parsedData[29]
        EUR = parsedData[31]
        timestamp = parsedData[39]
    except:
        marketInfo = parsedData[4]
        quantity = parsedData[8]
        openClosePrice = parsedData[9]
        openCloseStatus = parsedData[14]
        USD = parsedData[15]
        EUR = parsedData[16]
        timestamp = parsedData[20]
    ####Output beautifying#####
    #Long or short determination

    if(counter==0 or float(EUR)!=0):
        positionType = "CLOSE     "
    else:
        positionType = "OPEN      "
    if(positionType == "OPEN      " and float(quantity)<0):
        positionType = "OPEN SHORT"
    #Quantity padding and value roundings

    EUR = format(float(EUR),'.2f')
    quantity = format(float(quantity),'.2f')
    openClosePrice = format(float(openClosePrice),'.2f')
    if(float(quantity)>0):
        quantity = "+"+quantity
    #EUR omission when 0, padding and counting

    if(float(EUR)>0):
        EUR = "+"+EUR
        winner += 1
        profit += float(EUR)
    elif(float(EUR)<0):
        loser += 1
        loss += float(EUR)
    if(EUR=="0.00"):
        EUR = "  |"
    #Date and exchange rate handling

    dateVariable = timestamp[:10]
    if(dateComparison != dateVariable):
        dateComparison = dateVariable
        #Terminal output
        print(spacer())
        print(dateComparison)
        exRate = getRate(str(dateComparison))
        print("Exchange rate on day: "+str(exRate))
        print(spacer())
        #tradesReport.txt output
        writeFile.write(spacer()+"\n")
        writeFile.write(dateComparison+"\n")
        writeFile.write("Exchange rate on day: "+str(exRate)+"\n")
        writeFile.write(spacer()+"\n")
    ###########################

    #Print data to terminal
    print(positionType," ",marketInfo," ",quantity," ",format((float(openClosePrice)/exRate),".2f")," ",EUR)
    #Print data to file tradesReport.txt
    writeFile.write(positionType+" "+marketInfo+" "+quantity+" "+format((float(openClosePrice)/exRate),".2f")+" "+EUR+"\n")
    #Counter of trade pairs (real number of trades is the final counter value divided by 2)
    counter += 1

#Output summary to terminal
print(spacer())
print(winner+loser," Trades   | ", winner, " winners  | ", loser," losers     |")
print(format(float(profit),'.2f')," profit|  and ",format(float(loss),'.2f')," losses             |")
print(spacer())
print("Running P&L: ", format(float(profit+loss),'.2f'))
print(spacer())

#Output summary to tradesReport.txt
writeFile.write(spacer()+"\n")
writeFile.write(str(winner+loser)+" Trades   | "+str(winner)+" winners      |  "+str(loser)+" losers     |"+"\n")
writeFile.write(str(format(float(profit),'.2f'))+" profit| and "+str(format(float(loss),'.2f'))+" losses                 |"+"\n")
writeFile.write(spacer()+"\n")
writeFile.write("Running P&L: "+str(format(float(profit+loss),'.2f'))+"\n")
writeFile.write(spacer()+"\n")
