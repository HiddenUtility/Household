from enum import Enum


class EposCardFileColumns(Enum):
    SHOP_NAME = "ご利用場所"
    DATE = "ご利用年月日"
    PAYMENT = "ご利用金額（キャッシングでは元金になります）"