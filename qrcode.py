import pyqrcode


# Create the QR Code
qr = pyqrcode.create("www.google.com")

# Save the QR Code as a PNG file
qr.png("qr.png", scale=8)


