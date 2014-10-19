import sqlite3
import time

class ChatDatabase(object):

    def __init__(self, name):
        '''
        Connect to name.db, and create table Chat if it doesn't exist.
        '''

        self.schema = "(TimeSinceEpoch, TwitchUsername, MessageContents)"
        self.conn   = sqlite3.connect(name)
        self.c      = self.conn.cursor()

        self.c.execute('''CREATE TABLE IF NOT EXISTS Chat
            (
            TimeSinceEpoch int,
            TwitchUsername varchar(255),
            MessageContents varchar(500)
            )
            ''')

    def write(self, message):
        ''' insert object of type Message into the database'''

        sql_info = ( 
                str(int(time.time())), # int, time-since-epoch
                message.sender,        # str, twitch username 
                message.contents,       # str, message contents
                )

        self.c.execute('''INSERT INTO Chat 
            VALUES (?, ?, ?)
            ''', sql_info)

    def commit(self): 
        self.conn.commit()

    def close(self):
        self.conn.close()


    def read_all_messages(self):
        self.c.execute('''SELECT * FROM Chat''')
        message = c.fetchone()
        while(message):
            print(message)
            message = c.fetchone()


    def read_messages_starting_at(time): pass

