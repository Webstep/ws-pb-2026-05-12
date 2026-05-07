from models.CallRecord import CallRecord


def make_sorted_number_of_calls_by_caller(
    callRecords: list[CallRecord],
) -> list[tuple[str, int]]:
    callDataByCaller = collect_number_of_calls_by_caller(callRecords)

    callDataByCallerSortedByNumberOfCalls = sorted(
        callDataByCaller.items(),
        key=lambda item: item[1],
        reverse=True,
    )

    return callDataByCallerSortedByNumberOfCalls


def collect_number_of_calls_by_caller(callRecords: list[CallRecord]) -> dict[str, int]:
    callDataByCaller = {}
    for callRecord in callRecords:
        caller = callRecord.get("Caller")

        callDataForCaller = callDataByCaller.get(caller)

        if callDataForCaller is None:
            callDataByCaller[caller] = 1
            continue

        callDataByCaller[caller] += 1

    return callDataByCaller
