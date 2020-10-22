##
## https://www.hackerrank.com/challenges/python-string-formatting/problem?h_r=next-challenge&h_v=zen
##

def print_formatted(n):
    wdth = len(str(bin(n)[2:]))
    for i in range (1, n+1):
        x_decimal = (str(i))
        x_octal = (str(oct(i)))[2:]
        x_hex = (str(hex(i)))[2:]
        x_binary = (str(bin(i)))[2:]



        x_decimal = x_decimal.rjust(wdth-1 , " ")
        x_octal = x_octal.rjust(wdth, " ")
        x_hex =  x_hex.rjust(wdth, " ")
        x_binary = x_binary.rjust(wdth, " ")



        output = "{} {} {} {}".format(x_decimal,x_octal,x_hex,x_binary)
        print (output)



if __name__ == "__main__":
    n = int(input())
    print_formatted(n)