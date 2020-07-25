def print_formatted(number):
    w=len(bin(number)[2:])
    l,l1=len(str(bin(number))),len(str(number))
    for i in range(1,number+1):
        b,c,d=str(oct(i)),str(hex(i)),str(bin(i))
        c=c.upper()
        print(str(i).rjust(w,' '),b[2:].rjust(w,' '),c[2:].rjust(w,' '),d[2:].rjust(w,' '))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
