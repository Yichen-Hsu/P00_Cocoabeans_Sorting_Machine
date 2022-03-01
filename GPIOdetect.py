

a = [0, 1, 0]
y = list()
while True:
    a = int(input("please enter you numbers: "))
    if a == 0:
        y.append(a)
        print(y)
        while True:
            a = int(input("please enter you numbers2: "))
            if a == 1:
                y.append(a)
                print(y)
                while True:
                    a = int(input("please enter your numbers3: "))
                    if a == 0:
                        y.append(a)
                        print(y)
                        if y[0] == 0 and y[1] == 1 and y[2] == 0:
                            print("detect")
                            for _ in range(int(len(y))):
                                y.pop()
                            print(y)
                            break
                        else:
                            continue
                    else:
                        continue
                break
            else:
                continue
                
        continue
    else:
        print("no receive")
        continue
 