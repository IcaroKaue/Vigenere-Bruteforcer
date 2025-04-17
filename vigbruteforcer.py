# VIGENERE BRUTEFORCER

alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
klist = []
txtlist = []

def a1z26(ct="", k=""):
    ct = list(ct.upper())
    k = list(k.upper())
    ctindex = []
    kindex = []
    for i in ct:
        index = alpha.find(i)
        ctindex.append(index)
    for i in k:
        index = alpha.find(i)
        kindex.append(index)      
    return ctindex, kindex

def vncoder(ct="", k=""):
    ct, k = a1z26(ct, k)
    cttemp = []
    i = 0
    while i < len(ct):
        shift = k[i%len(k)]
        ct[i] = (ct[i] + shift)%26
        i += 1
    for x in ct:
        cttemp.append(alpha[x])
    ct = ''.join(cttemp)
    return ct

def vecoder(ct="", k=""):
    ct, k = a1z26(ct, k)
    cttemp = []
    i = 0
    while i < len(ct):
        shift = k[i%len(k)]
        ct[i] = (ct[i] - shift)%26
        i += 1
    for x in ct:
        cttemp.append(alpha[x])
    ct = ''.join(cttemp)
    return ct

def brute(ct, listname, decoder):
    listname = listname+".txt"
    txt = open(listname,'r')
    keytxt = txt.read()
    txt.close()
    keytxt = keytxt.split()
    for x in keytxt:
        if decoder:
            print(f"Key {x}{' '*(len(max(keytxt))-len(x))} = {vecoder(ct, x)}")
        else:
            print(f"Key {x}{' '*(len(max(keytxt))-len(x))} = {vncoder(ct, x)}")

def sep():
    print('-'*50)

def main():
    sep()
    print("MASS BRUTEFORCER FOR VIGENERE WITH CUSTOM WORDLIST")
    sep()
    sep()
    choice = int(input(f"Do you want to DECODE or ENCODE? \n1) Decode \n2) Encode \n{'-'*50}\nType the number corresponding to your choice: "))

    if choice == 1:
        ciphertext = input("Please enter your ciphertext: ")
        txtname = input("Please enter the name of your keylist (NOTE: IT SHOULD BE IN THE SAME DIRECTORY AS THIS FILE): ")
        sep()   
        print("BATCH DECODER")
        sep()
        brute(ciphertext, txtname, True)
        sep()

    elif choice == 2:
        ciphertext = input("Please enter your ciphertext: ")
        txtname = input("Please enter the name of your keylist (NOTE: IT SHOULD BE IN THE SAME DIRECTORY AS THIS FILE): ")
        sep()
        print("BATCH ENCODER")
        sep()
        brute(ciphertext, txtname, False)
        sep()
    else:
        print("Input malformed. Either press 1 for DECODING or 2 for ENCODING. To exit, press CTRL+C")
        main()

main()
    


    


    