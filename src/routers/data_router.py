import nsetools
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

# Initialize the NSE client (replace with your API key if required)
nse = nsetools()

data_router = APIRouter(
    prefix="/data", 
    tags=["data"]
)

@data_router.get("/stocks/daily")
async def get_daily_data():
    try:
        # Get daily data for all stocks
        all_stocks = nse.get_quote()
        q = nse.get_quote('infy')
        # Filter for valid stocks with percentage change data
        valid_stocks = [
            stock for stock in all_stocks if stock["pChange"] is not None
        ]

        # Sort stocks by percentage gain in descending order
        sorted_stocks = sorted(
            valid_stocks, key=lambda stock: float(stock["pChange"]), reverse=True
        )

        return JSONResponse(content={"stocks": sorted_stocks})

    except Exception as e:
        return JSONResponse(
            status_code=500, content={"error": str(e)}
        )