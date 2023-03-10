from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import SendMessageRequest

class TelegramBot:
    def __init__(self, api_id, api_hash, phone_number, username):
        self.api_id = api_id
        self.api_hash = api_hash
        self.phone_number = phone_number
        self.username = username

    def connect(self):
        self.client = TelegramClient(self.username, self.api_id, self.api_hash)
        self.client.connect()
        if not self.client.is_user_authorized():
            self.client.send_code_request(self.phone_number)
            self.client.sign_in(self.phone_number, input('Enter the code: '))

    def send_message(self, channel_name, message):
        channel = self.client.get_entity(channel_name)
        full_channel = self.client(GetFullChannelRequest(channel))
        self.client(SendMessageRequest(
            peer=full_channel.chat_id,
            message=message
        ))
