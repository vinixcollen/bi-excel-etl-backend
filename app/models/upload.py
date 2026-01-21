from tortoise import fields
from tortoise.models import Model
import uuid
from app.enums.upload_status import UploadStatus

class Upload(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    file_name = fields.CharField(max_length=100)
    size = fields.FloatField()
    uploaded_at = fields.DatetimeField(auto_now_add=True)
    status = fields.CharEnumField(
        UploadStatus,
        default=UploadStatus.PROCESSING
    )
    file_url = fields.CharField(max_length=250)

    class Meta:
        table = "Upload"