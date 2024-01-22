#The task is logical error

#There is a 4-digit number password to log-in
password = "345O"
user_input = input(" Please enter the 4-digit number password: ")

while True:
   user_input == password
   print(" You're wrong! ")
   user_input = input(" Please enter the 4-digit number password: ")
   if user_input != password:
       print(" Game Over ")
       break


#even the user has entered the correct pw, it will show "You're wrong! And if the user entered the wrong pw, it will show Game Over. User never log-in
