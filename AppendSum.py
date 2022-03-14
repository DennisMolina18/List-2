#APPEND SUM

def append_sum(lst):
    sum1 = lst[-2] + lst[-1]
    lst.append(sum1)
    sum2 = lst[-2] + lst[-1]
    lst.append(sum2)
    sum3 = lst[-2] = lst[-1] 
    lst.append(sum3)
    return lst
  
#Uncomment the line below when your function is done
  
print(append_sum([1, 1, 2]))