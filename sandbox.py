def foo ():
    print "Hello World"

foo ()

var = "comme"

def woo(x):
    print var,
    print x,
    
woo ("ci,")
woo ("ca.")



def factorial(n):
    prod = 1
    for i in range(1, n+1):
        prod = prod * i
    return prod

# y = factorial(2)
# print y

# y = factorial(5)
# print y

# y = factorial(20)
# print y

# y = factorial(6000)
# print y

# y = factorial(100000)
# print y


    
def f(x):
    return x**2 - 4*x + 4
least = f(-20)
for z in range(-20,20):
        if f(z) < least:
                least = f(z)
                leastx = z
print leastx