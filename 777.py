import smbus
import time
a=0
addr=0x21
PCA9535_OUTPUT=0
PCA9535_INPUT=1
FND=[0x88,0xC6,0x86,0x8E,0x89,0xF1,0xC7,0xC0,0x8C,0x92,0xC1]
BUS=smbus.SMBus(1)
b=[0,1,2,3,4,5]
while True:
    for i in range(6):
        BUS.write_word_data(addr, 0x03, 0x00)
        BUS.write_word_data(addr, 0x02, FND[b[i]])
        BUS.write_word_data(addr, 0x03, (1<<i))
        b[i]=b[i]+1
        if(b[i]==10):
            b[i]=0
    time.sleep(1)
