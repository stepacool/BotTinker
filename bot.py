import config
import utils
import requests
import json
import re
import threading
import socket
from time import sleep




def main():
	s = socket.socket()
	s.connect((config.HOST, config.PORT))
	s.send("NAME {}\r\n".format(config.NAME).encode("utf-8"))
	s.send("PASS {}\r\n".format(config.PASS).encode("utf-8"))
	s.send("JOIN #{}\r\n".format(config.CHAN).encode("utf-8"))

	chat_message = re.compile 
	utils.mess(s, "Hello. Bot initiated.")

	T = threading.Thread(args = (), target = utils.fillModList, group=None)
	T.start()
	T.run()
	while True:
		response = s.recv(1024).decode('utf-8')
		print(response)
		sleep(2)


if __name__ == "__main__":
	main()