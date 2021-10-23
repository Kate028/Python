import qrcode   #import decleration for the qrcode generator
from PIL import Image
#img=qrcode.make("https://en.wikipedia.org/wiki/Elon_Musk") # u can paste link here
#img.save('wiki_Elon.jpg')     this is simple in two line code for qr generator
qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data("https://en.wikipedia.org/wiki/Elon_Musk")#add_data is function we can pass any links to it
qr.make(fit=True)

img=qr.make_image(fill_color="black",back_color="white").convert('RGB')# this helps in making qr code with white backgroun and black fill
img.save("sample.png")
