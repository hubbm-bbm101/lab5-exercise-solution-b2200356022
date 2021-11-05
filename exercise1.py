N = int(input("Please enter a number: "))
sum_odd = 0
sum_even = 0
even_ns = 0

for n in range(1, N + 1):
    if n % 2 != 0:
        sum_odd += n
    else:
        sum_even += n
        even_ns += 1

print("Sum of odd numbers is", sum_odd, "and average of even numbers is", sum_even/even_ns)
