from random import choice
from timer import Timer

def binary_search(search_term, input_list):

  low = 0
  high = len(input_list) - 1

  steps = 0

  while low <= high:
    
    half = (low + high) / 2
    attempt = input_list[half]

    if attempt == search_term:
      return attempt
    if attempt >  search_term:
      high = half - 1
    elif attempt < search_term:
      low = half + 1


def simple_search(search_term, input_list):

  for item in input_list:
    if item == search_term:
      return search_term

test_list = range(1,100)
search = choice(test_list)

with Timer() as t:
  result = binary_search(search, test_list)
print('Binary Search in range of 100 for %s took %.07f sec, and result was %s' % (search, t.interval, result))

with Timer() as t:
  simple_search(search, test_list)
print('Simple Search in range of 100 for %s took %.07f sec, and result was %s' % (search, t.interval, result))


test_list = range(1,1000)
search = choice(test_list)

with Timer() as t:
  result = binary_search(search, test_list)
print('Binary Search in range of 1000 for %s took %.07f sec, and result was %s' % (search, t.interval, result))

with Timer() as t:
  simple_search(search, test_list)
print('Simple Search in range of 1000 for %s took %.07f sec, and result was %s' % (search, t.interval, result))


test_list = range(1,10000)
search = choice(test_list)

with Timer() as t:
  result = binary_search(search, test_list)
print('Binary Search in range of 10000 for %s took %.07f sec, and result was %s' % (search, t.interval, result))

with Timer() as t:
  simple_search(search, test_list)
print('Simple Search in range of 10000 for %s took %.07f sec, and result was %s' % (search, t.interval, result))


test_list = range(1,100000)
search = choice(test_list)

with Timer() as t:
  result = binary_search(search, test_list)
print('Binary Search in range of 100000 for %s took %.07f sec, and result was %s' % (search, t.interval, result))

with Timer() as t:
  simple_search(search, test_list)
print('Simple Search in range of 100000 for %s took %.07f sec, and result was %s' % (search, t.interval, result))


test_list = range(1,1000000)
search = choice(test_list)

with Timer() as t:
  result = binary_search(search, test_list)
print('Binary Search in range of 1000000 for %s took %.07f sec, and result was %s' % (search, t.interval, result))

with Timer() as t:
  simple_search(search, test_list)
print('Simple Search in range of 1000000 for %s took %.07f sec, and result was %s' % (search, t.interval, result))

test_list = range(1,10000000)
search = choice(test_list)

with Timer() as t:
  result = binary_search(search, test_list)
print('Binary Search in range of 10000000 for %s took %.07f sec, and result was %s' % (search, t.interval, result))

with Timer() as t:
  simple_search(search, test_list)
print('Simple Search in range of 10000000 for %s took %.07f sec, and result was %s' % (search, t.interval, result))

test_list = range(1,100000000)
search = choice(test_list)

with Timer() as t:
  result = binary_search(search, test_list)
print('Binary Search in range of 100000000 for %s took %.07f sec, and result was %s' % (search, t.interval, result))

with Timer() as t:
  simple_search(search, test_list)
print('Simple Search in range of 100000000 for %s took %.07f sec, and result was %s' % (search, t.interval, result))