filename = 'py/pcc_2e/chapter_10/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = 'a'
for line in lines:
    pi_string += line.strip()
    
print(f"{pi_string[:52]}...")
print("length = " , len(pi_string))
print("length2 = " + str(len(pi_string)))
