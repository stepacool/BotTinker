import config
import utils
import requests
import json
import re
import threading
import socket
from time import sleep




def main():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((config.HOST, config.PORT))
	s.send("PASS {}\r\n".format(config.PASS).encode("utf-8"))
	s.send("NICK {}\r\n".format(config.NAME).encode("utf-8"))	
	s.send("JOIN #{}\r\n".format(config.CHAN).encode("utf-8"))
	s.send("PRIVMSG #{} :{}\r\n".format(config.CHAN, "messagesss").encode('utf-8'))
	response = s.recv(1024).decode('utf-8')
	print(response)

	chat_message = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
	utils.mess(s, "Hello. Bot initiated.")
	print(chat_message)

	T = threading.Thread(args = (), target = utils.fillModList, group=None)
	print(1)
	T.start()
	print(3)
	T.run() # THIS LINE IS THE PROBLEM
	print(2)
	while True:
		response = s.recv(1024).decode('utf-8')	
		print(response)
		print(1)
		message = chat_message.sub("", response)
		print(message)
		utils.mess(s, "Hello. Bot initiated.")
		sleep(2)


if __name__ == "__main__":
	main()