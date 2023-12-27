from pydantic import BaseModel
from fastapi import Query


class HistoricalDataRequest(BaseModel):
    symbol: str
    start_date: str = Query(None)
    end_date: str = Query(None)

class CorporateActionRequest(BaseModel):
    from_date: str
    to_date: str

class StockQuoteResponse(BaseModel):
    symbol: str
    open: float
    high: float
    low: float
    close: float
    change: float
    percent_change: float

class HistoricalDataResponse(BaseModel):
    dates: list[str]
    open: list[float]
    high: list[float]
    low: list[float]
    close: list[float]


class IndexQuoteResponse(BaseModel):
    index_name: str
    open: float
    high: float 
    low: float
    close: float
    change: float
    percent_change: float


class CorporateActionRequest(BaseModel):
    from_date: str
    to_date: str


class CorporateAction(BaseModel):
    company: str
    date: str
    type: str
    record_date: str
    ex_date: str
    ratio: float
    amount: float
    description: str

class DownloadResponse(BaseModel):
    content: bytes
    filename: str

class IndexHistoryResponse(BaseModel):
    dates: list[str]
    data: list[float]