from flask_restplus import Namespace, Resource, fields

from ..services.stock.stock import StockService

api = Namespace('Stock',description="Stock")

@api.route('/item/<tag_no>')
class EPContractList(Resource):
    @api.doc('Stock')
    def get(self, tag_no):
        stock = StockService()
        return stock.ReadStock(tag_no)

