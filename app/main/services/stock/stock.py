from ...models.mysql.stock import StockModel

import json

stock = StockModel()


class StockService():
    def read_stock(self, tag_no):
        response = stock.read_stock_by_tagn_o(tag_no)
        if response != False:
            for i in response:
                i['data_tambahan'] = json.loads(i['data_tambahan']) if i['data_tambahan'] is not None else None
        return response

    def update_stock_data(self, product_data):
        product = product_data["product"]
        product_online = product['product_online']
        data_attribute = {
            "prefix": "",
            "ukuran": {
                "size_lebar": product_online['lebar'],
                "size_cincin": product_online['size'],
                "size_panjang": product_online['panjang'],
                "size_diameter": product_online['diameter']
            },
            "category": product_online['kategori'],
            "kod_paten": "",
            "category_name": ""
        }
        StockModel().update_data_attribute_stock(product['product_info']['id'], product['product_info']['no_tag'], data_attribute)