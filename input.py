# Input :
# x k
# Polynomial


# function to ensure user passed 2 int as input for x and k
def checkResult(x, k, poly): 
    poly = eval(poly)
    return poly == k

xandk = list(map(int, input().split()))

poly = input()

# if user passed more than two int as x and k, function will ignore it
print(checkResult(xandk[0], xandk[1], poly))
