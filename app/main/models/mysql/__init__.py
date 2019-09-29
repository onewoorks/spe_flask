from .. import mysql_execute_query
from .emas_buruk import EmasBurukModel
from .tempahan import TempahanModel
from .jualan import JualanModel
from .stock import StockModel
from .no_bil import NoBilModel
from .bayar_kad import BayarKadModel

def mysql_execute_bulk_query(query):
    # mysql_execute_query(query)
    print(query)