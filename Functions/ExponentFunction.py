# Basic Exponent
print(2**4) # 2^4 = 16

# function calling
def raise_to_power(base, power):
    print(base**power)

raise_to_power(4,2)

# Function with loop
def exp(base, power):
    result = 1
    for a in range(power):
        result = result*base
    return result

print(exp(2, 8))