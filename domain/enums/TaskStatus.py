from enum import Enum

class TaskStatus(str, Enum):
    PUBLISHED = "published"
    DRAFT = "draft"