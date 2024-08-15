def encry():
    import random
    import string
    t=input("Enter the message:- ")
    a=t.split()
    n=int(input("Enter the encryption key:- "))
    b=[]
    for i in a:
        if(len(i)>=3):
            y=''.join(random.choices(string.ascii_letters+string.digits ,k=(n*2)))
            x=y[:n]+i[1:]+i[0]+y[-n:]
            b.append(x)
        else:
            c=i[::-1]
            b.append(c)
    print(" ".join(b)+"\n")
    mains()

def decry():
    t=input("Enter the message:- ")
    a=t.split()
    n=int(input("Enter the decryption key:- "))
    b=[]
    for i in a:
        # print(i)
        if(len(i)>=3):
            y=i[n:-n]
            x=y[-1]+y[:-1]
            b.append(x)
        else:
            c=i[::-1]
            b.append(c)
    print(" ".join(b),'\n')
    mains()

def mains():
    print("""press 1 for Encrypt
press 2 for Decrypt
press anything for quit or exit""")
    en=(input("Press:- "))
    if en=='1':
        encry()
    elif en=='2':
        decry()
    else:
        print("Bye")

mains()