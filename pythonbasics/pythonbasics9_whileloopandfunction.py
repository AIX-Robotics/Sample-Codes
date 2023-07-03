# Define a function to greet a person with a given name
def greet(name):
  print("Hello " + name + ", how are you?")
  print("I'm very pleased to meet you.")


# Greet several people specified by the user
goAgain = "yes"
while (goAgain == "yes"):
  name = input("Please enter the name of a person to greet: ")
  greet(name)
  goAgain = input("Would you like to go again? Answer yes or no. ")


print("Good bye!")