from typing import Union, List, Dict
from fastapi import APIRouter
from pydantic import schema
from ...controller.exchange_rate import controller as exchange_rate
from ...schema import exchange_rate as schema

router = APIRouter(prefix="/current-exchanger-rate",
                   tags=["current-exchanger-rate"],
                   responses={404: {
                       "description": "此頁面不存在喔, 嘻嘻"
                   }})


@router.get("/change", response_model=Union[schema.changed_data, None])
async def change_exchanger_rate(source: str, target:str, amount:str) -> Union[schema.changed_data, None]:
    print(schema.change_info(
            source=source,target=target,amount=amount
        ))
    return await exchange_rate.change_exchanger_rate(
        change_info = schema.change_info(
            source=source,target=target,amount=amount
        )
    )
