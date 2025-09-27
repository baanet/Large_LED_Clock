# This file is executed on every boot (including wake-boot from deepsleep)
# On startup the code will connect to the local WiFi
# then get the current UTC time and local Day light saving start and end date are calculated
# the UTC time is combined with the local offset and is compared againts the DST dates and write correct offset to the local file
# the system will then check if the RTC has a valid date / time
# if not the RTC is updated
# normal RTC time creep is handled in the main program
# Add try / except function to code to handle no internet connection

# Version 20250709 @ 16:05

from machine import Pin, SoftI2C
import time
from time import sleep
import sys
import network
import ntptime
from ds3231_gen import *
from web1 import *
import _thread

utcoffset = 10
ntptime.host = "pool.ntp.org"

try:
    
    N1 = network.WLAN(network.STA_IF)
    N1.active(True)
    N1.disconnect()

    f = open('config/wifi_config.txt', 'r') 
    SSID = f.readline()
    SSID = SSID.strip() # Remove unwanted leading and lagging charaters
    print('SSID - ' + SSID)
    PASSWORD = f.readline()
    PASSWORD = PASSWORD.strip() # Remove unwanted leading and lagging charaters
    print('PASSWORD - ' + PASSWORD)
    f.close()
    
    N1.connect("Moto G 5 Plus 9895","Marvin3150")
    #N1.connect(SSID, PASSWORD)#
    #N1.connect("Grove-WiFi","f33dmenow3150")
    #N1.connect("TheGrove24","f33dmenow3150")
    print(" WiFi Connected -",N1.ifconfig())
    sleep(2)
    if N1.isconnected():
        #(ip,gateway,netmask,MAC,ssid)= N1.ifconfig()
        print(" WiFi Connected -",N1.ifconfig())
        #f.write("WiFi Connected \n")
        #get_time()
        
except KeyboardInterrupt:
        print ('Interrupted')
        #sys.exit(0) 

_thread.start_new_thread(web_page, ())
#RTC Pins and setup
sda_pin=Pin(12)
scl_pin=Pin(11)

i2c = SoftI2C(scl=scl_pin, sda=sda_pin)
time.sleep(0.5)

ds = DS3231(i2c)

def chk_rtc(): #check if the RTC hasa valid date/time
    tc=ds.get_time()
    #print(tc)
    if tc[0] == 2000: 
        tc1 = time.localtime(ntptime.time()+(utc_offset*60*60))
        ds.set_time(tc1)
        #print(ds.get_time())
        
def get_dst_dates():
    global sdst, edst, t
    t = time.localtime(ntptime.time())
    print(t)
    y1 = t[0]
    N = 2
    # create a new string of last N characters
    y1 = str(y1)[-N:]
    dd1 = 9
    dd2 = 9

    def month_code():
        global m2, m1
        mc = (0,3,3,6,1,4,6,2,5,0,3,5)
        m2 = mc[m1-1]

    leap=0
    y1 = int(y1)
    y2 = (y1+int(y1/4))%7
    print(y2)
    #Find 1st sunday in October
    d1 = 0
    while dd1 != 0:
        if dd1 != 0:
            m2 = 0 #October
            d1= d1+1
            dd1 = ((y2+m2+6+d1)-leap)%7
            sdst = d1
        else:
            print(d1)

    #Find 1st sunday in April
    d1 = 0
    y1e = int(y1)
    y2e = (y1e+int(y1e/4))%7
    while dd2 != 0:
        if dd2 != 0:
            m2 = 6 #April
            d1= d1+1
            dd2 = ((y2e+m2+6+d1)-leap)%7
            edst = d1
        else:
            print(d1)
        
    print("1st Sun of October in",y1,"is:",sdst)
    print("1st Sun of April in",y1e,"is:",edst)


def get_time(): # gets the current time based on NTP/UTC time
    print(ds.get_time())#time.localtime())
    utctime = ntptime.time()
    print(utctime+utcoffset)
    time_secs = (time.mktime(time.localtime()))# + utcoffset#(3600*11)
    print(time_secs)
    ts1 = time.localtime(utctime+utcoffset)
    print("")
    year, month, day, hour, minute, second, weekday, yearday = time.localtime(time_secs)

    print(f"Date: {day}/{month}/{year}")
    print(f"Time: {hour}:{minute}:{second}")
    #print(ts1)
    #print(ds.get_time())

try:
    #chk_rtc()
    get_time()
    get_dst_dates()
    #f.close()

    if t[1] >= 4:
        if t[2] >= edst:
            utc_offset = 10
            
    if t[1] >= 10:
        if t[2] >= sdst:
            utc_offset = 11
            
    print(utc_offset)
    f = open("utcoffset.py","w")
    f.write("utc_offset = ")
    f.write(str(utc_offset))
    f.close()
    chk_rtc()

except:
    print("no Internet")