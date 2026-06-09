messages = ["hello","how are you?","great to see you"]
def show_messages(msgs):
    print("Here are the messages: ")
    for msg in messages:
        print(msg)


def send_messages(show_msgs,sent_msgs):
    show_messages(messages)
    sent_messages = messages[:]


send_messages(show_messages,)