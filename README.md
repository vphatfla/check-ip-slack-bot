# check-ip-slack-bot
1. Follow Slack tutorial to create Slack app. https://api.slack.com/start/building/bolt-python
You need to create a Slack workspace first and then create the app, set name of bot = bot1

2. Set chat:write, app_mentions:read, groups:history, im:history in bot token scopes.

3. Install app, save bot user oauth token. 

4. install python virtual enviroment:
```
python3 -m venv .venv
source .venv/bin/activate
```

5. Install dependencies in requirements.txt
```
pip install -r requirement.txt
```

6. Get your user oauth token, signing secret, and APIKEY from Virustotal, then set:
```
export SLACK_SIGNING_SECRET = <your signing secret>
export SLACK_BOT_TOKEN = <your bot token>
export API_KEY = <your virus total API KEY>
```
then run
```
python3 app.py
>>> Bolt app is running! (development server)
```

7. Install ngrok
```
https://ngrok.com/download
```

8. Connect account with ngrok by follow the intrusction on ngrok website

9. Fire up ngrok
```
ngrok http 3000
```

10. Enable Event Subscriptions and copy/paste the forwarding url from the terminal of ngrok into the Request URL.

11. Go to Subscribe to bot events and enable message.channel. then Save

12. Enjoy!
