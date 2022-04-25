from difflib import get_close_matches
import json
from random import choice
import datetime

class DateTime:
	def currentTime(self):
		time = datetime.datetime.now()
		x = " A.M."
		if time.hour>12: x = " P.M."
		time = str(time)
		time = time[11:16] + x
		return time

	def currentDate(self):
		now = datetime.datetime.now()
		day = now.strftime('%A')
		date = str(now)[8:10]
		month = now.strftime('%B')
		year = str(now.year)
		result = f'{day}, {date} {month}, {year}'
		return result
	

def isContain(text, lst):
	for word in lst:
		if word in text:
			return True
	return False



data = json.load(open('extrafiles/NormalChat.json', encoding='utf-8'))

def reply(query):
	if query in data:
		response =  data[query]
	else:
		query = get_close_matches(query, data.keys(), n=2, cutoff=0.6)
		if len(query)==0: return "None"
		return choice(data[query[0]])

	return choice(response)

