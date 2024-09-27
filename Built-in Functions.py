secret = [-78, -385, -436, 489, -484, -433, -529, 396, 35, 409, -489, -367, -94, 515, 515, 374]
key = [12, 50, 44, 6, 36, 22, 21, 49, 90, 66, 56, 98, 51, 60, 35, 71]

print(secret)
print(key)

# Get the absolute value of each number in secret
abs_secret = []
for num in secret:
    new_num = abs(num)
    abs_secret.append(new_num)
print(abs_secret)

# For each index add the number in key to the result of step 1


# Reverse the order of the numbers in the result of step 2
# Use integer division to divide each number in the result of step 3 by 5
# Add the index of each number in step 4 to its value
# Convert each value to a character
# use ''.join(list) to convert a list of characters to a string
