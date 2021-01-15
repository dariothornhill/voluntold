import os
from pathlib import Path
from dotenv import load_dotenv

from slack import WebClient
from slack.errors import SlackApiError

from voluntold.chat_client import ChatClient

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class SlackClient(ChatClient):
    
    ''' This is the base class for our chat application client interfaces '''
    def __init__(self):
        # TODO setup persistance, connect to some db
        # mark as slack chat interface
        self.chat_interface = 'slack'
    
    def connect(self):
        self.client = WebClient(token=os.environ['SLACK_API_TOKEN']) #  TODO find out if I need to manage this differently per workspace
    
    def join(self, channel):
        # self.client.join(channel)
        pass
