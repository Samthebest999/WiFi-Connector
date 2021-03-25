import os
import time
os.system('netsh wlan show profile')
profile = input("Which Profile do you choose?")
ssid = input("What is the name of the Wi-Fi Network you are trying to connect to?")
profileiq = "\"" + profile + "\""
ssidiq = "\"" + ssid + "\""
print("Ok")
time.sleep(1)
print("Connecting.")
time.sleep(1)
print("\n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n "
      " \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  ")
time.sleep(1)
print("Connecting..")
time.sleep(1)
print("\n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n "
      " \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  ")
time.sleep(1)
print("Connecting...")
time.sleep(1)
os.system("netsh wlan connect ssid=" + ssidiq + " name=" + profileiq + " interface=Wi-Fi")
time.sleep(3)
