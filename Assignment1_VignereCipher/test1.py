rt="Time 47598347 ^&*() dvnvdmv dnvd ndvn dkkdmk"   ###i
PLAINTEXT="ABCDROHITPATIDARJITUTTAMS"                 ###k 
plain=""
key=rt
key=key.lower()
c=chr(ord(key[0])-32)
print(key)
for i in range(1,len(rt)):
     c=c+key[i]
print(f"Key:{c},")
k=0
for i in range(0,len(rt)):
    if rt[i]>='a' and rt[i]<='z':                 ##
            C=chr(ord(PLAINTEXT[k])+32)
            plain=plain+C
            k=k+1
    elif rt[i]>='A' and rt[i]<='Z' :
            plain=plain + PLAINTEXT[k]
            k=k+1
    else :
          plain=plain + rt[i]
print("plain:",plain)
                  
          