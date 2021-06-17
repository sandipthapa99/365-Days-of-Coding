list1 = [1,2,3,5,7,11,-1,-6]
list2 = [-2,-3,-5,-7,-11,-1,-6]
list3 = [0,1]
mylist = [list1,list2,list3]

def missing_value(list):
    list.sort()
    while not list[0] >=1:
        list.pop(0)
        if not list:
            list.append(0)
            break
    if list[0] !=1:
        print("Missing smallest value: 1")
    else:
        for i in range(len(list)-1):
            if list[i+1]== list[i]+1: 
                pass
            else:
                print("Missing smallest value: {}".format(list[i]+1))
                break
        else:
            print("Missing smallest value:",list[-1]+1)

for sublists in mylist:
    missing_value(sublists)

# =======
# Result:
# ====================================================================
# Missing smallest value: 4
# Missing smallest value: 1
# Missing smallest value: 2
# ====================================================================