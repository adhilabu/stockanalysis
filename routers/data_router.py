from fastapi import FastAPI, Query, Request, APIRouter
from typing import List
import nsepy
from nsetools import Nse
from pydantic import BaseModel
from models.data_models import IndexQuoteResponse, StockQuoteResponse, HistoricalDataRequest, HistoricalDataResponse, IndexHistoryResponse, IndexQuoteResponse, DownloadResponse, CorporateAction, CorporateActionRequest, IndexHistoryResponse

data_app = APIRouter(
    prefix='/data',
    tags=['data']
)

# Index quotes and lists
@data_app.get("/indices", response_model=List[str])
async def get_index_list_data():
    nse_tool = Nse()
    return nse_tool.get_index_list()

@data_app.get("/indices/{index_name}/quote", response_model=IndexQuoteResponse)
async def get_index_quote(index_name: str):
    quote = get_index_quote(index_name)
    return IndexQuoteResponse(**quote)

# Stock quotes and history
@data_app.get("/quotes/{symbol}", response_model=StockQuoteResponse)
async def get_stock_quote(symbol: str):
    try:
        quote = get_quote(symbol)
        return StockQuoteResponse(**quote)
    except Exception as e:
        return {"error": str(e)}

@data_app.get("/history", response_model=HistoricalDataResponse)
async def get_historical_data(request: HistoricalDataRequest):
    try:
        data = get_history(
            request.symbol,
            start_date=request.start_date,
            end_date=request.end_date,
        )
        response = HistoricalDataResponse(
            dates=data.index,
            open=data["Open"],
            high=data["High"],
            low=data["Low"],
            close=data["Close"],
        )
        return response
    except Exception as e:
        return {"error": str(e)}

# Index historical data (P/E, P/B, Dividend, Return)
@data_app.get("/indices/{index_name}/pe_history", response_model=IndexHistoryResponse)
async def get_index_pe_history(index_name: str):
    try:
        data = get_index_pe_history(index_name)
        dates = data.index.strftime("%Y-%m-%d")
        response = IndexHistoryResponse(dates=dates, pe_ratios=data)
        return response
    except Exception as e:
        return {"error": str(e)}

# Similar implementations for P/B, dividend, and return history endpoints

# Bhavcopy download
@data_app.get("/bhavcopy/{date}", response_model=DownloadResponse)
async def get_bhavcopy(date: str):
    try:
        data = get_bhavcopy(date)
        # Process and format Bhavcopy data for download (e.g., CSV or file object)
        response = DownloadResponse(content=data, filename=f"bhavcopy_{date}.csv")
        return response
    except Exception as e:
        return {"error": str(e)}

# Corporate actions and announcements
@data_app.get("/corporate_actions", response_model=List[CorporateAction])
async def get_corporate_actions(request: CorporateActionRequest):
    try:
        actions = get_corporate_actions(request.from_date, request.to_date)
        response = [CorporateAction(**action) for action in actions]
        return response
    except Exception as e:
        return {"error": str(e)}

# Similar implementation for announcements endpoint

# Define request/response models and base models used across endpoints

# ... (omitted for brevity, adapt from previous examples)

