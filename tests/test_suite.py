import pytest
import json
import tempfile
import os
from models.CallRecord import CallRecord
from utils.read_call_records_from_file import read_call_records_from_file
from utils.make_sorted_number_of_calls_by_caller import (
    make_sorted_number_of_calls_by_caller,
    collect_number_of_calls_by_caller,
)
from utils.collect_sum_of_duration_in_seconds_by_receiver import (
    collect_sum_of_duration_in_seconds_by_receiver,
)
from utils.find_number_of_phone_unique_numbers import (
    find_number_of_phone_unique_numbers,
)


@pytest.fixture
def sample_call_records():
    return [
        CallRecord(
            Caller="12345678",
            Receiver="09876543",
            StartTimeAsUtc="2024-11-27T10:00:00Z",
            DurationInSeconds=120,
        ),
        CallRecord(
            Caller="12345678",
            Receiver="11223344",
            StartTimeAsUtc="2024-11-27T10:05:00Z",
            DurationInSeconds=60,
        ),
        CallRecord(
            Caller="09876543",
            Receiver="12345678",
            StartTimeAsUtc="2024-11-27T10:10:00Z",
            DurationInSeconds=180,
        ),
        CallRecord(
            Caller="11223344",
            Receiver="12345678",
            StartTimeAsUtc="2024-11-27T10:20:00Z",
            DurationInSeconds=30,
        ),
        CallRecord(
            Caller="12345678",
            Receiver="44556677",
            StartTimeAsUtc="2024-11-27T10:30:00Z",
            DurationInSeconds=90,
        ),
    ]


@pytest.fixture
def temp_json_file(sample_call_records):
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json_data = [
            {
                "Caller": record["Caller"],
                "Receiver": record["Receiver"],
                "StartTime": record["StartTimeAsUtc"],
                "Duration": record["DurationInSeconds"],
            }
            for record in sample_call_records
        ]
        json.dump(json_data, f)
        temp_path = f.name

    yield temp_path

    if os.path.exists(temp_path):
        os.unlink(temp_path)


class TestReadCallRecordsFromFile:
    def test_read_valid_file(self, temp_json_file):
        records = read_call_records_from_file(temp_json_file)

        assert len(records) == 5
        assert records[0]["Caller"] == "12345678"
        assert records[0]["DurationInSeconds"] == 120

    def test_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            read_call_records_from_file("/nonexistent/path.json")

    def test_invalid_json(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            f.write("{ invalid json")
            temp_path = f.name

        try:
            with pytest.raises(ValueError, match="Invalid file format"):
                read_call_records_from_file(temp_path)
        finally:
            os.unlink(temp_path)

    def test_missing_required_field(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump([{"Caller": "12345678"}], f)
            temp_path = f.name

        try:
            with pytest.raises(ValueError, match="Invalid file format"):
                read_call_records_from_file(temp_path)
        finally:
            os.unlink(temp_path)


class TestMakeSortedNumberOfCallsByCaller:
    def test_sorted_calls_by_caller(self, sample_call_records):
        result = make_sorted_number_of_calls_by_caller(sample_call_records)

        assert len(result) == 3
        assert result[0] == ("12345678", 3)
        assert result[1][0] in ("09876543", "11223344")
        assert result[2][0] in ("09876543", "11223344")
        assert result[1][1] == 1
        assert result[2][1] == 1

    def test_collect_number_of_calls_by_caller(self, sample_call_records):
        result = collect_number_of_calls_by_caller(sample_call_records)

        assert result["12345678"] == 3
        assert result["09876543"] == 1
        assert result["11223344"] == 1

    def test_empty_records(self):
        emptyRecords = []

        result = make_sorted_number_of_calls_by_caller(emptyRecords)

        assert result == []


class TestCollectSumOfDurationByReceiver:
    def test_sum_duration_by_receiver(self, sample_call_records):
        result = collect_sum_of_duration_in_seconds_by_receiver(sample_call_records)

        assert result["12345678"] == 210
        assert result["09876543"] == 120
        assert result["11223344"] == 60
        assert result["44556677"] == 90

    def test_empty_records(self):
        emptyRecords = []

        result = collect_sum_of_duration_in_seconds_by_receiver(emptyRecords)

        assert result == {}


class TestFindNumberOfUniquePhoneNumbers:
    def test_unique_numbers(self, sample_call_records):
        result = find_number_of_phone_unique_numbers(sample_call_records)

        assert result == 4

    def test_single_record(self):
        records = [
            CallRecord(
                Caller="12345678",
                Receiver="09876543",
                StartTimeAsUtc="2024-11-27T10:00:00Z",
                DurationInSeconds=120,
            )
        ]

        result = find_number_of_phone_unique_numbers(records)

        assert result == 2

    def test_same_caller_receiver(self):
        records = [
            CallRecord(
                Caller="12345678",
                Receiver="12345678",
                StartTimeAsUtc="2024-11-27T10:00:00Z",
                DurationInSeconds=60,
            )
        ]

        result = find_number_of_phone_unique_numbers(records)

        assert result == 1

    def test_empty_records(self):
        emptyRecords = []

        result = find_number_of_phone_unique_numbers(emptyRecords)

        assert result == 0
