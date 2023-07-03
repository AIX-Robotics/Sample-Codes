limit = 10
count = 1
while (count <= limit):
  if (count < limit/2):
    print("Count is " + str(count) + ": we're not yet halfway")
  elif (count == limit/2):
    print("Count is " + str(count) + ": we're halfway")
  else:
    print("Count is " + str(count) + ": we're almost there!")
  count = count+1

print("Done")