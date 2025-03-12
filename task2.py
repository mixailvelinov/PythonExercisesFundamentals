import time

# We can convert the list to a set for faster checks
devices_list = [f"Device_{i}" for i in range(1, 301)]
devices_set = set(devices_list)

device = input("Enter a device name: ")

# Start the timer
start_time = time.perf_counter()

# Check if the device is in the set
if device in devices_set:
    print(f"{device} is in the list.")
else:
    print(f"{device} is not in the list.")

# End the timer
end_time = time.perf_counter()

# Print result
print(f"Time taken: {end_time - start_time:.10f} seconds.")
