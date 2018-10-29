import random


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True


def encrypt(message, e, n):
    cypher = []
    for character in message:
        # cypher.append(ord(character)**e % n)
        cypher.append(pow(ord(character), e, n))
    return cypher


def decrypt(cyphertext, d, n):
    result = []
    for value in cyphertext:
        # result.append(chr(value**d % n))
        result.append(chr(pow(value, d, n)))
    return "".join(result)


def sum_of_random_values_in_list(some_list):
    sum = 0
    for value in some_list:
        if value * random.randint(1, 10) % 2 == 0:
            sum += value
    return sum


def sum_of_prime_numbers_up_to_n(n):
    sum = 0
    for number in range(2, n+1):
        if is_prime(number):
            sum += number
    return sum


print(sum_of_random_values_in_list([1, 2, 3, 4, 5, 6]))

print(sum_of_prime_numbers_up_to_n(11))

cyphertext = encrypt("test", 73, 589)
print(cyphertext)
print(decrypt(cyphertext,37,589))