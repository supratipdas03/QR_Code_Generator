import pyqrcode
import png
link = "https://supratipdas-portfolio.netlify.app/"
qr_code = pyqrcode.create(link)
qr_code.png("website.png", scale=5)