import socket, sys


class ChatscriptInstance(object):
    def __init__(self, bot, user, server='127.0.0.1', port=1024):
        self.server = server
        self.port = port
        self.bot = bot
        self.user = user
        
        
    def sendAndReceiveChatScript(self, texte, timeout=10):
        msg = u'%s\u0000%s\u0000%s\u0000' % (self.user+self.bot, self.bot, texte)
        msg = str.encode(msg)
        try:
            # Connect, send, receive and close socket. Connections are not persistent
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(timeout)  # timeout in secs
            try:
                s.connect((self.server, self.port))
            except socket.gaierror as e:
                print("Address-related error connecting to server: %s" % e)
                sys.exit(1)
            except socket.error as e:
                print("Connection error: %s" % e)
                sys.exit(1)

            s.sendall(msg)
            msg = ''
            while True:
                chunk = s.recv(1024)
                if chunk == b'':
                    break
                msg = msg + chunk.decode("utf-8")
            s.close()
            return msg
        except Exception as inst:
            print(type(inst))
            print(inst.args)
            print(inst)
            return None
        
    def chatscript(self, texte):
        return self.sendAndReceiveChatScript(texte)
