import config
import requests
import json
import threading
import socket
from time import sleep


def mess(sock, mess):
	sock.send("PRIVMSG #{} :{}\r\n".format(config.CHAN, mess).encode('utf-8'))





def ban(sock, user):
	mess(sock, ".ban {}".format(user))





def timeout(sock, user, seconds = 500):
	mess(sock, ".timeout {} {}".format(user, seconds))




#http://tmi.twitch.tv/group/user/stepacool/chatters
def fillModList():
	while True:
		try:
			url = "http://tmi.twitch.tv/group/user/stepacool/chatters"
			req = requests.get(url, headers={"accept": "*/*"})
			res = req.text
			print(req, res, req.json())
			if not res.find("502 Bad Gateway"):
				config.modlist.clear()
				data = req.json()
				for p in data["chatters"]["moderators"]:
					config.modlist[p] = "mod"
				for p in data["chatters"]["admins"]:
					config.modlist[p] = "admin"
				print(data)
		except:
			print("ERROR! Something went wrong.")
		sleep(5)



