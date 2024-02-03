import pytest
from httpx import AsyncClient


@pytest.mark.parametrize("room_id, date_from, date_to, status_code", [
	*[(4, "2021-10-10", "2021-10-20", 200)]*30,
	(4, "2021-10-10", "2021-10-20", 409),

])
async def test_add_and_get_booking(room_id, date_from, date_to, status_code, auth_ac: AsyncClient):
	response = await auth_ac.post("/bookings", params={
		"room_id": room_id,
		"date_from": date_from,
		"date_to": date_to,
	})

	assert response.status_code == status_code
