from utils.print_call_statistics import print_call_statistics
from utils.read_call_records_from_file import read_call_records_from_file

FILE_PATH = "assets/crds.json"

if __name__ == "__main__":
    callRecords = read_call_records_from_file(FILE_PATH)

    print_call_statistics(callRecords)
