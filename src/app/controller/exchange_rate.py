from typing import Union, List, Dict
from ..schema import exchange_rate as schema
from ..model.tool import tool

class ExchangeRateController:
    @staticmethod
    async def change_exchanger_rate(change_info: schema.change_info) -> Union[schema.changed_data, None]:
        return await tool.change_exchanger_rate(change_info)


controller = ExchangeRateController()
