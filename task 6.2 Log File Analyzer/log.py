log_content = """2024-10-01 12:00:00 INFO 192.168.1.1 User logged in
2024-10-01 12:05:00 ERROR 192.168.1.1 Failed to load resource
2024-10-01 12:10:00 WARNING 192.168.1.2 Disk space low
2024-10-01 12:15:00 INFO 192.168.1.3 User logged out
"""

log_file_path = r'C:\Users\Admin\Desktop\3A\task\task 6.2\sample_log.log'

with open(log_file_path, 'w') as file:
    file.write(log_content)

print(f"Log file created at: {log_file_path}")