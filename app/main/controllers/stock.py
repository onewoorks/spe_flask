from flask_restplus import Namespace, Resource, fields
from flask import request
import json

from ..services.stock.stock import StockService

api = Namespace('Stock',description="Stock")

@api.route('/item/<tag_no>')
class EPContractList(Resource):
    @api.doc('Stock')
    def get(self, tag_no):
        stock = StockService()
        return stock.read_stock(tag_no)

@api.route('/item/update-online')
class UpdateStok(Resource):
    def post(self):
        input_data = json.loads(request.data)
        stock = StockService()
        stock.update_stock_data(input_data)

