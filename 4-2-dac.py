import RPi.GPIO as RG
import time
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
    if d=='':
        return(0)
    else:
        return(int(d))
try:
    a=int(input())
    while(True):
        for k in range(256):
            a1=dv(k)
            for i in range(8):
                RG.output(dac[7-i],a1%10)
                a1=a1//10
            time.sleep(a/512)
        for k in range(255,-1,-1):
            a1=dv(k)
            for i in range(8):
                RG.output(dac[7-i],a1%10)
                a1=a1//10
            time.sleep(a/512)
finally:
    RG.output(dac,0)
    RG.cleanup()  