import time
from fbchat import Client
from fbchat.models import *

# Replace the following variables with your own information
username = "your_facebook_username"
password = "your_facebook_password"
friend_name = "the_name_of_the_person_you_want_to_message"
message = "I love you"

# Log in to Facebook Messenger
client = Client(username, password)

# Get the user ID of the person you want to message
users = client.searchForUsers(friend_name)
friend = users[0]
friend_id = friend.uid

# Send the message 100 times with a delay of 1 second between each message
for i in range(100):
    client.send(Message(text=message), thread_id=friend_id, thread_type=ThreadType.USER)
    print(f"Message {i+1} sent successfully!")
    time.sleep(1)

# Log out of Facebook Messenger
client.logout()
