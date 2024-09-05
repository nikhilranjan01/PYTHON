import qrcode

# Personal information
personal_info = """
Name: Nikhil Ranjan
Email: nikhilranjan@gmail.com
Phone: +91XXXXXXXXX
Address: Jodhpur
"""

# Generate QR code
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in pixels
    border=4,  # Thickness of the border (number of boxes)
)

# Add data to the QR code
qr.add_data(personal_info)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
img.save("personal_info_qr.png")

# If you want to display the image (optional)
img.show()
