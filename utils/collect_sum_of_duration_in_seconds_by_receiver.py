from models.CallRecord import CallRecord


def collect_sum_of_duration_in_seconds_by_receiver(
    callRecords: list[CallRecord],
) -> dict[str, int]:
    callDataByReceiver = {}
    for callRecord in callRecords:
        receiver = callRecord.get("Receiver")
        durationInSeconds = callRecord.get("DurationInSeconds")

        callDataForReceiver = callDataByReceiver.get(receiver)

        if callDataForReceiver is None:
            callDataByReceiver[receiver] = durationInSeconds
            continue

        callDataByReceiver[receiver] += durationInSeconds

    return callDataByReceiver
