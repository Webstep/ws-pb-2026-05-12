from utils.make_sorted_number_of_calls_by_caller import (
    make_sorted_number_of_calls_by_caller,
)
from utils.collect_sum_of_duration_in_seconds_by_receiver import (
    collect_sum_of_duration_in_seconds_by_receiver,
)
from utils.find_number_of_phone_unique_numbers import (
    find_number_of_phone_unique_numbers,
)


def print_call_statistics(callRecords):
    callDataByCallerSortedByNumberOfCalls = make_sorted_number_of_calls_by_caller(
        callRecords
    )

    if len(callDataByCallerSortedByNumberOfCalls) < 3:
        print("Not enough callers to show top 3.")
    else:
        print("Top 3 Most Active Callers:")
        for caller, callData in callDataByCallerSortedByNumberOfCalls[0:3]:
            print("%s: %d calls" % (caller, callData))

    sumOfDurationInSecondsByReceiver = collect_sum_of_duration_in_seconds_by_receiver(
        callRecords
    )

    if len(callDataByCallerSortedByNumberOfCalls) == 0:
        print("No callers found.")
    else:
        topCaller = callDataByCallerSortedByNumberOfCalls[0][0]

        sumOfDurationInSecondsToTopCaller = sumOfDurationInSecondsByReceiver.get(
            topCaller, 0
        )

        print(
            "Total Duration of Calls to %s: %d seconds"
            % (topCaller, sumOfDurationInSecondsToTopCaller)
        )

    numberOfUniquePhoneNumbers = find_number_of_phone_unique_numbers(callRecords)
    print("Total Unique Phone Numbers: %d" % numberOfUniquePhoneNumbers)
