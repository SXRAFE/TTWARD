import enum
import datetime

class GradeType(enum.Enum):
    GRADE = 1
    PASS = 2
    ABSENCE = 3
    COMMENT = 4


class Grade:

    # Raw grade object may contain the following data:
    # type: int (GradeType)
    # value: str
    # subject: str

    def __init__(self, raw: dict):
        self.type = raw["type"]
        self.value = raw["value"]
        
        # TODO: get subject PRIMARY KEY from SQL
        self.subject
        self.addedTime = datetime.now()
    