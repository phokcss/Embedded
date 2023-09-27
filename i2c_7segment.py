import smbus
import time
PCA9535_OUTPUT=0
PCA9535_INPUT=1
FND=[0xC0,0xF9,0xA4,0xB0,0x99,0x92,0x83,0xD8,0x80,0x90]
_MODE=[0xFF,0xFF]
_VALUE=[0xFF,0xFF]
BUS=smbus.SMBus(1)

def time_check():
    while True:
        now =time.localtime()
        time_list=[]
        now_hour=str(now.tm_hour)
        if len(now_hour)==1:
            time_list.append(0)
            time_list.append(now_hour)
        elif len(now_hour)==2:
            for i in range(0,len(now_hour)):
                time_list.append(now_hour[i])
        now_min=str(now.tm_min)
        if len(now_min)==1:
            time_list.append(0)
            time_list.append(now_min)
        elif len(now_min)==2:
            for i in range(0,len(now_min)):
                time_list.append(now_min[i])
        now_sec=str(now.tm_sec)
        if len(now_sec)==1:
            time_list.append(0)
            time_list.append(now_sec)
        elif len(now_sec)==2:
            for i in range(0,len(now_sec)):
                time_list.append(now_sec[i])

        return time_list
def pca9535_pin_mode(addr,port,pin,mode):
    if(mode==1):
        _MODE[port] |=(1<<pin)
    else:
        _MODE[port] &= ~(1 <<pin)
    BUS.write_word_data(addr,(port +0x06),_MODE[port])
    print("pin:{:#010b}".format(port + 0x06),
          "mode:{:#010b}".format(_MODE[port]))

def fnd_write(addr,num):
    n=[(num%1000000)//100000,
        (num%100000)//10000,
        (num%10000)//1000,
        (num%1000)//100,
        (num%100)//10,
        (num%10)//1,
    ]
    for i in range(6):
        BUS.write_word_data(addr,0x03,0x00)
        BUS.write_word_data(addr, 0x02, FND[n[i]])
        BUS.write_word_data(addr,0x03,(1<<i))
def main():
    addr=0x21
    try:
        for i in range(8):
            pca9535_pin_mode(addr,0,i,PCA9535_OUTPUT)
            pca9535_pin_mode(addr, 1, i, PCA9535_OUTPUT)
        tmp=[]
        while True:
            time_list=time_check()
            if tmp !=time_list:
                tmp= time_list
                print("now time: %s%s시 %s%s분 %s%s초" %(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5]))
            time_str="%s%s%s%s%s%s"%(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])
            for i in range(10):
                for j in range(1):
                    BUS.write_word_data(addr, 0x03, 0x00)
                    BUS.write_word_data(addr, 0x02, FND[i])
                    BUS.write_word_data(addr, 0x03, 0xFF)
                    time.sleep(0.5)
    except KeyboardInterrupt:
        pass
if __name__ =="__main__":
    main()
