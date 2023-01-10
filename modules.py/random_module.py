import random
print(random.randint(2,4))  # PRINT ANY NUMBER BETWEEN 2 AND 4 INCLUDING 2 AND 4
print(random.randrange(2,4))  # PRINT ANY NUM BETWEEN 2 AND 4 EXCLUDING 4
l=[10,20,30,40]
print(random.choice(l))
# shuffle() RETURNS HE SEQUENCE IN A RANDOM ORDER
random.shuffle(l)
print(l)
# uniform() RETURNS A RANDOM FLOAT NUMBER BETWEENTWO GIVEN PARAMETERS
print(random.uniform(3,9))