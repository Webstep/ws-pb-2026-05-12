from utils.make_sorted_cost_of_calls_by_caller import (
    make_sorted_cost_of_calls_by_caller,
)


def print_international_call_costs(callRecords):
    sortedCallCostByCaller = make_sorted_cost_of_calls_by_caller(callRecords)

    if len(sortedCallCostByCaller) < 3:
        print("Not enough callers to show top 3.")
    else:
        print("Top 3 Callers by Cost:")
        for caller, callData in sortedCallCostByCaller[0:3]:
            print("%s: %d øre" % (caller, callData))
