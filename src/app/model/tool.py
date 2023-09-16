import json
from dateutil import parser
from typing import Union, List, Dict
from datetime import datetime, timedelta, timezone
from asyncpg import Record
from asyncpg.exceptions import UniqueViolationError
from ..schema import exchange_rate as schema
from ..schema.base import ApiException
from .config import get_settings

class ToolModel():
    @staticmethod
    async def change_exchanger_rate(change_info: schema.change_info) -> schema.changed_data:
        settings = get_settings()
        currenies_source_keys = settings.exchange_rate_table['currencies'].keys()
        amount = 0
        
        # 檢查使用者輸入
        try:
            if change_info.source not in currenies_source_keys:
                raise Exception('source 值格式錯誤')
            elif  change_info.target not in settings.exchange_rate_table['currencies'][change_info.source].keys():
                raise Exception('target 值格式錯誤')
            elif change_info.amount.__contains__('$') is False:
                raise Exception('amountet 值格式錯誤')
            amount = float(change_info.amount[1:].replace(',', ''))
        except Exception as e:
            raise ApiException(code=404,
                                msg="匯率轉換發生非預期錯誤",
                                detail={
                                    "payload": change_info,
                                    "description": str(e)
                                })
        # 匯率運算
        try:
            change_rate = float(settings.exchange_rate_table['currencies'][change_info.source][change_info.target])
            amount *= change_rate
            amount *= 1000

            if amount % 10 > 4:
                amount += 10
            amount /= 10
            float_point = '{:02d}'.format(int(amount % 100))
            amount /= 100

            amount = str(int(amount))[::-1]

            amount_part = [amount[i:i+3] for i in range(0, len(amount), 3)]
            amount = ",".join(amount_part)[::-1]
            amount = f'${amount}.{float_point}'
            return schema.changed_data(amount=amount)
        except Exception as e:
            raise ApiException(code=500,
                                msg="匯率轉換發生非預期錯誤",
                                detail={
                                    "payload": change_info,
                                    "description": str(e)
                                })


tool = ToolModel()
