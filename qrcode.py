import qrcode
data='Good morning world!'
QR=qrcode.QRCode(version=1,box_size=15,border=4)
QR.add_data(data)
QR.make(fit=True)
image=QR.make_image(fill_colour='White', back_color='Black') 
image.save('Directory_where_the_image_will_be_saved')
