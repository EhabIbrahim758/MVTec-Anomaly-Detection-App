from fastapi.datastructures import UploadFile
from fastapi.params import File
from pydantic import BaseModel

class Image_path(BaseModel) :
    img_path : str
    img_type : str


