from logging import exception
import os
from re import A
import ipaddress
# Use the package we installed
from slack_bolt import App
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
  str1 = f"Hello <@{message['user']}>, I am Bot1 beta, created by Van. \nI do not have slash/prefix command, hence I will listen to any thing to type and verify whether they are an IP or not. \n"
  str1 += "To get data of an IP address, just type in an address in IPv4. \n"
  str1 += "Please only let me join particular channels that you want to check ip addresses only, otherwise I will be annoying replying everything you say.\n"
  str1 += "This bot is only for demonstrating purposes. Still have rooms for developments."
  say(str1)

# Listens for messages and verify IP address
@app.message("")
def ask_who(message, say):
  # get IP param as ipInput
  ipInput = message['text']

  # validating IP address for both IPv4 and IPv6
  if (valid_ip(ipInput)): 
    say('Valid IP address')
    try:
      #responseJSON : json data from api res with stringInput
      responseJSON = infoIP(ipInput)

      #process the json data
      processedData = processData(responseJSON, ipInput)
      
      #get summaryData from processedData
      saySummaryData = processedData[0]

      #send a message regarding the data
      say(f"{saySummaryData}")
      
    except Exception as e:
      say("Sorry, something went wrong")
  else: say('UNVALID IP address, type bot1-help for more information')

@app.event("app_home_opened")
def update_home_tab(client, event, logger):
  
  try:
    # views.publish is the method that your app uses to push a view to the Home tab
    client.views_publish(
      # the user that opened your app's app home
      user_id=event["user"],
      # the view object that appears in the app home
      view={
        "type": "home",
        "callback_id": "home_view",

        # body of the view
        "blocks": [
          {
            "type": "section",
            "text": {
              "type": "mrkdwn",
              "text": "*Welcome to your _App's Home_* :tada:"
            }
          },
          {
            "type": "divider"
          },
          {
            "type": "section",
            "text": {
              "type": "mrkdwn",
              "text": "This button won't do much for now but you can set up a listener for it using the `actions()` method and passing its unique `action_id`. See an example in the `examples` folder within your Bolt app."
            }
          },
          {
            "type": "actions",
            "elements": [
              {
                "type": "button",
                "text": {
                  "type": "plain_text",
                  "text": "Click me!"
                }
              }
            ]
          }
        ]
      }
    )
  
  except Exception as e:
    logger.error(f"Error publishing home tab: {e}")

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))