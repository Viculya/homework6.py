my_dict={"Иванов":1951,"Петров":1952,"Сидоров":1953}
print ('Dict: ',my_dict)
print('Existion value: ',my_dict.get("Иванов"))
print('Not existing value:',my_dict.get("Семенов"))
my_dict.update({"Семенов":1960,"Антонов":1961})
a=my_dict.pop("Иванов")
print('Deleted value:',a)
print('Modifiel dictionary: ',my_dict)
my_set={1,2,3,0,2,3,False,"Sacha","Max","Max"}
print('Set: ',my_set)
my_set.add(6)
my_set.discard("Max")
print('Modified set: ',my_set)