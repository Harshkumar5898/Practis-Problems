List = input(" - Enter a list of food - \n")
Food_List = List.split(',')
another = Food_List.copy()

Food_List.reverse()
print(Food_List)


print(Food_List[::-1])

a = -1
for i in range(len(Food_List)):
    Food_List[i] = another[a]
    a -= 1


print(Food_List)
