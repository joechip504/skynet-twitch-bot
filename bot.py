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

            if (msg.contents == "Open the pod bay doors"):
                s.send(bytes("PRIVMSG #joechip504 :I'm sorry,\
                             I can't let you do that.\r\n", "UTF-8"))

            if (str(msg.sender) == "falcons52"):
                s.send(bytes("Go away", "UTF-8"))

            if (msg.contents[0] == "!"):
                command = msg.contents.split(" ")[0].strip("!").lower()
                try:
                    args = msg.contents.split(" ")[1].lower()
                except IndexError:
                    print("There were no arguments")

                    
                if (command == "test"):
                    reply = "PRIVMSG " + "#joechip504" + " :Test worked!\r\n"
                    s.send(bytes(reply, "UTF-8"))

                    
                elif(command == "roll"):
                    print("Rolling " + args)
                    results = []
                    die = int(args.split("d")[0])
                    size = int(args.split("d")[1])
                    for i in range(0, die):
                        results.append(random.randint(1,size))
                    resultsToPrint = ", ".join(str(e) for e in results)
                    reply = "PRIVMSG #joechip504 :" + resultsToPrint + "\r\n"
                    s.send(bytes(reply, "UTF-8"))


                #elif (command == 
