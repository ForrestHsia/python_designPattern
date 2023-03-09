import qrcode

qrCodeContent = "https://e751-60-249-180-200.jp.ngrok.io/login"

img = qrcode.make(qrCodeContent)

img.save("test.png")