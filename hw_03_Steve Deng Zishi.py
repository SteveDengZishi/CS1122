''' Steve Deng Zishi
    zd475
    hw3
'''
#2
def dec_to_bin(dec_num):
    print(bin(dec_num)[2:])

#3
def hex_to_chr(hex_num):
    print(chr(eval(str(hex_num))), end ='')

#4
def bin_to_hex(bin_num):
    print(hex(int(str(bin_num), 2)))

#5
def oct_to_dec(oct_num):
    sum = 0
    counter = 0
    for i in range (len(str(oct_num))-1, -1, -1):
            sum += int(str(oct_num)[counter])*8**i
            counter += 1
    print(sum)
        

def main():
    num_lst = [57, 123, 85, 38]
    for dec_num in num_lst:
        dec_to_bin(dec_num)
    print("\n")
        
    lst_hex_1 =[0x41,0x53,0x43,0x49,0x49,0x20,0x77,0x68,0x61,0x74,0x20,0x79,0x6f,0x75,0x20,0x64,0x69,0x64,0x20,0x74,0x68,0x65,0x72,0x65]
    lst_hex_2 =[0x39,0x41,0x4d,0x20,0x69,0x73,0x20,0x74,0x6f,0x6f,0x20,0x65,0x61,0x72,0x6c,0x79,0x20,0x66,0x6f,0x72,0x20,0x63,0x6c,0x61,0x73,0x73]
    lst_hex_3=[0x43,0x6f,0x6d,0x70,0x75,0x74,0x65,0x72,0x73,0x20,0x61,0x72,0x65,0x20,0x6d,0x61,0x67,0x69,0x63]
    lst_hex_4=[0x57,0x68,0x61,0x74,0x20,0x74,0x68,0x65,0x20,0x68,0x65,0x78,0x3f]

    lst_hex=[lst_hex_1,lst_hex_2,lst_hex_3,lst_hex_4]
    for i in range (len(lst_hex)):
        for hex_num in lst_hex[i]:
            hex_to_chr(hex_num)
        print("\n")

    lst_bin = [1011101011101101111010101101,\
               11001010111111101111101011001110,\
               10111110111011111101000000001101,\
            11111111111111111001000001100010]
    
    for bin_num in lst_bin:
        bin_to_hex(bin_num)
    print("\n")

    oct_lst = [10, 42, 77, 113]

    for oct_num in oct_lst:
        oct_to_dec(oct_num)


main()

    