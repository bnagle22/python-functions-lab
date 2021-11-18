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
# Works for any length of b:
# def occurrences(a, b):
#   new_str = a.replace(b, '')
#   count = (len(a) - len(new_str)) / len(b)
#   return int(count)

# Works if b has length 1, 2, or 3:
def occurrences(a, b):
  count = 0
  chars = len(b)
  if chars == 1:
    for i in range(len(a)):
      if (a[i]) == b:
        count += 1
  elif chars == 2:
    for i in range(len(a)-1):
      if (a[i]+ a[i + 1]) == b:
        count += 1
  elif chars == 3:
    for i in range(len(a)-2):
      if (a[i] + a[i + 1] + a[i + 2]) == b:
        count += 1

  return count

# print(occurrences('fleeep floop fleeep', 'fl'))

# Ex 4
def product(*args):
  product = 1
  for i in args:
    product *= i
  return product


# function calls
# print(sum_to(6))
# print(largest([10, 4, 15, 2]))
# print(occurrences("fleeep fleep", 'eee'))
# print(product(3, 4, 2, 10))