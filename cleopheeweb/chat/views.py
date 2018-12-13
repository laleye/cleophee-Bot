from django.shortcuts import render

# Create your views here.

def home(request):
    #msg = u'%s\u0000%s\u0000%s\u0000' % (user, botname, ":build patient")
    #msg = str.encode(msg)
    #resp = sendAndReceiveChatScript(msg, server=server, port=port)
    #print("ici"+str(resp))
    return render(request, 'chat/home.html')
