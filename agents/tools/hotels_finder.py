import os
from typing import Optional

from dotenv import load_dotenv
from serpapi import GoogleSearch
from langchain.pydantic_v1 import BaseModel, Field
from langchain_core.tools import tool

load_dotenv()


class HotelsInput(BaseModel):
    q: str = Field(description="Location of the hotel")
    check_in_date: str = Field(
        description="Check-in date. Format: YYYY-MM-DD"
    )
    check_out_date: str = Field(
        description="Check-out date. Format: YYYY-MM-DD"
    )
    sort_by: Optional[int] = Field(
        8,
        description="Sort results. Default is highest rating."
    )
    adults: Optional[int] = Field(
        1,
        description="Number of adults. Default is 1."
    )
    children: Optional[int] = Field(
        0,
        description="Number of children. Default is 0."
    )
    rooms: Optional[int] = Field(
        1,
        description="Number of rooms. Default is 1."
    )
    hotel_class: Optional[str] = Field(
        None,
        description="Hotel class, for example 2,3,4"
    )


class HotelsInputSchema(BaseModel):
    params: HotelsInput


@tool(args_schema=HotelsInputSchema)
def hotels_finder(params: HotelsInput):
    """
    Find hotels using the Google Hotels engine through SerpAPI.
    """

    search_params = {
        "api_key": os.environ.get("SERPAPI_API_KEY"),
        "engine": "google_hotels",
        "hl": "en",
        "gl": "us",

        "q": params.q,

        "check_in_date": params.check_in_date,
        "check_out_date": params.check_out_date,

        "currency": "USD",

        "adults": params.adults,
        "children": params.children,
        "rooms": params.rooms,

        "sort_by": params.sort_by,
        "hotel_class": params.hotel_class
    }

    try:
        search = GoogleSearch(search_params)

        # Get results as dictionary
        results = search.get_dict()

        # Get hotel properties safely
        hotels = results.get("properties", [])

        return hotels[:5]

    except Exception as e:
        return f"Hotel search error: {str(e)}"