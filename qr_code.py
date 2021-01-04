import qrcode

user_input = input('Enter text: ')
qr_code = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr_code.add_data(user_input)
qr_code.make(fit=True)
img = qr_code.make_image(fill_color='black', back_color='white')
img.show()