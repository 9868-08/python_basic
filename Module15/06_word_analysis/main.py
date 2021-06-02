# Define the custom function to find element in the list
def findElement(listName, searchElement):
  # Read the list using loop
  for value in listName:
  # Check the element value is equal to the search value or not
    if value == searchElement:
      return True

    # Return false if no match found
    return False

input_word = 'лава'
output=[]
letter_count = 0
non_uniq_count = 0
count_inside = 0
count_outside = 0
symbols = []
for symbol_outside in input_word:
    if symbol_outside not in input_word:  # если символа нет в списке
        symbols.append(sym)
print(symbols)
