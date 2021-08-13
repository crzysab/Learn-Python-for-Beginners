tuplez = (2,4,1,4,7,8)
print("My Tuple : ", tuplez)

# Count an element in tuple
cou = tuplez.count(4)
print("4 in my tuple : ", cou)

# Check index number
ind = tuplez.index(7)
print("7 in index : ", ind)

# Add a new element in tuple
tuplez = tuplez + (5,)
print("New Tuple : ",tuplez)

# Remove an element in tuple
tuplez = list(tuplez) #must be convert to a list
tuplez.remove(8)
print("After remove : ", tuplez)