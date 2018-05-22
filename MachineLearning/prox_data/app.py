from flask import Flask, render_template, request
from werkzeug import secure_filename
import xlrd
from xlrd import XLRDError
from collections import OrderedDict
import datetime
from pymongo import MongoClient
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
      try:
          wb = xlrd.open_workbook(f.filename)
          sh = wb.sheet_by_index(0)
          order_list = []
          keys = [sh.cell(0, col_index).value for col_index in range(sh.ncols)]     
          for rownum in range(1, sh.nrows):
              orders = OrderedDict()
              row_values = sh.row_values(rownum)
              orders["ID"] = sh.cell(rownum,0).value
              orders.update({keys[col_index]: [{"status":sh.cell(rownum, col_index).value,"status_date":datetime.datetime.utcnow().strftime('%Y-%m-%d')}] for col_index in range(1,sh.ncols)})
              order_list.append(orders)
          j = json.dumps(order_list)
          with open('sample.json','w') as f:
              f.write(j)
      except XLRDError as e:
          return "The format of the file is not LEGAL"
      client = MongoClient('34.219.47.108',27017)
      pxsdb=client.sample_DB
      current_json=json.loads(open('sample.json').read())
      order_id=pxsdb.existing_order_tbl.distinct("ID")
      for json_dict in current_json:
          if json_dict["ID"] in order_id:
              for key in json_dict:
                  if key != "ID":
                      if pxsdb.existing_order_tbl.find_one({"ID":json_dict['ID']})[key][-1]["status"] != json_dict[key][0]["status"]:
                          pxsdb.existing_order_tbl.update({'_id' :pxsdb.existing_order_tbl.find_one({"ID":json_dict['ID']})['_id']}, {'$addToSet' :{key  : {"status":json_dict[key][0]["status"],"status_date":"2020-01-01"}}})
          else:
              pxsdb.existing_order_tbl.insert(json_dict)
      return render_template('upload.html')


if __name__ == '__main__':
   app.run(debug = True)
