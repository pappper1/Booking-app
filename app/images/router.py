import shutil

from fastapi import APIRouter, UploadFile

from app.tasks.tasks import process_pic

router = APIRouter(
	prefix="/images",
	tags=["Images"]
)

@router.post("/hotels")
async def add_hotel_image(name: int, file: UploadFile):
	im_path = f"app/static/images/{name}.jpg"
	with open(im_path, "wb") as buffer:
		shutil.copyfileobj(file.file, buffer)
	process_pic.delay(im_path)
	return {"status": "ok"}