import random

print("Frequency table (sum,count) for rolling two dices 10000 times")
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
count10 = 0
count11 = 0
lst = [[2,count1],[3,count2],[4,count3],[5,count4],[6,count5],[7,count6],[8,count7],[9,count8],[10,count9],[11,count10],[12,count11]]
for i in range (1,10001):
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    sum = dice_1 + dice_2
    if sum == 2:
        count1 += 1
        lst[0][1] = count1
        sum = 0
    elif sum == 3:
        count2 += 1
        lst[1][1] = count2
        sum = 0
    elif sum == 4:
        count3 += 1
        lst[2][1] = count3
        sum = 0
    elif sum == 5:
        count4 += 1
        lst[3][1] = count4
        sum = 0
    elif sum == 6:
        count5 += 1
        lst[4][1] = count5
        sum = 0
    elif sum == 7:
        count6 += 1
        lst[5][1] = count6
        sum = 0
    elif sum == 8:
        count7 += 1
        lst[6][1] = count7
        sum = 0
    elif sum == 9:
        count8 += 1
        lst[7][1] = count8
        sum = 0
    elif sum == 10:
        count9 += 1
        lst[8][1] = count9
        sum = 0
    elif sum == 11:
        count10 += 1
        lst[9][1] = count10
        sum = 0
    elif sum == 12:
        count11 += 1
        lst[10][1] = count11
        sum = 0
for i in range (0,11):
    print(f"{lst[i][0]}      {lst[i][1]}")
   




#     lst = [0,0,0,0,0,0,0,0,0,0,0]
#     count1 = 0
#     count2 = 0
#     count3 = 0
#     count4 = 0
#     count5 = 0
#     count6 = 0
#     count7 = 0
#     count8 = 0
#     count9 = 0
#     count10 = 0
#     count11 = 0
#     dice_1 = random.randint(1,6)
#     dice_2 = random.randint(1,6)
#     sum = dice_1 + dice_2
#     if sum == 2:
#         count1 += 1
#         lst[0] = count1
#         sum = 0
#     elif sum == 3:
#         count2 += 1
#         lst[1] = count2
#         sum = 0
#     elif sum == 4:
#         count3 += 1
#         lst[2] = count3
#         sum = 0
#     elif sum == 5:
#         count4 += 1
#         lst[3] = count4
#         sum = 0
#     elif sum == 6:
#         count5 += 1
#         lst[4] = count5
#         sum = 0
#     elif sum == 7:
#         count6 += 1
#         lst[5] = count6
#         sum = 0
#     elif sum == 8:
#         count7 += 1
#         lst[6] = count7
#         sum = 0
#     elif sum == 9:
#         count8 += 1
#         lst[7] = count8
#         sum = 0
#     elif sum == 10:
#         count9 += 1
#         lst[8] = count9
#         sum = 0
#     elif sum == 11:
#         count10 += 1
#         lst[9] = count10
#         sum = 0
#     elif sum == 12:
#         count11 += 1
#         lst[10] = count11
#         sum = 0
# print(lst)