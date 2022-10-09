cars = ["ford", "toyota", "nissan"]
print(cars)
print(cars[0]) # this pulls out the first item in the cars list, ford
print(cars[1].title()) #pass the value of cars[1] to title function, then that to the print function
print(cars[-1]) #-1 will always be the last item in a list, in Python
message = "My first car was a " + cars[0] + "!"
print(message)

cars[0] = "ram" #changing values in a list
print(cars[0])

cars.append("mitsubishi") #append adds an item to a list at the back of the list
print(cars)

cars.insert(0, "kia") #insert will add a variable to a list, at the index location listed before it
print(cars)

del cars[1]#this deletes the value at 1 of the list
print(cars)

popped_cars = cars.pop()#this will remove the item from the end of the list and allow you to work with it
print(cars)
print(popped_cars)

first_popped = cars.pop(0)#this will pop the first item in the list
print(cars)
print(first_popped)

cars.remove("nissan")# this will remove a specific value from a list, if it exists
print(cars)
