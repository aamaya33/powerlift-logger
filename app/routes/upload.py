from fastapi import APIRouter, File, UploadFile, HTTPException

router = APIRouter()

@router.post("/uploadfile/")
async def create_file(file: UploadFile = File(...)):
    if not file: 
        return HTTPException(status_code=400, detail="No file uploaded")
    # FIXME: For now we'll be saving the file locally, but we shoudl change this to save it in a cloud storage
    return {
            "filename": file
    }
    
