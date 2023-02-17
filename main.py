import telegram

# Set up the Telegram bot using your bot's API token
bot = telegram.Bot(token='5856420569:AAGqIr79LKzaxMcG6ElzyewDLDtfxjfRnOs')

# Define a function to send a message
def send_message(chat_id, text):
    bot.send_message(chat_id=chat_id, text=text)

# Define a function to make a request to the Telegram API
def make_request(method, params=None):
    return bot.request(method, params)

# Example usage
chat_id = 123456789 # Replace with the ID of the chat you want to send a message to
message_text = "Hello, world!"
send_message(chat_id, message_text)

# Make a request to the Telegram API
response = make_request("getUpdates")
print(response)
