import re
from collections import Counter

def analyze_log(file_path):
    suspicious_events = []
    failed_login_attempts = []

    with open(file_path, "r") as log:
        for line in log:
            if re.search(r"failed|error|unauthorized", line, re.IGNORECASE):
                suspicious_events.append(line.strip())

            if "Failed password" in line:
                ip_match = re.search(r"\d+\.\d+\.\d+\.\d+", line)
                if ip_match:
                    failed_login_attempts.append(ip_match.group())

    ip_counter = Counter(failed_login_attempts)

    print("\n--- Suspicious Events ---")
    for event in suspicious_events:
        print(event)

    print("\n--- Failed Login Attempts by IP ---")
    for ip, count in ip_counter.items():
        print(f"{ip}: {count} attempts")

if __name__ == "__main__":
    analyze_log("sample.log")
