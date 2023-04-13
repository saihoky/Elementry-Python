# file name: func_prime2.py

def prime(range_num):
    num_list = list(range(2, range_num + 1))

    index = 0
    while index < len(num_list):
        num = num_list[index]
        num_list = list(filter(lambda x: x == num or x % num, num_list))
        index += 1

    print(num_list)

if __name__ == '__main__':
    a=prime(int(input('Input the last number of a range what you want!  ')))
