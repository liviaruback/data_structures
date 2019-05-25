# Function to calculate the Nth fibonacci number, using a list (extra memory).   leetcode log: faster than 41% runtime    memory usage: less than 11%
def fibo1(n):

	if n == 0: return 0
	if n <= 2: return 1

	fibo = []
	for i in range(1,n+1):
		if i<=2:
			fibo.append(1)
		else:
			fibo.append(fibo[-1]+fibo[-2])

	return fibo[-1]

# Function to calculate the Nth fibonacci number, with no extra memory, using 3 pointers    leetcode log:  faster than 96% runtime    memory usage: less than 50%
# fibo = [0,1,1,2,3,5,8,...]
def fibo2(n):

	if n == 0: return 0
	if n <= 2: return 1

	previousPrevious = 0
	previous = 0
	current = 1
	for i in range(2,n+1):
		previousPrevious = previous # move one ahead
		previous = current # move one ahead
		current = previousPrevious + previous # sum up the last 2

	return current

# Recursive solution    leetcode log:  faster than 16% runtime    memory usage: less than 6% : the worst performance
# fibo = [0,1,1,2,3,5,8,...]
def fibo3(n):

	if n == 0: return 0
	if n == 1: return 1

	return fibo3(n-1)+fibo3(n-2)

# Recursive solution with Memoization   leetcode log:  faster than 16% runtime    memory usage: less than 6% : the worst performance
# fibo = [0,1,1,2,3,5,8,...]
fibonacci_cache = {}

def fibo4(n):

	if n in fibonacci_cache:
		return fibonacci_cache[n]

	if n == 0: 
		value = 0
	if n == 1: 
		value = 1

	value = fibo3(n-1)+fibo3(n-2)
	fibonacci_cache[n] = value

	return value


print("Fibo of 35:", fibo1(35))
print("Fibo of 35:", fibo2(35))
print("Fibo of 35:", fibo3(35))
print("Fibo of 35:", fibo4(35))
