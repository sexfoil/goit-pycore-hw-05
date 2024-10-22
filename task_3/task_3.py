from pathlib import Path
from collections import defaultdict
import argparse, re

log_levels = ["INFO", "ERROR", "DEBUG", "WARNING"]
date_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")
time_pattern = re.compile(r"^\d{2}:\d{2}:\d{2}$")
level_pattern = re.compile(f"^({'|'.join(log_levels)})$")


validate_format = lambda value, pattern: pattern.match(value)


def get_valid_data(match_result: re.Match):
    if match_result:
        return match_result.string
    raise ValueError


def parse_log_line(line: str):    
    parts = line.split()
    
    if len(parts) < 4:
        raise ValueError
    
    date = get_valid_data(validate_format(parts.pop(0), date_pattern)) 
    time = get_valid_data(validate_format(parts.pop(0), time_pattern)) 
    level = get_valid_data(validate_format(parts.pop(0), level_pattern)) 
    message = " ".join(parts)
    
    return {"date": date, "time": time, "level": level, "message": message}


def load_logs(file_path: str):
    with open(file_path, "r", encoding="utf-8") as file:
        lines: list = file.readlines()
        logs = [parse_log_line(line) for line in lines]
        return logs


def filter_logs_by_level(logs: list, level: str):
    if level and level in log_levels:
        return list(filter(lambda log: level == log["level"], logs))
    
    return [] 


def count_logs_by_level(logs: list):
    result = defaultdict(int)
    for log in logs:
        result[log["level"]] += 1
    
    return dict(result)


def display_log_counts(counts: dict):
    col_name_1 = "Logging level "
    len_1 = len(col_name_1)
    col_name_2 = " Quantity"
    len_2 = len(col_name_2)
    print(f"{col_name_1}|{col_name_2}")
    dash_row = "-" * len_1 + "|" + "-" * len_2
    print(dash_row)
    for k, v in counts.items():
        print(f"{k:<{len_1}}| {v:<{len_2}}")


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--Path", required=True)
parser.add_argument("-l", "--LogLevel", required=False)
args = parser.parse_args()

try:
    logs_file_path = Path(args.Path)
    log_level: str = args.LogLevel.upper()

    logs: list = load_logs(logs_file_path)

    filtered_logs = filter_logs_by_level(logs, log_level)

    result = count_logs_by_level(logs)
    display_log_counts(result)
    
    if filtered_logs:
        print(f"\nDetails for logging level '{log_level}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")


except FileNotFoundError:
    print("Incorrect path to file or file does not exist")
except UnicodeDecodeError:
    print("Incorrect file format")
except ValueError:
    print("Incorrect logs data format")
