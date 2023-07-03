# Define a function to greet a person with a given name
def greet(name):
  print("Hello " + name + ", how are you?")
  print("I'm very pleased to meet you.")

# Greet "Ama" 4 times, appending the loop variable to Ama"s name each time
for count in range(4):
  greet("Ama" + str(count))
  
print("Good bye!")