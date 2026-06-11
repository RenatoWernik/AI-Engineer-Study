messages = ["hi","how are you?","great to see you"]
sent_messages = []
def display_messages(msg_list):
    for msg in msg_list:
        print(msg.title())

display_messages(messages)


def send_messages(msg_list,sent_msg_list):
    while msg_list:
        current_msg = msg_list.pop()
        print(f"Sending the current message: {current_msg.title()}")
        sent_msg_list.append(current_msg)
    print(f"The following messages have been sent: {sent_msg_list}")

send_messages(messages,sent_messages)
print(messages)
print(sent_messages)
        
