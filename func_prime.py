# file name: func_prime.py

def prime(num):
    num_set = list(range(2, num + 1))
    prime_set = num_set[:]
    
    for a in num_set:
        for b in num_set:
            if (b in prime_set) and (a != b and b % a == 0):
                prime_set.remove(b)
         
    print(prime_set)
    return prime_set

if __name__ == '__main__':
    a=prime(int(input('Input the last number of range what you want! ')))
