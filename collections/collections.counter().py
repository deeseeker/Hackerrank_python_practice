#Task

# Raghu is a shoe shop owner. His shop has  number of shoes.
# He has a list containing the size of each shoe he has in his shop.
# There are N number of customers who are willing to pay x amount of money only if they get the shoe of their desired size.
# Your task is to compute how much money Raghu earned.
from collections import Counter
shoes = int(input())
x = input()
shoe_sizes = [int(x) for x in x.split()]
customers = int(input())
print(shoes,shoe_sizes,customers)
n_shoe_sizes = Counter(shoe_sizes)
print(n_shoe_sizes)
total_earned = 0
for i in range(customers):
    d_shoes_price = [int(x) for x in input().split()]
    d_shoe = d_shoes_price[0]
    price = d_shoes_price[1]
    print(d_shoe,price)

#make the count of the shoe shoe_sizes

    if n_shoe_sizes[d_shoe] > 0:
        total_earned = total_earned + price
        print('Raghu earned:', total_earned)
        new_freq = n_shoe_sizes[d_shoe] - 1
        n_shoe_sizes[d_shoe] = new_freq

        print(n_shoe_sizes)
    else:
        print('we are progressing')
