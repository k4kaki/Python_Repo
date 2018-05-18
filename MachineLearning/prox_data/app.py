from flask import Flask, render_template, request
from werkzeug import secure_filename
import xlrd
import pymongo
import simplejson as json
app = Flask(__name__)

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      wb = xlrd.open_workbook("f.filename")
      sh = wb.sheet_by_index(0)
      order_list = []
      keys = [sh.cell(0, col_index).value for col_index in range(sh.ncols)]     
      for rownum in range(1, sh.nrows):
          orders = OrderedDict()
          row_values = sh.row_values(rownum)
          orders["ID"] = sh.cell(rownum,0).value
          
          order_list.append(orders)
if __name__ == '__main__':
   app.run(debug = True)
