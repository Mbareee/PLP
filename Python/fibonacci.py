fibionacci = []

def get_nums(N):
    for x in range(N):
        if x == 0:
            fibionacci.append(x)

        elif x ==1:
            fibionacci.append(x)
    

        else:
            fibionacci.append(fibionacci[x-1] + fibionacci[x-2])

    print(fibionacci)


get_nums(10)