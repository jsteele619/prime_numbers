def prime_numbers(size):
    
    the_list = list(range(2, size+1))
    
    for x in range(3, size+1):
        for y in range(2, x-1):
            if x % y == 0 and x in the_list:
                the_list.remove(x)
            else:
                pass

    print(the_list)


prime_numbers(100)