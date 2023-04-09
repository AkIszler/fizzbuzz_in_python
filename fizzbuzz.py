def fizzbuzz():
     for i in range(1,100):
        if i % 2 == 0:
                print("fizz")  #prints fizz if divisible by 2
        if i % 3 == 0:
                print("buzz")   #prints buzz if divisible by 3
        if i % 3 == 0 & i % 2 == 0:
             print("fizzbuzz")  #prints fizzbuzz if divisible by 3 and 2
        else:
             print(i)     #prints the rest of the numbers
fizzbuzz()

#done in function because I wanted to pratice my functions

