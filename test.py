'''
HW1 submission test program by
part of HW1 submission by
2016064 - Palash Aggrawal
2016201 - Snehal Gupta
The txt file used is included in the zip submitted

import unittest
import urllib.request
import json
from a1 import *
from random import uniform,randint

#We create a list containing all the valid currency codes.
#This is from a txt file created from the given webpage
currency = open('currency.txt', 'r')
currencylist = list(currency)
n = len(currencylist)


'''
In the following test procedure, the functions currency_response, has_error, and exchange are tested
The test cases are made as general as possible, 
so as to remove the possibility of having selected 'favorable test cases'

i.e. after the test we are sure we tested for statistically any value that could hve been thrown at the functions

This is becuase the test cases are selected from the list of possible values (currency codes) randomly
This is viable for test because there is no partition in the possible values regarding their affect on the functions
Meaning that no value is different from another in terms of its value as a test case for the functions

Further, by this anyone who doesn't have the main program's code can be sure that the program is runnig fine
Coz there is no 'match fixing'  in this test'''

class test(unittest.TestCase):
	
	"""Testing the currency_response function"""
	def testresponse(self):

		#Iterating test 5 times, with different RANDOMLY selected test cases.

		for i in range(5):

			#Selecting from and to currency values randomly from the available valid values
			j=currencylist[randint(0,n-1)][:3]
			k=currencylist[randint(0,n-1)][:3]
			#the [:3] is to select only the first three letters of each item in the list
			#The rest of it is '/n' as in the data it is a newline after each code


			#Selecting at random an amount less than 5000
			amt = uniform(0,5000)



			#Creating the url string
			url='http://cs1110.cs.cornell.edu/2015fa/a1server.php?from='+j+'&to='+k+'&amt='+str(amt)



			#Expected result from the test data
			result = urllib.request.urlopen(url).read()
			self.assertEqual(currency_response(j,k,amt),result)


	def testerror(self):
		"""Test Cases for has_error function"""
		#These various test cases include combinations of incomplete capitalisation of input
		#And also completely wrong input.

		#Defining a function so that long line of code is not required for each test case.
		def iterhas_error(cf,ct,amt):
			result = currency_response(cf,ct,amt).decode("utf-8")
			return has_error(result)

		#Various combinations of erronous values
		self.assertEqual(iterhas_error('inr','USD',200),True)
		self.assertEqual(iterhas_error('iNR','usd',250),True)
		self.assertEqual(iterhas_error('INR','usd',250),True)
		self.assertEqual(iterhas_error('INR','AED','25r'),True)
		self.assertEqual(iterhas_error('iNR','usd','25r'),True)
		#And correct values
		self.assertEqual(iterhas_error('LKR','AED',30),False)
	
	def testexchange(self):
		"""Test Cases for exchange function"""
		#Iterating test 5 times, with different RANDOMLY selected test cases.

		for i in range(5):

			#Selecting from and to currency values randomly from the available valid values
			j=currencylist[randint(0,n-1)][:3]
			k=currencylist[randint(0,n-1)][:3]
			#the [:3] is to select only the first three letters of each item in the list
			#The rest of it is '/n' as in the data it is a newline after each code



			#Getting exchange rate
			url='http://cs1110.cs.cornell.edu/2015fa/a1server.php?from='+j+'&to='+k+'&amt='+'1'
			json = urllib.request.urlopen(url).read().decode("utf-8")
			locat = json.find('rhs')+8
			json=json[locat:] #We sliced json such that now it starts from 8 places after r of rhs
			                  #i.e. from where the amount of 1 currency_from in currency_to starts.

			exrate = json[: json.find(' ')]
			


			#Selecting at random an amount less than 5000
			amt = uniform(0,5000)
			#Result should be equal to manually calculated result
			resamt = round(amt*float(exrate),3)
			'''We use the round off function because, when calculated from above method,
			the values were deviating after about 7-8 decimal places.
			We know that is due to the way the two algrithms calculate.
			We can be sure that the answer is correct if we check to just three decimal places
			In fact we could have just type casted it into an integer.
			Knowing that if the two methods are giving the same integer but devivate in the decimals,
			The error is negligible, and thus we can be sure that the answer is coming correct''' 
			
			self.assertEqual(round(float(exchange(j,k,amt)),3),resamt)


		#Also checking for some erronous values
		self.assertEqual(exchange('inr','USD',200),-1)
		self.assertEqual(exchange('INR','USD','2rr'),-1)
		self.assertEqual(exchange('INR','UsD',200),-1)

if __name__=='__main__':
	unittest.main()
