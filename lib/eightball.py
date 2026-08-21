from math import ceil
import random
import json


class EightBall: 	
	salts = []	
	i = 0
	mode = "free"
	theend = False
	useend = False
	answers = [
	    {"text": "● It is certain.", "val": 1},
	    {"text": "● It is decidedly so.", "val":  1},
	    {"text": "● Without a doubt.", "val":  1},
	    {"text": "● Yes definitely.", "val": 1 },
	    {"text": "● You may rely on it.", "val":  1},        
	    {"text": "● As I see it, yes.", "val":  0.6},
	    {"text": "● Most likely.", "val":  0.8},
	    {"text": "● Outlook good.", "val":  0.7},
	    {"text": "● Yes.", "val":  1},
	    {"text": "● Signs point to yes.", "val":  0.9 },        
	    {"text": "● Reply hazy, try again.", "val":  0.6},
	    {"text": "● Ask again later.", "val":  0.6},
	    {"text": "● Better not tell you now.", "val":  0.4},
	    {"text": "● Cannot predict now.", "val": 0.4 },
	    {"text": "● Concentrate and ask again.", "val": 0.6 },        
	    {"text": "● Don't count on it.", "val":  0.1},
	    {"text": "● My reply is no.", "val":  0},
	    {"text": "● My sources say no.", "val":  0.3},
	    {"text": "● Outlook not so good.", "val": 0.2 },
	    {"text": "● Very doubtful. ", "val": 0.1 }]

	def __init__(self, salts_string = "", useend = False):
		self.salts = []
		self.useend = useend

		if salts_string != "":
			self.setSalts(salts_string)
			self.mode = "salted"
		
		
	def random(self, ar):
		result = None
		
		if self.mode == "free":
			result = random.choice(ar)
		else:
			result = self.getOneByEightBall(ar)
		
		return result
			
	def answer(self):			
		if self.mode == "free":
			ans = random.choice(self.answers)["val"]
		else:
			ans = self.getOne(self.answers, self.salts[self.i])["val"]
			
		if ans > 0.5:
			return True
		else:
			return False
		
	# only random 8 ball

	def getOneRandomWithEightBall(self, ar):
		item = None
		yes = False
		
		while not yes:		
			item = random.choice(ar)
			yes = self.answer()

		return item	
			
	# salted 8 ball	
	
	def setSalts(self, salts):
		saltssplitted = salts.split(" ")
		for salt in saltssplitted:
			if salt != "":
				self.salts.append(salt)	
		
	def getOneByEightBall(self, ar, justnum = False):
		item = None
		yes = False
		
		while not yes:
			item = self.getOne(ar, self.salts[self.i], justnum)			
			yes = self.answer()
		
		if self.useend and self.theend:
			return False
			
		return item		

	def answerText(self, salt):
		return self.getOne(self.answers, salt)["text"]

	def getOne(self, ar, salt, justnum = False):		
		length = len(ar)
		num = self.getNumber(length, salt)

		if justnum:
			return num
		
		self.i += 1
		if (self.i >= len(self.salts)):		
			self.i = 0
			self.theend = True
			
		one = ar[num]
		return one
		
	def getNumber(self, length, salt):
		sums = 0
		for i, char in enumerate(salt):
			sumitem = ord(char)
			sums = sums + sumitem
		answer = ceil(sums % length)		
		return answer
		
	# only random by salts

	def getOneBySalts(self, ar, justnum = False):
		item = self.getOne(ar, self.salts[self.i], justnum)					
		
		if self.useend and self.theend:
			return False
			
		return item		
	
	# shuffle 

	def shuffle(self, ar, mode):		
		for i in range(len(ar) - 1, 0, -1):
			if mode == "free8ball":
				one = self.getOneRandomWithEightBall(ar)
				j = ar.index(one)			
			elif mode == "salted":				
				one = self.getOneByEightBall(ar)
				j = ar.index(one)
			else:
				one = random.choice(ar)
				j = ar.index(one)
			ar[i], ar[j] = ar[j], ar[i]
		return ar
	
	# random from range
	
	def randomFromRange(self, minv, maxv, mode):
		result = None
		rlist = []
		
		if minv < maxv: 
			r = range(minv, ceil(maxv), 1)
			rlist.extend(r) 
			rlist.append(maxv) 
					
		if mode == "free8ball":
			result = self.getOneRandomWithEightBall(rlist)
		elif mode == "salted":
			result = self.getOneByEightBall(rlist)
		else:
			result = random.choice(rlist)
		
		return result

	def get8ballAnswer(self):
		 return random.choice(self.answers)
