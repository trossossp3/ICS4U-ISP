f = open("input.txt", "w")
f.close()

while True: 
    f = open("input.txt", "w")
    cat = input()
    f.write(cat+"\n")
    f.close()

    while True:
        f=open("input.txt","r+")
        line = f.readline()
        f.close()
        if(line[:2]=="**"):
            print(line)
            break
    
   
   
