number = 13195
for index in range(number-1,1,-1):
    if number%index == 0:
        # if index is prime or not
        is_index_prime = True
        for index_index in range(2, index):
            if index%index_index == 0:
                is_index_prime = False
                break
        if is_index_prime:
            print(index)
            break