import qrcode
data='Good morning world!'
QR=qrcode.QRCode(version=1,box_size=15,border=4)
QR.add_data(data)
QR.make(fit=True)
image=QR.make_image(fill_colour='White', back_color='Black') 
image.save('C:/Users/shash/Desktop/Extras/myqrcode1.png')
