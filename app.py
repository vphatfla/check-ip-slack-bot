from logging import exception
import os
from re import A
import ipaddress
# Use the package we installed
from slack_bolt import App
from handlingRes import handlingRes
from request import *
from processData import *
# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

# validation for IP address
def valid_ip(address):
    
    try:
        ip = ipaddress.ip_address(address)
        return True
    except:
        return False

# Add functionality here
# @app.event("app_home_opened") etc
@app.message("bot1-help")
def response_help(message, say):
  str1 = f"Hello <@{message['user']}>, I am Bot1 beta, created by Van. \nSlash command is - \n"
  str1 += "To get summary data of an IP address, type in: -summmary-<IPv4 address>. \n"
  str1 += "To get full data of an IP address, type in: -full-<IPv4 address>.\n"
  str1 +="IPv4 address must be in format x.x.x.x with x<=255, example: 255.255.255.255\n"
  str1 += "Please only let me join particular channels that you want to check ip addresses only, otherwise I will be annoying replying everything you say.\n"
  str1 += "This bot is only for demonstrating purposes. Still have rooms for developments."
  say(str1)

# Listens for messages and verify IP address
@app.message("")
def ask_who(message, say):
  # get whole command
  m = message['text']

  #verify slash -
  if (m[0] == "-"): 
    #verify -summary or -full
    command = ""
    ipInput = ""
    if (m[0:9] == "-summary-"): 
      command = "s"
      ipInput = m[9:]
    elif (m[0:6] == "-full-"):
      command = "f"
      ipInput = m[6:]
    else:
      say('Invalid command, type bot1-help for more information')
      return
    
    # validate ipInput
    if (not valid_ip(ipInput)):
      say('Invalid IP address, type bot1-help for more information')
    else:
      handlingRes(command, ipInput, say)
  else:
    return



# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))