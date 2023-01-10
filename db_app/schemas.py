import re
from typing import Optional
from fastapi import Form
from pydantic import BaseModel, validator, PastDate


class StatisticsBase(BaseModel):
    date: Optional[PastDate]
    views: Optional[int]
    clicks: Optional[int]
    cost: Optional[float]

    @validator('date')
    def date_format(cls, v):
        if format(v) == '%Y/%m/%d':
            raise ValueError('must match the format %Y/%m/%d')
        return v

    @validator('views')
    def views_type(cls, v):
        if not isinstance(v, int):
            raise ValueError('must match an integer')
        return v

    @validator('clicks')
    def clicks_type(cls, v):
        if not isinstance(v, int):
            raise ValueError('must match an integer')
        return v

    @validator('cost')
    def cost_type(cls, v):
        if len(str(v).split('.')[1]) > 2:
            raise ValueError('must have 2 decimal places')
        return v


class ShowStatistics(BaseModel):
    date_from: Optional[str]
    date_to: Optional[str]

    @validator('date_from', 'date_to', check_fields=False)
    def date_format(cls, v):
        if re.fullmatch(r'^\d{4}\-\d\d\-\d\d$', v):
            return v
        raise ValueError('must match the format date')
        