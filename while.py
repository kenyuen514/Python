#enter a number
#add them all together and calculate the averge
#stop after entering -1

total = 0
count=0

user_input = int(input("Please enter a number (-1 to exit) : "))
while user_input != -1:
     total += user_input #sum of user input
     count += 1 #counting the number of entries, but not too suer why need to adding +=1

     user_input = int(input("Please enter a number (-1 to exit) : "))

     if user_input == -1: #after entering -1, exit
         print(total)
         print(count)
         average = total / count #calculate the average
         print(average)
         break




