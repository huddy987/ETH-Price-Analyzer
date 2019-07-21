import sys
import csv

numOfExchanges = 9

# in main, I need an array of Exchanges

class exchange:
	# num is a float
	def update_current_value(self, num):
		self.pastVal = self.currVal
		self.currVal = num
		pass

	#exchange_rate is the dictionary of exchanges
	def update_matrix(self, exchange_rate):
		directions = ["up", "down"]
		
		# provide directions for which part of the matrix to update
		selfie = "down"
		if self.currVal > self.pastVal:
			selfie = "up"
		elif self.currVal == self.pastVal:
			# if an equal situation occurs, ignore it for now
			self.relations["equal"]["equal"] += 1
			return

		# iterate over the exchanges
		for exchanges in exchange_rate:
			# if we're not analyzing the same exchange or if equal
			if self.name != exchanges or self.pastVal == exchange_rate[exchanges].pastVal:
				continue

			# default to down
			compare = "down"
			if self.pastVal > exchange_rate[exchanges].pastVal:
				compare = "up"




	# spit out if exchange is going to go up or down
	# with the certainty
	def predict_future():
		pass

	def printer(self, num):
		if num == 1:
			print(exchange_names[i] + ": " + str(exchange_dict[exchange_names[i]].currVal))
		else:
			print(exchange_names[i] + ": " + str(exchange_dict[exchange_names[i]].currVal) +" ; " + str(exchange_dict[exchange_names[i]].pastVal))

	# name is a string. variable name should = name
	# this only happens at the start
	def __init__(self, name):
		# the data one time unit before
		self.pastVal = -1
		# the current data
		self.currVal = 0
		# name of exchange
		self.name = name

		#its relation with other exchanges
		#keys: up_up, up_down, down_up, down_down
		self.relations = {}
		# first is home. second is compare
		# back these data up every few minutes to make sure they're saved
		directions = ["up", "down"]
		# first key is self, second is what it's getting compared to
		for selfie in directions:
			self.relations[selfie] = {}
			for compare in directions:
				self.relations[selfie][compare] = 0

		# catches when there are equals --> doesn't happen often. Ignore data for now
		self.relations["equal"] = {}
		self.relations["equal"]["equal"] = 0

# ETH_dict
def accept_data(ETH_dict):
	pass

def check_algorithm():
	pass




if __name__ == '__main__':
	global_num = 0
	# key is stringName of the exchange
	exchange_dict = {}

	with open('exchange_stats.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		for row in csv_reader:
			# every iteration of this for loop, the currVal gets updated
			# initialize the exchange variables
			if line_count == 0:
				#print(row)

				exchange_names = row	# holds the string-list of exchanges
				# initializes the 
				for i in range(1, numOfExchanges+1):
					exchange_dict[exchange_names[i]] = exchange(exchange_names[i])
			else:
				for i in range(1, numOfExchanges+1):
					# update every exchange
					exchange_dict[exchange_names[i]].update_current_value(float(row[i]))

			# iterate over the dictionary of exchanges and update the matrices
			if line_count > 1:
				for i in range(1, numOfExchanges + 1):
					exchange_dict[exchange_names[i]].update_matrix(exchange_dict)
			line_count += 1

	print()
	exchange_dict[exchange_names[i]].update_matrix(exchange_dict)
	print("DONE")

	# print(f'Processed {line_count} lines.')
	# if I get a negative one, too many request. Make a timeout

