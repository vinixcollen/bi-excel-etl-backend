from app.models.upload import Upload

async def get_all_uploads_handler():
    uploads = await Upload.all()

    return {
        "data": uploads
    }

async def create_upload_handler():
    # Create a new record when a file is uploaded
    pass