import json
from json2html import *
import webbrowser
import os
# func to create html file for data json
def htmlFile(data):
    formatted_data = json2html.convert(data)
    tempHTML = open("./tempHTML/temp.html", "w")
    tempHTML.write(formatted_data)
    tempHTML.close()
    return

    
def processData(jsonData, ipAddress):
    #get data based on attribute of json data res
    allData = json.loads(jsonData)["data"]
    attributeData = allData["attributes"]
    typeData = allData["type"]
    idData = allData["id"]
    linksData = allData["links"] 
    #wrtie the temp.html with data from allData
    htmlFile(allData)
    # create url link to open local html file, note: not the optimal way to do it
    urlLink = 'file://' + os.getcwd() + "/tempHTML/temp.html"
    
    #dict for summary data
    summaryDataDict = {
        "IP address" : ipAddress,
        "Owner": ("N/A") if ("as_owner" not in attributeData) else attributeData["as_owner"],
        
        "Country" : ("N/A") if ("country" not in attributeData) else attributeData["country"],
        "Continent": ("N/A") if ("continent" not in attributeData) else attributeData["continent"],
        "Links for full data (copy and paste on the browser)": urlLink,
    }

    #conver dict to string STRI summary
    stri = "Summary data \n"
    for key in summaryDataDict.keys():
        stri += str(key) + ": " + str(summaryDataDict[key]) + "\n"
        
    return stri, " 1"

export = processData

