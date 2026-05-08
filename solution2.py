from constants.FILE_PATH import FILE_PATH
from utils.print_international_call_costs import print_international_call_costs
from utils.read_call_records_from_file import read_call_records_from_file

if __name__ == "__main__":
    callRecords = read_call_records_from_file(FILE_PATH)

    print_international_call_costs(callRecords)
