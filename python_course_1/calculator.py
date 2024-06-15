def convert(number):
    return bin(number)[2:], oct(number)[2:], hex(number)[2:].upper()

n = int(input())
print(*convert(n))