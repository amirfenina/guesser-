print ('think of  a number that is between 0 and 100')
minimum_number=0
maximum_number=100

for i in range (7):
    median = (minimum_number+maximum_number)//2
    x= input (f'is this the number you thought of {median}  (equal/higher/lower)' )
    if x=='higher' :
        minimum_number=median
    elif x=='lower':
        maximum_number=median
    else:
        break
print ('that was so easy :) nt ')


