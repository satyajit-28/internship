# # 
# L = []
# L.append(10)
# print(len(L))

# L.append((10, 20, 30))
# print(len(L))


# L.extend([10])
# print(len(L))

L = [10, 20]
L.append([30, 40, 50])


for i in L:
    if type(i) == list:
        print(i[1])
    # if dir(type(i)) == "__iter__":
    #     for j in i:
    #         print(j)
    
    

