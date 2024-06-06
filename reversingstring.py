string = "Im Praneetha Passionate Python Developer"
words = string.split(" ")
words = words[-1::-1]
outputstring = " ".join(words)
print(outputstring)