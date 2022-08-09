# Given an array of characters where each character represents a fruit tree, you are given two baskets
#  and your goal is to put maximum number of fruits in each basket. The only restriction is that each 
#  basket can have only one type of fruit.

# You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit
#  from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

# Write a function to return the maximum number of fruits in both the baskets.

def totalFruit(fruits):
    max_len = 0
    win_start = 0
    fruit_set = {}

    for win_end in range(len(fruits)):
        end_fruit = fruits[win_end]
        fruit_set[end_fruit] = 1 + fruit_set.get(end_fruit , 0)

        while len(fruit_set) > 2:
            start_fruit = fruits[win_start]
            fruit_set[start_fruit] -= 1
            if fruit_set[start_fruit] == 0:
                del fruit_set[start_fruit]
            win_start += 1

        max_len = max(win_end-win_start+1, max_len)

    print(max_len)


totalFruit(['A', 'B', 'C', 'A', 'C'])