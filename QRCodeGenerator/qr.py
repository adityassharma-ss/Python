import pyqrcode ## import pyqrcode module
import png ## import png module
from pyqrcode import QRCode ## import QRCode from pyqrcode
from PIL import Image ## import Image module from PIL package

link = input("Enter the text/link/description to generate qrcode: ") ## take input from user

qr_code = pyqrcode.create(link) ## create qrcode
qr_code.png("QRCode.png", scale = 5) ## save qrcode as png file

Image.open("QRCode.png") ## open the qrcode image

