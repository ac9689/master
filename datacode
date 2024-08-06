import time

def digital_clock():
    while True:
        # Get the current time in hours, minutes, and seconds
        current_time = time.localtime()
        hour = current_time.tm_hour
        minute = current_time.tm_min
        second = current_time.tm_sec
        
        # Formatting the time to display properly
        clock_time = f"{hour:02}:{minute:02}:{second:02}"
        
        # Print the current time
        print(clock_time, end="\r")
        
        # Wait for one second
        time.sleep(1)

if __name__ == "__main__":
    try:
        digital_clock()
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user")
