from app.dao.base import BaseDAO
from app.hotels.models import Rooms


class RoomDAO(BaseDAO):
	model = Rooms