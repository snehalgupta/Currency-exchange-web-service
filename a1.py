
'''
HW1 Submission by 
2016064 - Palash Aggrawal
2016201 - Snehal Gupta
The txt file used is included in the zip submitted

This is a program which helps in live currency conversion.
It takes from the user 
	-> the currency from which to convert
	-> the amount of this currency
	-> The currency in which to convert to

The input however is formatted in a way that - both currencies should be entered in terms of valid currency codes
and the currency codes should be in capitals. There is an option for the user to refe to the valid currency codes,
to make the program user friendly.
Also, the amount entered should be float.

This program uses a web sevice which gives data based on the entered values stated above 
and on real time exchange rate data. The web service returns JSON data and this program analyises that accordingly.

Various functions are defined to handle these tasks.
 #Step 1 - Get Input

 #Step 2 - Paste input in URL by concatenating

 #Step 3 - Get JSON (define currency_response())

 #Step 4 - Check validity in response (define has_error())

 #Step 5 - Analyse and Slice the JSON string (define excahnge(), before_space(), after_space())

 #Step 6 - Output the converted amount which is returned from exchange()

'''

import urllib.request

import json


def currency_response(currency_from,currency_to,amount_from):

        """Returns: a JSON string that is a response to a currency query. 

         This is the function to handle the web request
         A currency query converts amount_from money in currency currency_from  to the                  
         currency currency_to. The response should be a string of the form

        '{"lhs":"<old­amt>","rhs":"<new­amt>","valid":true, "error":""}'       

         where the values old­amount and new­amount contain the value and name  for the                              
         original and new currencies. If the query is invalid, both old­amount and new­amount will
         be empty, while "valid" will be followed  by the value false. 

         Parameter currency_from: the currency on hand  
         Precondition: currency_from is a string          

         Parameter currency_to: the currency to convert to    
         Precondition: currency_to is a string  

         Parameter amount_from: amount of currency to convert   
         Precondition: amount_from  is a float"""

        #Creating the required string for web request
        str1='http://cs1110.cs.cornell.edu/2015fa/a1server.php?'

        str2='from='+currency_from+'&to='+currency_to+'&amt='+str(amount_from)

        str3=str1+str2 #concatenating input to url 

        obj=urllib.request.urlopen(str3) # returns an object that represents the web page for the url
        json=obj.read() # read() returns content of webpage as string, or rather JSON string in this case.
        

        return json




def has_error(json2):

      """Returns : True if the query has an error; False otherwise.

      Given a JSON response to a currency query, this returns the opposite of the value following          
      the keyword "valid". For example, if the JSON is

      '{"lhs":"","rhs":"","valid":false,"error":"Source currency code is invalid."}'

      then the query is not valid, so this function returns True (It does NOT return the message
      'Source currency code is invalid' ).

      Parameter json: a json string to parse
      Precondition : json is the response to a currency query"""
      #USING DICTIONARY

      #parsed_json=json.loads(json2)#converting json string to dictionary

      #valid=not(parsed_json['valid'])

      #return valid

      #USING STRING MANIPULATION

      #We use the fact that our JSON string has a specific format to find whether their is an erro in input
      #And also the fact that the web service analyses error in the input, so we don't need to.
      index1=json2.find('valid')
      index2=json2.index(',',index1+9)
      valid1=json2[index1+9:index2]
      if(valid1=='false'):
         return True #means has an error
      else:
         return False #means no error
      

#We have also created functions to ease string output and analysis.
def before_space(s):


       """Returns : Substring of s; up to, but not including, the first space

       Parameter s: the string to slice

       Precondition : s has at least one space in it"""

       space1=s.find(' ')

       amt_req=s[0:space1]

       return amt_req


def after_space(s):

       """Returns : Substring of s after the first space

       Parameter s: the string to slice

       Precondition : s has at least one space in it"""

       space=s.find(' ')

       cur_req=s[space+1:]


       return cur_req



def exchange(currency_from, currency_to, amount_from):

     """Returns : amount of currency received in the given exchange.

     This is effectively our main function, combining the above.
     In this exchange, the user is changing amount_from money in
     currency currency_from to the currency currency_to. The value
     returned represents the amount in currency currency_to.

     Return -1 for invalid currency code or invalid amount_from value

     The value returned has type float.

     Parameter currency_from: the currency on hand
     Precondition : currency_from is a string for a currency code.

     Parameter currency_to: the currency to convert to
     Precondition : currency_to is a string for a currency code

     Parameter amount_from: amount of currency to convert
     Precondition : amount_from is a float"""

     json1=currency_response(currency_from,currency_to,amount_from).decode("utf-8")
     # decode() decodes the byte string. Currency_response returns a JSON string, and for us to use it,
     #we need to convert it into string.

     valid1=has_error(json1)
     #The web service takes care of any error in the input, 
     #we use this feature to terminate the program if there is error in input.
     if(valid1==True):

        return -1

     else:
        #USING DICTIONARY
        #parsed_json = json.loads(json1)

        #out=parsed_json['rhs']

        #conv_amt=before_space(out)

        #USING STRING MANIPULATION
        

        #Again we use the fact that the String we have has a specific format and thus, we use it to find
        #The desired data. We know that the converted amount is after 8 characters from the 'r' of rhs.
        index3=json1.find('rhs')
        index4=json1.index(',',index3)
        out=json1[index3+8:index4-1]
        conv_amt=before_space(out)

        return conv_amt








# Application Script
if __name__=='__main__':

   print("Please enter currency in caps\n ")




   #User friendly feature additon:
   #We create an option for the user to refer to the valid currency codes data.
   #Since this can be repetietive and takes a lot of steps, all the steps are optional

   ref=input("for reference of valid currency codes, please enter y, else n \n")

   while (ref=='y'):
      #We create a list containing all the valid currency codes.
      #This is from a txt file created from the given webpage
      currency = open('currencytable.txt', 'r')
      currencylist = list(currency)
      n = len(currencylist)
      opt = input("For whole list, press a. \nFor currency starting with specific letter, press b  \n")
      #As said above, the steps are long, and therefore all functionalities are optional.

      if (opt=='a'):
          print("Psst! Don't worry about the \\n in the end of each line (if it appears!)")
          print("If it doesn't, obviously don't worry")
          for i in range(n):
               print(currencylist[i])
          print("\n \nFinding it difficult to scroll up and search?")
          print("Well you can repeat and go with option b to search using the first letter of the currency code")

      elif (opt=='b'):
          opt1=input("Enter the first letter of the currency code (pls enter in capital letter)")
          for i in range(n):
               if (currencylist[i][0]==opt1):
                    print(currencylist[i])

      else:
          print("Invalid input")

      ref = input("Repeat? (y/n)")
      




   from1=input('Enter the currency on hand (for example USD,INR) - ')

   print('Enter amount in ', from1),
   amt=input()

   to1=input('Enter the currency to convert to - ')

   result=exchange(from1,to1,amt)
   print(result)



          

     
