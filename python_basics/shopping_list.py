"""
a mock shopping list program
"""


# make a list that will hold on to our items
shopping_list = []

# print out instructions on how to use the app
print("What should we pick up at the store? ")
print("Enter 'DONE' to stop adding items.")

while True:
    # ask for new items
    new_item = input("> ")

    # be able to quit the app
    if new_item == 'DONE':
        break
        
    # add new items to a list
    shopping_list.append(new_item)
    
    
# print out the list

print("Here's your list: ")
for item in shopping_list:
    print(item)