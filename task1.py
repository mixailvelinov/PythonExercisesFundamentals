from datetime import datetime

# Collect user prompts
start_time_1 = input("Start time for first event: ")
end_time_1 = input("End time for first event: ")
start_time_2 = input("Start time for second event: ")
end_time_2 = input("End time for second event: ")

# Using 24-hour format
time_format = "%H:%M"

# Convert the variables to datetime objects
event_1 = [datetime.strptime(start_time_1, time_format).time(), datetime.strptime(end_time_1, time_format).time()]
event_2 = [datetime.strptime(start_time_2, time_format).time(), datetime.strptime(end_time_2, time_format).time()]

# Check if the events overlap and print the corresponding result
if event_1[0] <= event_2[1] and event_2[0] <= event_1[1]:
    overlap_start = max(event_1[0], event_2[0]).strftime('%H:%M')
    overlap_end = min(event_1[1], event_2[1]).strftime('%H:%M')
    print(f"true\nThe two events overlap starting from {overlap_start} to {overlap_end}.")
else:
    print("false\nThe two events do not overlap.")
