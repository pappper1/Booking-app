from datetime import date

from fastapi import APIRouter, Depends, Request
from fastapi_versioning import version
from pydantic import parse_obj_as

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking
from app.exceptions import RoomCannotBeBooked
from app.tasks.tasks import send_booking_confirmation_email
from app.users.dependecies import get_current_user
from app.users.models import Users

router = APIRouter(
	prefix="/bookings",
	tags=["Bookings"],
)

@router.get("")
@version(1)
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBooking]:
	return await BookingDAO.find_all(user_id=user.id)


@router.post("")
@version(1)
async def add_booking(room_id: int, date_from: date, date_to: date, user: Users = Depends(get_current_user)):
	booking = await BookingDAO.add(user_id=user.id, room_id=room_id, date_from=date_from, date_to=date_to)
	booking_dict = parse_obj_as(SBooking, booking.__dict__).dict()
	send_booking_confirmation_email.delay(booking_dict, user.email)
	if not booking:
		raise RoomCannotBeBooked


@router.delete("/{booking_id}")
@version(1)
async def delete_booking(booking_id: int, user: Users = Depends(get_current_user)):
	return await BookingDAO.delete(id=booking_id, user_id=user.id)