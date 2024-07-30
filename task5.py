# Problem 1 - what will be thw expected out for the following?

data = [10,501,22,37,100,999,87,351]
result = filter (lambda x: x > 4, data)
print(list(result))
# outupt will be the same data given : [10,501,22,37,100,999,87,351] 

# Problem 2 - Writa a python code using lambda function to check every element of list is string or integer.
 
x=input("Enter here:")
data.apply(lambda x: x.dtype)

# Problem 3 - write a code using lambda function  to create a fibonacci series from 1 to 50 elements
fibo = lambda n: [ab.append(sum(ab))]
for ab in [[0,1]]:
 for n in range(n):
   print(*fibo(50))

# Problem 4 - Write a python function to validate Regular expression for the following
 
 # a)-Email Address:

def validate_email_id(self, email):
 pattern = r"^[a-z0-9_.]+@[a-z0-9]+\.[a-z]{2,6}"
 if re.match ( pattern , email):
  return True
 else:
  return False  

 # b)-Mobile number of Bangladesh

 def validate_bangladesh_mobile_number(self, mobile_number):
  pattern=r"^[+880][1][0-9]{9}$"
 if re.match ( pattern , mobile_number):
  return True
 else:
  return False  
 
 # c)- validate telephone numbers of USA:

 def validate_USA_telephone_number(self, telephone_number):
  pattern=r"^[+1][0-9]{9}"
 if re.match ( pattern , telephone_number):
  return True
 else:
  return False   
 
 # d)- 16 character alpha numeric password includes uppercase, lowercase, special char, numbers
  
def validate_password(self, password):
  pattern=r"^[A-Z][a-z]@[0-9]{15}"
  if re.match ( pattern , password):
   return True
  else:
   return False  

