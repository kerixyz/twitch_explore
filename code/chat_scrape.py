import socket
import logging
from emoji import demojize

logging.basicConfig(level = logging.DEBUG,
                    format = '%(asctime)s - %(message)s',
                    datefmt = '%Y-%m-%d_%H:%M:%S',
                    handlers = [logging.FileHandler('../logs/102219-loeya-chat.log', encoding = 'utf-8')])

server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'Kxree'
token = 'oauth:8q3kbk4it7gis5wphcnublfc321yzy'
channel = '#loeya'


def main():
    s = socket.socket()
    s.connect((server, port))
    s.send(f"PASS {token}\r\n".encode('utf-8'))
    s.send(f"NICK {nickname}\r\n".encode('utf-8'))
    s.send(f"JOIN {channel}\r\n".encode('utf-8'))

    try:
        while True:
            r = s.recv(2048).decode('utf-8')
            print(r)

            if r.startswith('PING'):
                s.send("PONG\n".encode('utf-8'))

            elif len(r) > 0:
                logging.info(demojize(r))

    except KeyboardInterrupt:
        s.close()
        exit()

if __name__ == '__main__':
    main()
