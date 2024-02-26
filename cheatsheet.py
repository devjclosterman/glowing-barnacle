lst = [1, 2, 3]

length = len(lst) # length = 3
first = lst[0]  # first_element = 1
sublist = lst[1:3] # sublist = [2, 3]

lst.append(4)   # [1, 2, 3, 4]
lst.clear()   # []
new_lst = lst.copy() #[1, 2, 3, 4] (shallow copy)
lst.extend([5, 6]) #[1, 2, 3, 4, 5, 6]
lst.insert(1, 4) #[1, 4, 2, 3]
lst.pop() #[1, 2]
lst.remove(2) #[1, 3]
del lst[0]  