## Creating a binary search algorithm 
    # Takes average of all values and divide by 2
    # repeatedly divides by half till target is found

## Steps
# create a function that takes a list and target parameter 
# multiple variables : middle, start, end. Steps needed
# recursion or while loop 
# increase steps every split
# conditions to track target position 


def binary_search(list, element):
    middle = 0 
    start = 0
    end = len(list)
    steps = 0

    while(start<=end):
        print("Step",steps,":",str(list[start:end+1]))

        steps = steps+1
        middle = (start + end) // 2
        
        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle -1
        else:
            start = middle +1

    return -1

my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
target = 9

binary_search(my_list, target)

# while loop has better time complexity than recursions 