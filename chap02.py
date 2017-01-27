# a graceful method for adding values to dictionary keys even if the key is missing from dictionary
word_counts = {}
for word in document:
  previous_count = word_counts.get(word, 0)
  word_counts[word] = previous_count + 1

# an even better method for doing the above is using default dict
# they can be initialized using some default initial value
from collections import defaultdict
# here we have initiaized the defaultdict to give zero value to any key created for the first time
word_counts = defaultdict(int) # int() produces 0
for word in document:
  word_counts[word] += 1

# can also initialize new keys with empty dicts
dd_list = defaultdict(list)
dd_list[2].append(1) # now dd_list contains {2: [1]}

# Counter is a very useful data type in collections
# converts a list of values to a value -> count mapping
from collections import Counter
c = Counter([0, 1, 2, 0])
# c is basically a dict {0:2, 1:1, 2:1}
# this collection is very useful for creating histograms

# most_common is another useful method here
# print the 10 most common words and their counts
for word, count in word_counts.most_common(10):
print word, count


s = some_function_that_returns_a_string()
if s:
first_char = s[0]
else:
first_char = ""

# an easier way to do the above
first_char = s and s[0]


Python has an all function, which takes a list and returns True precisely when every
element is truthy, and an any function, which returns True when at least one element is
truthy:
all([True, 1, { 3 }]) # True
all([True, 1, {}]) # False, {} is falsy
any([True, 1, {}]) # True, True is truthy
all([]) # True, no falsy elements in the list
any([]) # False, no truthy elements in the list


# sorting in python
# default sorting is smallest to largest
x = [4,1,2,3]
y = sorted(x) # is [1,2,3,4], x is unchanged
x.sort() # now x is [1,2,3,4]

# sort the list by absolute value from largest to smallest
x = sorted([-4,1,-2,3], key=abs, reverse=True) # is [-4,3,-2,1]

# basic list comprehension
even_numbers = [x for x in range(5) if x % 2 == 0] # [0, 2, 4]

# slightly complex list comprehension
increasing_pairs = [(x, y) # only pairs with x < y,
for x in range(10) # range(lo, hi) equals
for y in range(x + 1, 10)] # [lo, lo + 1, ..., hi - 1]

# we can create generators using () instead of [] in list comprehensions

# randomness
import random
four_uniform_randoms = [random.random() for _ in range(4)]
# [0.8444218515250481,    # random.random() produces numbers
# 0.7579544029403025,     # uniformly between 0 and 1
# 0.420571580830845,      # it's the random function we'll use
# 0.25891675029296335]    # most often

# we can specify the seed of the random variable 
# in order to produce deterministic results
random.seed(10)

# choose a random no from a range
# note that this range can be mapped to any other linear range through a
# series of simple arithmetic operations
random.randrange(4, 8)     # range is [4, 8) all ints

# use the shuffle function to return a random permutation of a list
up_to_ten = range(10)
random.shuffle(up_to_ten)
print up_to_ten
# [2, 5, 1, 9, 7, 3, 8, 6, 4, 0] (your results will probably be different)

# choose an element randomly
my_best_friend = random.choice(["Alice", "Bob", "Charlie"])

# random.sample(list, num_elements) to choose a sample without replacement
lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6) # [16, 36, 10, 6, 25, 9]


# to choose a sample with replacement
four_with_replacement = [random.choice(range(10)) for _ in range(4)]

# map can be useful in creating new lists using an existing one
new_list = map(some_fun(), old_list)

# use zip to merge multiple lists into a single list of tuples
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
zip(list1, list2) # is [('a', 1), ('b', 2), ('c', 3)]
# if the lists are of different lengths, zip stops as soon as the first list ends

# we can also using unzip
pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)

# * performs argument unpacking


