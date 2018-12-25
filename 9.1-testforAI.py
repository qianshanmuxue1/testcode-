import itchat

from itchat.content import TEXT


@itchat.msg_register(itchat.content.TEXT)
def simple_reply(msg):
    if msg['Type'] == TEXT:
        return 'I received: %s' % msg['Content']


itchat.auto_login()
#itchat.send(msg=u'hello',toUserName="")
#itchat.logout()
itchat.run()


