from connect import connect
import random

class Message:
    """Represent IRC message"""

    def __init__(self, buf):
        if ("PING" not in buf and "PRIVMSG" not in buf):
            self.sender = self.contents = None
        else:
            self.sender   = buf.split('!')[0].strip(':')
            self.contents = buf.split(':')[-1].strip()

    def is_ping(self):
        return self.sender.startswith("PING")

if __name__ == "__main__":
    s = connect()

    while(True):
        # Call recv()
        readbuffer = s.recv(1024).decode("UTF-8", errors = "ignore")
        for msg in readbuffer.split('\n'):
            msg = Message(msg)

            # Ignore blank messages
            if (msg.sender is None):
                continue

            print("SENDER: {} CONTENTS: {}\n".format(
                msg.sender, msg.contents))

            if (msg.is_ping()):
                print("Received a ping! Pong-ing...")
                s.send(bytes("PONG tmi.twitch.tv\r\n", "UTF-8"))



