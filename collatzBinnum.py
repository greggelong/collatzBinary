
def collatz(num):
    i =0
    print(i,num)
    while num != 1:
        i+=1
        if num%2==1:
            num = (num*3+1)
        else:
            num = num/2
            
        binpart = str(bin(int(num)))[2:]
        mask= (16 - int(num).bit_length())*"0" # make a mask
        binnum = mask+binpart
        
        
        print(binnum, i, int(num))
        
        
        
collatz(27)