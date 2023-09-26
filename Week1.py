from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename
import cv2
import os

app = Flask(__name__)

@app.route('/upload')
def upload_page():
   return render_template('index.html')

@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))

       # Đọc ảnh
      img = cv2.imread(f.filename, cv2.IMREAD_GRAYSCALE)

      # Lưu ảnh grayscale với tên mới
      grayscale_filename = "grayscale_" + f.filename
      cv2.imwrite(grayscale_filename, img)
      os.environ['GRAYSCALE_IMAGE_PATH'] = grayscale_filename

      return 'Ảnh đã được tải lên và chuyển thành grayscale thành công!'

if __name__ == '__main__':
   app.run(debug=True)

