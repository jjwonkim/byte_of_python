number = 23
running= 1


while running:

    guess = int(raw_input('Enter an integer :'))
    
    if guess == number:
        print 'Cong. you guessed it.'
        running  = 0
    
    elif guess < number:
        print 'No, it is a little higher than that'
        
    else:
        print 'No, it is a little lower than that'
        
else:
    print 'The while loop is over.'
        
print 'Done'
