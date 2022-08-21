
from processData import processData
from request import infoIP


def handlingRes(command, ipInput,say):
    say('Valid IP address')
    try:
      #responseJSON : json data from api res with stringInput
      responseJSON = infoIP(ipInput)

      #process the json data
      processedData = processData(responseJSON, ipInput)
      print('here')
      #get data to say from processedData
      if (command == 's'): sayData = processedData[0]()
      elif (command=='f'): sayData=processedData[1]()

      #send a message regarding the data
      say(f"{sayData}")
      
    except Exception as e:
      say("Sorry, something went wrong")
    return

export=handlingRes