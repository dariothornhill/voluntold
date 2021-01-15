from flask import Flask
from voluntold.slack_client import SlackClient

if __name__ == "__main__":
    slack = SlackClient()
    slack.connect()
    slack.client.chat_postMessage(channel='#bot-test', text="Guess who's back!")
    app.run(debug=True)
    