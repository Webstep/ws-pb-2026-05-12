from models.CallRecord import CallRecord

OERE_PER_SECOND_FOR_INTERNATIONAL_CALLS = 3
OERE_PER_SECOND_FOR_DOMESTIC_CALLS = 1


def make_sorted_cost_of_calls_by_caller(
    callRecords: list[CallRecord],
) -> list[tuple[str, int]]:
    callDataByCaller = collect_cost_of_calls_by_caller(callRecords)

    callDataByCallerSortedByNumberOfCalls = sorted(
        callDataByCaller.items(),
        key=lambda item: item[1],
        reverse=True,
    )

    return callDataByCallerSortedByNumberOfCalls


def collect_cost_of_calls_by_caller(callRecords: list[CallRecord]) -> dict[str, int]:
    costByCaller: dict[str, int] = {}
    for callRecord in callRecords:
        caller = callRecord.get("Caller")

        costForCaller = costByCaller.get(caller)

        costOfCall = calculate_cost_of_call(callRecord)

        if costForCaller is None:
            costByCaller[caller] = costOfCall
            continue

        costByCaller[caller] += costOfCall

    return costByCaller


def calculate_cost_of_call(callRecord: CallRecord) -> int:
    durationInSeconds = callRecord.get("DurationInSeconds")

    if is_call_international(callRecord):
        return durationInSeconds * OERE_PER_SECOND_FOR_INTERNATIONAL_CALLS
    else:
        return durationInSeconds * OERE_PER_SECOND_FOR_DOMESTIC_CALLS


# Dummy implementation for demonstration purposes
# TODO: Replace with logic for actual phone numbers, probably using a library like 'phonenumbers' (Google's libphonenumber port for Python)
def is_call_international(callRecord: CallRecord) -> bool:
    caller = callRecord.get("Caller")
    receiver = callRecord.get("Receiver")

    return caller[0] != receiver[0]
