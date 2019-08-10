import sys
import csv
import pickle

numOfExchanges = 9

# in main, I need an array of Exchanges

class exchange:
	# num is a float
	def update_current_value(self, num):
		self.pastVal = self.currVal
		self.currVal = num

	# exchange_rate is the dictionary of exchanges with key=string names; value=float number
	def update_matrix(self, exchange_rate):

		# provide directions for which part of the matrix to update
		# default is down
		if self.currVal > self.pastVal:
			selfie = "up"
		elif self.currVal < self.pastVal:
			selfie = "down"
		elif self.currVal == self.pastVal:
			selfie = "equal"
		else:
			print("YOU FUCKED UP")	
		# print("old: " + str(self.pastVal) + "      new: " + str(self.currVal))
		# print("selfie: " + selfie)

		# iterate over the exchanges
		for exchanges in exchange_rate:
			# if we're not analyzing the same exchange or if equal, just ignore it
			if self.name == exchanges:
				# continue
				pass

			# see what the comparisons are for the other exhange
			if exchange_rate[exchanges].currVal > exchange_rate[exchanges].pastVal:
				compare = "up"
			elif exchange_rate[exchanges].currVal < exchange_rate[exchanges].pastVal:
				compare = "down"
			elif exchange_rate[exchanges].currVal == exchange_rate[exchanges].pastVal:
				compare = "equal"
			else:
				print("YOU FUCKED UP")

			#actually change the dictionary inside the dictionary
			self.relations[exchanges][selfie][compare] += 1


	# spit out if exchange is going to go up or down
	# with the certainty
	def predict_future(self):
		pass

	def printer(self, num, exchange_names,exchange_dict):
		i = 0
		if num == 1:
			print(exchange_names[i] + ": " + str(exchange_dict[exchange_names[i]].currVal))
		else:
			print(exchange_names[i] + ": " + str(exchange_dict[exchange_names[i]].currVal) +" ; " + str(exchange_dict[exchange_names[i]].pastVal))

	# name is a string. variable name should = name
	# this only happens at the start
	# exchange names is a list of strings == first row of the csv file
	def __init__(self, name, exchange_names):
		# the data one time unit before
		# initialize to something dumb
		self.pastVal = -1
		# the current data
		self.currVal = 0
		# name of exchange
		self.name = name

		#its relation with other exchanges
		# keys: names of the exchanges
		# up_up, up_down, down_up, down_down
		self.relations = {}
		# first is self. second is compare

		# back these data up every few minutes to make sure they're saved
		directions = ["up", "equal", "down"]

		# first key is self, second is what it's getting compared to
		for name in exchange_names:
			self.relations[name] = {}
			for selfie in directions:
				self.relations[name][selfie] = {}
				for compare in directions:
					self.relations[name][selfie][compare] = 0
			# catches when there are equals --> doesn't happen often. Ignore data for now

	def printMatrix(self, whatTo, exchange_names):
		directions = ["up", "equal", "down"]
		print("\n" +"\n" + self.name + "\n" + "_____________________________________")
		for exchange in exchange_names:
			# if we're only targeting one exchange, then just go back to the top of the for loop
			if (whatTo in exchange_names) and (whatTo != exchange):
				continue
			print(exchange)
			bruh = "ued"
			i = 0
			print(" " + bruh + " -" + self.name)
			for compared in directions:
					print(bruh[i] + str(self.relations[exchange]["up"][compared]) + str(self.relations[exchange]["equal"][compared]) +
						str(self.relations[exchange]["down"][compared]))
					i += 1
			print()

	# output a matrix to a csv file for manual checking
	def writeMatrix(self,whatTo,exchange_names):
		f = open("save_data.csv", "w+")

		directions = ["up", "equal", "down"]
		f.write(self.name + "\n")
		for exchange in exchange_names:
			# if we're only targeting one exchange, then just go back to the top of the for loop
			if (whatTo in exchange_names) and (whatTo != exchange):
				continue
			f.write(exchange + "\n")
			bruh = ["up","equal","down"]
			i = 0
			f.write(" ," + "up,equal,down," + self.name + "\n")
			for compared in directions:
					f.write(bruh[i]+"," + str(self.relations[exchange]["up"][compared]) +","+ str(self.relations[exchange]["equal"][compared]) +","+
						str(self.relations[exchange]["down"][compared])+ "\n")
					i += 1
			f.write("\n")
		f.close()

		# output will be true for up, false for down or 

def will_ItGoUp(exchange, exchange_rate):
	if exchange not in exchange_rate:
		print("FUCK YOU")
		return False

	up = 0
	down = 0

	upper = False
	downer = False

	for exchanger in exchange_rate[exchange].relations:

		# print (exchanger +": "+ str(Follows(exchange_rate[exchange].relations[exchanger])))
		
		# I know I can simplify this but this makes it more readable
		if exchange_rate[exchanger].currVal > exchange_rate[exchanger].currVal:
			upper = True
		else:
			upper = False

		if upper and Follows(exchange_rate[exchange].relations[exchanger]):
			up += 1
		else:
			down += 1

	if up > down:
		print("\nit will go up")
		# return True
	else:
		print("\nit's going down")
	# return False
	pass

# Does it follow?
def Follows(exchange_dict):
	directions = ["up", "equal", "down"]

	follow = 0
	oppose = 0

	# go through the matrix and see which is bigger
	for selfie in directions:
		for compare in directions:
			if selfie == compare:
				follow += exchange_dict[selfie][compare]
			else:
				oppose += exchange_dict[selfie][compare]
	if follow > oppose:
		return True
	# equal is false because inconclusive
	return False



# ETH_dict
def accept_data(ETH_dict):
	pass

def check_algorithm():
	pass

def broski_main():
	global_num = 0
	# key is stringName of the exchange
	exchange_dict = {}

	# we can pickle exchange_dict every few minutes in order to save the data
	with open('exchange_stats.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0

		for row in csv_reader:

			# every iteration of this for loop, the currVal gets updated
			# initialize the exchange variables
			if line_count == 0:
				# print(row)

				exchange_names = []	# holds the string-list of exchanges
				# saves the names of the exchanges in a string
				for i in range(1, numOfExchanges+1):
					exchange_names.append(row[i])
				#intializes the exchange objects
				for i in range(numOfExchanges):
					exchange_dict[exchange_names[i]] = exchange(exchange_names[i], exchange_names)

			else: # this else happens for the rest of the file
				for i in range(numOfExchanges):
					# update every exchange: +1 because of the time stamp
					exchange_dict[exchange_names[i]].update_current_value(float(row[i+1]))

			# iterate over the dictionary of exchanges and update the matrices
			if line_count > 1:
				# happens after the second line of the csv
				for i in range(numOfExchanges):
					exchange_dict[exchange_names[i]].update_matrix(exchange_dict)
			
			line_count += 1
			# print(row)

	
	# exchange_dict["Poloniex"].writeMatrix("all", exchange_names)
	# exchange_dict["Poloniex"].will_ItGoUp()
	will_ItGoUp("Poloniex",exchange_dict)
	print("\n\nDONE")

	# print(f'Processed {line_count} lines.')
	# if I get a negative one, too many request. Make a timeout


def messy_main():
	f = open("save_data.csv", "w+")
	f.write("1,2,3,4,5,6")
	f.close()

if __name__ == '__main__':
	broski_main()
	#messy_main()

# Poloniex
# Binance
# Huobi
# KuCoin
# Bitforex
# Bittrex
# OKEx
# Bitfinex
# TradeIO
