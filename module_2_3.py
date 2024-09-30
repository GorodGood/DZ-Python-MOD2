my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
inx = 0
while inx < len(my_list):
    if my_list[inx] > 0:
        print(my_list[inx])
    elif my_list[inx] == 0:
        inx += 1
        continue
    else:
        break
    inx += 1



