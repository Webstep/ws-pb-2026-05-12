from models.CallRecord import CallRecord


def find_number_of_phone_unique_numbers(callRecords: list[CallRecord]) -> int:
    uniqueNumbers = set[str]()
    for callRecord in callRecords:
        uniqueNumbers.add(callRecord.get("Caller"))
        uniqueNumbers.add(callRecord.get("Receiver"))

    return len(uniqueNumbers)
