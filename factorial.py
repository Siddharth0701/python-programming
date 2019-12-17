''''def recur_factorial(n):
   """Function to return the factorial
   of a number using recursion"""
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

# Change this value for a different result
#num = 7

# uncomment to take input from the user
num = int(input("Enter a number: "))

# check is the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of",num,"is",recur_factorial(num))
'''










print("*********************************************************************************************************************")

'''def personalinfo():
   id=int(input("plz enter the id no:"))
   name=input("enter the name: ")
   gender=input("enter your gender:")
   age=int(input("enter the age:"))

   address=input("enter the address:")

#personalinfo()
def employeeinfo():
   #salary=int(input("enter the salary of employee:"))
   qualification=input("enter thed qualification:")
   salary=int(input("enter the salary of employee:"))
   salary=0
   if salary<10000:
      salary=salary+30000
      print("congurlation your new salary is",salary)
   else:

      Sprint("your salary is no recour")
  #qualification=input("enter your qualification:")



def yourinfo():

   file_text=open("C:\Singhsoftware\singh.txt",'a')
   file_text.write( id, name, gender ,age ,address, qualification, salary)
   file_text.close()

personalinfo()
employeeinfo()
yourinfo()
      
   
'''






'''class animal:
   def dog(self):
      print("dog is very sincer animal")
   def cat(self):

      print("cat is small ")




class human( animal):
   def singh(self):
      print("my name is siddharth")
   def thakur(self):
      print("i am a thakur")


objhuman=human()
objhuman.dog()
objhuman.cat()
objhuman.singh()
objhuman.thakur()
   
'''
class parient:
   def_init_(self,name,age):
      self.name=name
      self.age=age


class child(parient):
   def show():
      print(self.name=)






































