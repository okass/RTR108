from math import cos

def main():
    if (2 > 1):
        print("big")
    else:
        print("main function")
    
    inp = input()
    try:
        floatp = float(inp)
        print(floatp)
    except:
        print("not a float")

    if 2 > 1 and 3 > 1 and 4 > 1:
        print("yes")
    else:
        print("no")
    
    print(cos(1))
    #for i=1,10:
    #    print(i)

main()

