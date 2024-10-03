import pyqrcode
from PIL import Image
link = input("Enter anything to generate QR code: ")
qr_code = pyqrcode.create(link)
qr_code.png("QRcode.png", scale=5)
Image.open("QRcode.png") 