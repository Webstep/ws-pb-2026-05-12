from typing import TypedDict


class CallRecord(TypedDict):
    Caller: str
    Receiver: str
    StartTimeAsUtc: str
    DurationInSeconds: int
