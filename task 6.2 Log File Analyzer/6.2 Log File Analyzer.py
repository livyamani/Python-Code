import re
from collections import Counter
from datetime import datetime


def parse_log_file(file_path):
    log_entries = []
    
    # Regex pattern for log entries
    log_pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (\d{3}\.\d{3}\.\d{1,3}\.\d{1,3}) (.+)')
    
    
    with open(file_path, 'r', encoding='utf-8') as file:  
        for line in file:
            match = log_pattern.match(line)
            if match:
                timestamp_str, severity, ip, message = match.groups()
                timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
                log_entries.append({
                    'timestamp': timestamp,
                    'severity': severity,
                    'ip': ip,
                    'message': message
                })
    
    return log_entries


def summarize_logs(log_entries):
    error_count = sum(1 for entry in log_entries if entry['severity'] == 'ERROR')
    ip_counter = Counter(entry['ip'] for entry in log_entries)

    print(f"Total entries processed: {len(log_entries)}")
    print(f"Total errors: {error_count}")
    print("Most frequent IP addresses:")
    for ip, count in ip_counter.most_common(5):
        print(f"{ip}: {count}")

def filter_logs(log_entries, filters):
    filtered_logs = log_entries
    
    
    if filters:
        if 'start_date' in filters:
            filtered_logs = [log for log in filtered_logs if log['timestamp'] >= filters['start_date']]
        if 'end_date' in filters:
            filtered_logs = [log for log in filtered_logs if log['timestamp'] <= filters['end_date']]
        if 'severity' in filters:
            filtered_logs = [log for log in filtered_logs if log['severity'] == filters['severity']]
    
    return filtered_logs


def analyze_log_file(file_path):
    log_entries = parse_log_file(file_path)
    
    summarize_logs(log_entries)

    filters = {
        'start_date': datetime(2024, 10, 1, 12, 0, 0),  
        'end_date': datetime(2024, 10, 1, 14, 0, 0)   
    }
    filtered_logs = filter_logs(log_entries, filters)

    print("\nFiltered Logs (Errors between 12:00 and 14:00):")
    for log in filtered_logs:
        print(f"{log['timestamp']} - {log['severity']} - {log['ip']} - {log['message']}")

if __name__ == "__main__":
    
    log_file_path = r'C:\Users\Admin\Desktop\3A\task\task 6.2 Log File Analyzer\sample_log.log'  # Change this to your log file path
    analyze_log_file(log_file_path)
