def fizzbuzz():
     for i in range(1,100):
        if i % 2 == 0:
                print("fizz")

        if i % 3 == 0:
                print("buzz")
        if i % 3 == 0 & i % 3 == 0:
             print("fizzbuzz")
        else:
             print(i)     

fizzbuzz()