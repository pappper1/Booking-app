import asyncio
from datetime import date

from fastapi import APIRouter
from fastapi_cache.decorator import cache

from app.hotels.dao import HotelDAO
from app.hotels.rooms.dao import RoomDAO
from app.hotels.rooms.schemas import SRooms
from app.hotels.schemas import SHotels

router = APIRouter(
	prefix="/hotels",
	tags=["Hotels"]
)

@router.get("/")
async def get_hotels() -> list[SHotels]:
	return await HotelDAO.find_all()


@router.get("/{location}")
async def get_hotels_by_location(location: str) -> list[SHotels]:
	return await HotelDAO.find_all(location=location)


@router.get("/{hotel_id}/rooms")
async def get_hotel_rooms(hotel_id: int) -> list[SRooms]:
	return await RoomDAO.find_all(hotel_id=hotel_id)


@router.get("/id/{hotel_id}")
async def get_hotel(hotel_id: int) -> SHotels:
	return await HotelDAO.find_one_or_none(id=hotel_id)