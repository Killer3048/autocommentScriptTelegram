import time
import config
from telegram_bot import TelegramBot

class PostMonitor:
    def __init__(self, channels, bot):
        self.channels = channels
        self.bot = bot
        self.seen_posts = set()

    def monitor(self):
        for channel in self.channels:
            posts = self.bot.client.get_messages(channel, limit=10)
            for post in posts:
                if post.id not in self.seen_posts:
                    self.seen_posts.add(post.id)
                    self.bot.send_message(channel, "This is an automatic comment.")
        time.sleep(10)

if __name__ == "__main__":
    bot = TelegramBot(config.API_ID, config.API_HASH, config.PHONE_NUMBER, config.USERNAME)
    bot.connect()

    monitor = PostMonitor(config.CHANNELS, bot)
    while True:
        monitor.monitor()
