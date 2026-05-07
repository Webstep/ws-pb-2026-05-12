from models.CallRecord import CallRecord

import json
import os


def read_call_records_from_file(file_path: str) -> list[CallRecord]:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    if not os.path.isfile(file_path):
        raise ValueError(f"Path is not a file: {file_path}")

    try:
        with open(file_path, "r") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("Root element must be an array")

        return [
            CallRecord(
                Caller=record["Caller"],
                Receiver=record["Receiver"],
                StartTimeAsUtc=record["StartTime"],
                DurationInSeconds=record["Duration"],
            )
            for record in data
        ]
    except (json.JSONDecodeError, KeyError, TypeError) as e:
        raise ValueError(f"Invalid file format: {e}")
