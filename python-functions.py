# Ex 1

def sum_to(n):
  sum = 0
  for i in range(1, n+1):
    sum += i
  return sum

# Ex 2

def largest(nums):
  largest = 0
  for i in nums:
    if i > largest:
      largest = i
  return largest

# Ex 3
def occurances(a, b):
  new_str = a.replace(b, '')
  count = (len(a) - len(new_str)) / len(b)
  return int(count)

# Ex 4
def product(*args):
  product = 1
  for i in args:
    product *= i
  return product


# function calls
print(sum_to(6))
print(largest([10, 4, 15, 2]))
print(occurances("fleeep fleep", 'eee'))
print(product(3, 4, 2, 10))