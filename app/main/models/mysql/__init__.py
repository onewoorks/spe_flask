from .. import mysql_execute_query, mysql_insert_query, mysql_insert_bulk_query
from .emas_buruk import EmasBurukModel
from .tempahan import TempahanModel
from .jualan import JualanModel
from .stock import StockModel
from .no_bil import NoBilModel
from .bayar_kad import BayarKadModel


def multiple_insert_query(query):
    mysql_insert_bulk_query(query)