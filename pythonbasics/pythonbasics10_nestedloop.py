goAgain = "yes"
while (goAgain == "yes"):
  limit = int(input("What number should I count up to? "))
  print("Okay, I will count up to " + str(limit))
  
  
  for count in range(limit):
    print(count+1)
    
  print("Okay, I'm done!")
  goAgain = input("Would you like to go again? Answer yes or no. ")

print("Good bye!")