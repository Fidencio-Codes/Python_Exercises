## Convert text or link into QR Code

## Steps
# Install needed libraries (pip install qrcode Image)
# Create function that collects a text and converts to QR code -- qrcode.QRCode()
# Save the qr code as an image 
# Run the function 


import qrcode

def generate_qrcode(text):

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    img.save("qrcodeimg.png")

# ask user for their URL
url = input("Enter URL: ")
generate_qrcode(url)

# Or generate QR code from a provided link 
# generate_qrcode("https://github.com/Fidencio-Codes")
# generate_qrcode("https://www.google.com")