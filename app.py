from flask import Flask, render_template,request
import qrcode


app=Flask(__name__)

@app.route('/', methods=['GET','POST'])
def hello_world():
    if request.method=='POST':
        link= request.form['title']
        qr(link)
    return render_template('index.html')


def qr(link):
    data = link

    # Create a QR Code object
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # controls the error correction used for the QR Code
        box_size=10,  # controls how many pixels each “box” of the QR code is
        border=4,  # controls how many boxes thick the border should be
    )

    # Add data to the QR Code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    img.save("static/qrcode.png")

if __name__=="__main__":
    app.run(debug=False)