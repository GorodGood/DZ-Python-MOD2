my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
inx = 0
while inx < len(my_list):
    if my_list[inx] > 0:
        print(my_list[inx])
        inx += 1
        continue
    elif my_list[inx] == 0:
        inx += 1
    else:
        print()
        break


