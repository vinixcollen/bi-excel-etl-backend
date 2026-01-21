from enum import Enum

class UploadStatus(str, Enum):
    SUCCESS = 'SUCCESS'
    FAILED = 'FAILED'
    PROCESSING = 'PROCESSING'