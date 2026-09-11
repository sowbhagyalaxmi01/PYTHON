n = int(input())
day = input()

days = ["sun", "mon", "tue", "wed", "thur", "fri", "sat"]

index = days.index(day)

d = days[(index + n) % 7]

print(d)


#fibonacci series
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
n=int(input())
print(fib(n))
