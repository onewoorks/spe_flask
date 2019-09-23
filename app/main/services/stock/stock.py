from ...models.mysql.stock import StockModel

import json

stock = StockModel()

class StockService():
    def ReadStock(self, tag_no):
        response = stock.ReadStockByTagNo(tag_no)
        for i in response:
            i['data_tambahan'] = json.loads(i['data_tambahan'])
        return response