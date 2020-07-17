#String Indexing

random_string="RACECAR"

print(random_string[0])

#We can refer to String Indexes
#just like lists

print(random_string[-2])

#Slicing
#Use with any sequence (Strings,Lists,etc)

substring = random_string[0:3]
print(substring)
#randomstring does not change value
print("This is the actual string unchanged: " + random_string)

new_variable=random_string
print ("This is the new variable: " + new_variable)

new_variable=new_variable[0:-1]
print ("We delete the last character: " + new_variable)
print ("We still have our original variable: " + random_string)


