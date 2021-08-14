# 1. range(stop) -> starts from 0 till (stop-1)
print("Example 1")
for data in range(5):
    print(data)

# 2. range (start,stop) -> ends at (stop-1)
print("Example 2")
for data in range(5,10):
    print(data)

# 3. range(start, stop, step) -> step cannot be 0, default is 1
print("Example 3")
for data in range(0,10,2):
    print(data)
