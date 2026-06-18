import random as rd 
#rd is aliased to random module
#genrate float random between 0 and 1
rand_float = rd.random()
print("Random float between 0 and 1 is: ", rand_float)
#genrate random float number between 1 and 10
rand_float_range = rd.uniform(1, 10)
print("Random float between 1 and 10 is: ", rand_float_range)   
#generate random integer between 1 and 100
rand_int = rd.randint(1, 100)
print("Random integer between 1 and 100 is: ", rand_int)
#generate random integer between 1 and 100 with step of 5
rand_int_step = rd.randrange(1, 100, 5)
print("Random integer between 1 and 100 with step of 5 is: ", rand_int_step)
