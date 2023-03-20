import RPi.GPIO as RG
dac=[26,19,13,6,5,11,9,10]
RG.setmode(RG.BCM)
RG.setup(dac,RG.OUT)
def dv(n):
    s=''
    n1=n
    while n1>0:
        s+=str(n1%2)
        n1=n1//2
    d=s[::-1]
    return(int(d))  
try:
    while (True):
        astr=input()
        a=int(astr)
        a1=dv(a)
        if a<0:
            print("i can't")
        elif a>255:
            print("i can't")
        else: 
            if a!=-1:
                for i in range(8):
                    RG.output(dac[7-i],a1%10)
                    a1=a1//10
                print("V:",round(3.3/256*a,2))

        
finally:
    RG.output(dac,0)
    RG.cleanup()