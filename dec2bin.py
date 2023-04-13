# file name: dec2bin.py

dec_num = int(input('이진수로 바꿀 수를 입력하세요. '))

bin_num=[]

while dec_num > 1:
    dec_num, b = divmod(dec_num,2)
    bin_num.append(b)

bin_num.append(dec_num)
bin_num=reversed(bin_num)

print(list(bin_num))
        
