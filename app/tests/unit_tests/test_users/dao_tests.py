from app.users.dao import UsersDAO


async def test_find_user_by_id():
	user = await UsersDAO.find_by_id(7987)

	assert user.email == "user@example.com"