import requests
from app.mac import mac, signals

'''
Signals this module listents to:
1. When a message is received (signals.command_received)
==========================================================
'''
@signals.message_received.connect
def handle(message):
    if message.text == "jadwal pramek":
        jadwal_pramek(message)
    elif "jadwal pramek dari" in message.text:
        get_jadwal_pramek(message)

'''
Actual module code
==========================================================
'''
def jadwal_pramek(message):
    answer = "*Info Jadwal Pramek* \njadwal pramek dari <stasiun> \n*Version:* 1.0.0 \n*Status:* Beta \nhttps://www.ssonlab.com"
    mac.send_message(answer, message.conversation)

api_url_base = 'http://104.223.63.38:8081/'

def get_jadwal_pramek(message):
    segment = message.text.replace(' ', '-')
    api_url = '{0}{1}'.format(api_url_base, segment)

    response = requests.get(api_url)

    if response.status_code == 200:
        mac.send_message(response.content, message.conversation)
    else:
        return None