from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import socket

# Create your views here.

botname = "cleophee"
server = "127.0.0.1"
port = 1024
user = "User"

def home(request):
    #msg = u'%s\u0000%s\u0000%s\u0000' % (user, botname, ":build patient")
    #msg = str.encode(msg)
    #resp = sendAndReceiveChatScript(msg, server=server, port=port)
    #print("ici"+str(resp))
    return render(request, 'chat/home.html')

def sendAndReceiveChatScript(msgToSend,server='127.0.0.1',port=1024,timeout=10):
    try:
        # Connect, send, receive and close socket. Connections are not persistent
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)  # timeout in secs
        try:
            print('ici')
            s.connect((server, port))
        except socket.gaierror as e:
            print("Address-related error connecting to server: %s" % e)
            sys.exit(1)
        except socket.error as e:
            print("Connection error: %s" % e)
            sys.exit(1)

        print('sendAndReceiveChatScript {}'.format(msgToSend))
        s.sendall(msgToSend)
        msg = ''
        while True:
            chunk = s.recv(1024)
            if chunk == b'':
                break
            msg = msg + chunk.decode("utf-8")
        s.close()
        return msg
    except:
        print('sendAndReceiveChatScript catching exception. Return None')
        return None
    

def cs(request):
    if request.method == 'POST':
        query = request.POST['msgtxt']
        query = query.strip()
        print('cs {}'.format(query))
        msg = u'%s\u0000%s\u0000%s\u0000' % (user, botname, query)
        msg = str.encode(msg)
        resp = sendAndReceiveChatScript(msg, server=server, port=port)
        print('cs got ChatScript response: {}'.format(resp))
        
        return HttpResponse(resp)
