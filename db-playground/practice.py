import sqlite3

schema = "(TimeSinceEpoch, TwitchUsername, MessageContents)"
conn   = sqlite3.connect('test.db')
c      = conn.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS Chat
            (
            TimeSinceEpoch int,
            TwitchUsername varchar(255),
            MessageContents varchar(500)
            )
            ''')

c.execute('''INSERT INTO Chat {}
        VALUES ('12345', 'LeKlappaTroll', 'top kek')
        '''.format(schema))

c.execute('''SELECT * FROM Chat''')
print(c.fetchone())

conn.commit()
conn.close()

