cars = ["ford", "toyota", "nissan"]
print(cars)
cars.sort()#sort lists lists alphabetically, this is a permanent change, not temporary to the list
print(cars)
cars.sort(reverse=True)#this will sort the cars in reverse alphabetical order
print(cars)
print("This is the sorted list of cars")
print(sorted(cars))#this will present the items in sorted order, without changing the actual value of the list
print("\n")
print("This is the actual list of cars")
print(cars)

cars.reverse()#this will permanently reverse the order of the list, not alphabetically
print(cars)

print("There are " + str(len(cars)) + " cars on the list!")
#len(list) will give back the length of items on the list


