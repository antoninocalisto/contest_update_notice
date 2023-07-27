#----------------------

#----------------------
import base64
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError
#----------------------
def send_email():
	SCOPES = [
			"https://www.googleapis.com/auth/gmail.send"
		]
	flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
	creds = flow.run_local_server(port=0)

	service = build('gmail', 'v1', credentials=creds)
	message = MIMEText('This is the body of the email')
	message['to'] = 'antuninosantos@gmail.com'
	message['subject'] = 'Concurso lançado!'
	create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

	try:
		message = (service.users().messages().send(userId="me", body=create_message).execute())
		print(F'sent message to {message} Message Id: {message["id"]}')
	except HTTPError as error:
		print(F'An error occurred: {error}')
		message = None
	# -----------------------------------------

def option_login_email_selenium():
	print('Entrou aqui!')


# -----------------
# Hunter Thornsberry
# http://www.adventuresintechland.com

# WebChange.py
# Alerts you when a webpage has changed it's content by comparing checksums of the html.

# import hashlib
# import urllib.request

# import random
# import time

# # url to be scraped
# url = "http://www.11rm.eb.mil.br/index.php/geral-categorias/102-geral/programas/servico-militar/militar-temporario/editais-processos-seletivos-para-militar-temporario/processo-seletivo-de-oficial-tecnico-temporario/490-edital-e-avisos-ott-ti-23-24"

# # time between checks in seconds
# sleeptime = 60

# def getHash():
#     # random integer to select user agent
#     randomint = random.randint(0,7)

#     # User_Agents
#     # This helps skirt a bit around servers that detect repeaded requests from the same machine.
#     # This will not prevent your IP from getting banned but will help a bit by pretending to be different browsers
#     # and operating systems.
#     user_agents = [
#         'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
#         'Opera/9.25 (Windows NT 5.1; U; en)',
#         'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
#         'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
#         'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.142 Safari/535.19',
#         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
#         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:8.0.1) Gecko/20100101 Firefox/8.0.1',
#         'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.151 Safari/535.19'
#     ]

#     opener = urllib.request.build_opener()
#     opener.addheaders = [('User-agent', user_agents[randomint])]
#     response = opener.open(url)
#     the_page = response.read()

#     return hashlib.sha224(the_page).hexdigest()

# current_hash = getHash() # Get the current hash, which is what the website is now
# print(current_hash)
# while 1: # Run forever
#     print(getHash())
#     if getHash() == current_hash: # If nothing has changed
#         print ("Not Changed")
#     else: # If something has changed
#         print ("Changed")
#         break
#     time.sleep(sleeptime)

# ----------------

# while True:
# 	try:
# 		url ="https://www.uetmardan.edu.pk/uetm/"
# 		r = requests.get(url)

# 		# Step2: Parse the HTML content
# 		soup = BeautifulSoup(r.content, 'html5lib')

# 		#print(soup.prettify()) # just printing the HTML code

# 		print(soup.get_text()) # just printing the text
# 	except KeyboardInterrupt: #so you can break the loop
# 		#maybe some clean up
# 		break
# 	#maybe catch something else

# 	# sleep(interval)

import requests
import time
import smtplib
from email.message import EmailMessage
import hashlib
from urllib.request import urlopen

# Aberto
# url = 'http://www.11rm.eb.mil.br/PROC_SELETIVO/23_24/OTT-23/OTT23-TI/'

# Fechado
# url = 'https://7rm.eb.mil.br/index.php/processos-seletivos-ott-stt-2018/item/82-processo-seletivo-2020-ott-stt-cet'

#Aberto
url = 'https://4rm.eb.mil.br/index.php/component/content/article?id=900'

response = urlopen(url).read()
currentHash = hashlib.sha224(response).hexdigest()

while True:
	try:
		response = urlopen(url).read()
		currentHash = hashlib.sha224(response).hexdigest()
		time.sleep(10)
		response = urlopen(url).read()
		newHash = hashlib.sha224(response).hexdigest()

		if newHash == currentHash:
			print("Not changed")
			continue
		else:
			print("This is a test")
			continue
	except:
	    print('failed')
