def conversion(n,b):
    r=0
    res=""
    c=''
    save=n%b
    while(n>0):
        r=n%b
        if(save!=r):
            break
        n=n//b
        if(b==16):
            if(r>9):
                if(r==10):
                    c='A'
                elif(r==11):
                    c='B'
                elif(r==12):
                    c='C'
                elif(r==13):
                    c='D'
                elif(r==14):
                    c='E'
                elif(r==15):
                    c='F'
                res=c+res
            else:
                res=str(r)+res
        else:
            res=str(r)+res
    if(n==0):
        return res
    else:
        return -1


def Gen_Bres(n):
    fich=open("F_Brésilien.dat","a+")
    for i in range(2,17):
        rs=conversion(n,i)
        if(rs!=-1):
            break

    if rs!=-1:
        fich.write("{} est un nombre brésilien car {}=({}){}\n".format(n,n,rs,i))
    else:
        fich.write("{} n'est pas brésilien\n".format(n))
    fich.close()

def main():
    #n=int(input("Donnez un entier:"))
    #b=int(input("Donnez une base:"))
    #rs=conversion(n,b)
    #if(rs!=-1):
    #    print("{}=({}){}".format(n,rs,b))
    #else:
    #    print("le nombre n'est pa brésilien")
    file=open("Nombres.txt","r")
    for ligne in file:
        Gen_Bres(int(ligne))
    file.close()
if __name__=="__main__":
    main()