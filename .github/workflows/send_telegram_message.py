import sys
import requests
from datetime import datetime, timedelta

bot_token = sys.argv[1]
group_id = sys.argv[2]
user = sys.argv[3]
issue_title = sys.argv[4]
issue_url = sys.argv[5]
issue_number = sys.argv[6]
issue_tags = sys.argv[7]

message = f'''
<b>[Nuevo Ticket] - ID #: {issue_number}</b>
<b>Creado por:</b> {user}
<b>Tema:</b> {issue_title}
<b>Enlace:</b> <a href="{issue_url}">click aquí</a>
<b>Tags:</b> {issue_tags}
<b>Notificación:</b> {(datetime.now() - timedelta(hours=5)).strftime("%d/%m/%Y : %H:%M:%S")}
'''

print(message)
r =requests.post(
    f'https://api.telegram.org/bot{bot_token}/sendMessage',
    json={'chat_id': group_id, 'text': message, 'parse_mode' : 'HTML'}
)

