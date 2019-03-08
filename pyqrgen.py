#!/user/bin/python
# -*- coding: UTF-8 -*-

#import QRCode from pyqrcode
import pyqrcode
import time
from pyqrcode import QRCode



print"                                                               "
print"	██████╗ ██╗   ██╗ ██████╗ ██████╗  ██████╗ ███████╗███╗   ██╗"
print"	██╔══██╗╚██╗ ██╔╝██╔═══██╗██╔══██╗██╔════╝ ██╔════╝████╗  ██║"
print"	██████╔╝ ╚████╔╝ ██║   ██║██████╔╝██║  ███╗█████╗  ██╔██╗ ██║"
print"	██╔═══╝   ╚██╔╝  ██║▄▄ ██║██╔══██╗██║   ██║██╔══╝  ██║╚██╗██║"
print"	██║        ██║   ╚██████╔╝██║  ██║╚██████╔╝███████╗██║ ╚████║"
print"	╚═╝        ╚═╝    ╚══▀▀═╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝"
print"                                                         ____________ "
print"	                                                 |by Venom-7|"


print "import your link to generate the QR"

# string which represent the QR code
link = raw_input("~$ ")

print "[+] generating your QRcode"
time.sleep(0.5)
print "[+] almost there..."
time.sleep(0.5)
print "[+] done!"

#generate QR code
url = pyqrcode.create(link)

#create and save the png file naming "myqr.svg"
url.svg("myqr.svg", scale = 10)

print "[!] open the 'myqr.svg' to get your QRcode."
