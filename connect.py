import socket

# ============================================================================
SETTINGS_FILE = 'settings.txt'
API_KEY_FILE  = '.apikey.txt'
# ============================================================================

def parse( f_settings, f_api ):
    """ 
    Parse files storing bot information. Return dictionary of the form:
    d = { HOST : "irc.twitch.tv", PORT : 6667, NICK : "skynet" ... }
    """
    d = {}
    for line in open( f_settings ):

        try:
            k, v = line.split()[0], line.split()[1]

            if (v.isdigit()):
                v = int(v)

            d[k] = v

        except:
            continue

    api_key = open(f_api).read().strip()
    d['OAUTH'] = api_key

    return d

def connect():
    """
    After filling out settings.txt and .apikey.txt, call connect() to
    connect to chat. connect() returns a socket.
    """

    # Grab info from setup files
    d = parse( SETTINGS_FILE, API_KEY_FILE )
    print(d)

    s = socket.socket()

    # Send IRC login commands
    s.connect((d['HOST'], d['PORT']))

    s.send(bytes("PASS %s\r\n" % d['OAUTH'], "UTF-8"))
    s.send(bytes("NICK %s\r\n" % d['NICK'], "UTF-8"))
    s.send(bytes("USER %s %s bla :%s\r\n" % (
        d['IDENT'], d['HOST'], d['REALNAME']), "UTF-8"))
    s.send(bytes("JOIN #%s\r\n" % d['CHAT_CHANNEL'], "UTF-8"))

    return s

if __name__ == "__main__":
    # simple connection test
    s = connect()
    read_buffer = ""
    while(True):
        read_buffer = s.recv(1024).decode("UTF-8", errors = "ignore")
        print(read_buffer)


