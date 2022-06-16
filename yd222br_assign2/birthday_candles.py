
age = 1 
boxes_buy = 0
boxes_total = 0
candles = boxes_buy * 24
candles_left = 0

while age <= 100:
    while candles_left < age:
        boxes_buy += 1
        boxes_total += 1
        candles_left += 24
    if boxes_buy != 0:
        print("Before birthday ",age,",buy ",boxes_buy," box(es)")
    candles_left = candles_left - age
    age += 1
    boxes_buy = 0
print(f"Total number of boxes: {boxes_total}, Remaining candles: {candles_left}")


    


    
    
    
    
    
    # if age <= 100:
    #     while candles - age > 0:
    #         candles = candles - age
    #         age += 1
    #         if candles - age < 0:
    #             flag = True
    #             if flag == True:
    #                 candles += 24
    #                 if candles + 24 - age > 0:
    #                     flag = False
    #                     age += 1
    #                     boxes += (candles // 24)
    #                     print("Before birthday ",age,",buy ",boxes," box(es)")
    #                 else:
    #                     candles += 24
        
        
            
            
    

    # candles += 24
    # if flag == True:
    #     while candles - age <= 0:
    #         boxes += 1
    #         candles += 24
    #         print("Before birthday ",age,",buy ",boxes," box(es)")