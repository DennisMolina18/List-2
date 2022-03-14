#Combine Sort
def combine_sort1(lst1, lst2):
    result = []
    for value in lst1:
        result.append(value)
        i = len(result)-2
        while i >= 0:
           if value < result[i]:
               result[i+1] = result[i]
           else:
               result[i+1] = value
               break
           i-=1
    for value in lst2:
        result.append(value)
        i = len(result)-2
        while i >= 0:
           if value < result[i]:
               result[i+1] = result[i]
           else:
               result[i+1] = value
               break
           i-=1
    return result
  #Uncomment the line below when your function is done  


print(combine_sort1([4, 10, 2, 5], [-10, 2, 5, 10]))