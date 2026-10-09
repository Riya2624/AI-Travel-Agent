import os
from typing import Optional

from dotenv import load_dotenv
from serpapi import GoogleSearch
from langchain.pydantic_v1 import BaseModel, Field
from langchain_core.tools import tool

load_dotenv()


class FlightsInput(BaseModel):
    departure_airport: Optional[str] = Field(
        description="Departure airport code (IATA)"
    )
    arrival_airport: Optional[str] = Field(
        description="Arrival airport code (IATA)"
    )
    outbound_date: Optional[str] = Field(
        description="Outbound date in YYYY-MM-DD format"
    )
    return_date: Optional[str] = Field(
        description="Return date in YYYY-MM-DD format"
    )
    adults: Optional[int] = Field(
        1,
        description="Number of adults. Default is 1."
    )
    children: Optional[int] = Field(
        0,
        description="Number of children. Default is 0."
    )
    infants_in_seat: Optional[int] = Field(
        0,
        description="Number of infants in seat. Default is 0."
    )
    infants_on_lap: Optional[int] = Field(
        0,
        description="Number of infants on lap. Default is 0."
    )


class FlightsInputSchema(BaseModel):
    params: FlightsInput


@tool(args_schema=FlightsInputSchema)
def flights_finder(params: FlightsInput):
    """
    Find flights using the Google Flights engine through SerpAPI.
    """

    search_params = {
        "api_key": os.environ.get("SERPAPI_API_KEY"),
        "engine": "google_flights",
        "hl": "en",
        "gl": "us",
        "departure_id": params.departure_airport,
        "arrival_id": params.arrival_airport,
        "outbound_date": params.outbound_date,
        "return_date": params.return_date,
        "currency": "USD",
        "adults": params.adults,
        "infants_in_seat": params.infants_in_seat,
        "stops": "1",
        "infants_on_lap": params.infants_on_lap,
        "children": params.children
    }

    try:
        search = GoogleSearch(search_params)

        # Get SerpAPI response as dictionary
        results = search.get_dict()

        # Get best flights
        flights = results.get("best_flights", [])

        return flights[:3]

    except Exception as e:
        return f"Flight search error: {str(e)}"