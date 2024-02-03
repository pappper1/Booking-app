from fastapi import HTTPException, status


class BookingException(HTTPException):
	status_code = 500
	detail = ""

	def __init__(self):
		super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(BookingException):

	status_code=status.HTTP_409_CONFLICT
	detail="User already exists"


class IncorrectEmailOrPasswordException(BookingException):

	status_code=status.HTTP_401_UNAUTHORIZED
	detail="Incorrect email or password"


class ExpiredTokenException(BookingException):

	status_code=status.HTTP_401_UNAUTHORIZED
	detail="Expired token"


class TokenAbsentException(BookingException):

	status_code=status.HTTP_401_UNAUTHORIZED
	detail="Token is absent"


class IncorrectTokenFormatException(BookingException):

	status_code=status.HTTP_401_UNAUTHORIZED
	detail="Incorrect token format"


class UserIsNotPresentException(BookingException):

	status_code=status.HTTP_401_UNAUTHORIZED


class RoomCannotBeBooked(BookingException):
	status_code=status.HTTP_409_CONFLICT,
	detail="No free rooms available"
