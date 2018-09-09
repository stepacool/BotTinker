import config
import utils

import requests  # probably not needed, will look into it later
import json # dunno why it's here  now, but will definitely ccome in handy later
import re # will probably move it to utils or config later, needed only to get the message out of a response
import _thread # better threading
import socket # essential here
from random import randint # for test purposes, twitch doesn't allow >2 similar messages per 30 secs
from time import sleep 

# Changed threading to _thread for the sake of simplicity


def main():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((config.HOST, config.PORT))
	s.send("Init #{} :{}\r\n".format(config.CHAN, "messagesss").encode('utf-8')) # For some reason, without a "wrong" command first, other won't work
	s.send("PASS {}\r\n".format(config.PASS).encode("utf-8"))
	s.send("NICK {}\r\n".format(config.NAME).encode("utf-8"))	
	s.send("JOIN #{}\r\n".format(config.CHAN).encode("utf-8"))
	s.send("PRIVMSG #{} :{}\r\n".format(config.CHAN, "Bot initiated").encode('utf-8'))
	response = s.recv(1024).decode('utf-8')
	chat_message = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
	utils.mess(s, "Bot initiated.")
	# T = threading.Thread(args = (), target = utils.fillModList, group=None)
	# print(1)
	# T.start()
	# print(3)
	# T.run() # THIS LINE IS THE PROBLEM
	# print(2)
	_thread.start_new_thread(utils.fillModList, ())
	while True:
		response = s.recv(1024).decode('utf-8')	
		print(response)
		if response.strip() == "PING :tmi.twitch.tv":
			s.send("PONG :tmi.twitch.tv".encode('utf-8'))
			print("sending PONG")
		else:
			message = chat_message.sub("", response).strip()
			nickname = re.search(r'PRIVMSG #(\w+)', response)
			if nickname != None:
				nickname = nickname.group(1)
			print(nickname)
			if message == "Hello" or message == "Hi":
				utils.mess(s, "Greetings " + nickname)
		sleep(0.5)


if __name__ == "__main__":
	main()