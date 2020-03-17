from methods import *
import secret


# create an object from class Time()
t = Time()
browser = Browser()
email = Email()
computer = Computer()

#  set the hours and minutes for start and stop scrip
hour_start_time, minute_start_time = 7, 42
hour_end_time, minute_end_time = 8, 45
pointer_interval, wait_time_between_interval, wait_time_between_space = 2, 600, 1  # this interval should be lower than the end time

# Condition for starting script
# This for not starting the script outside the start and end time
while hour_start_time < t.time_now_hour() > hour_end_time:
    t.time_wait(10)
    print(f'start time is at {hour_start_time}:{minute_start_time} and end time is at {hour_end_time}:{minute_end_time}')
# this is for running at the desired hour
while t.time_now_hour() <= hour_start_time and t.time_now_minute() < minute_start_time:
    t.time_wait(10)
# Start time
actual_time_start = t.time_now()
start = t.start_time()
# Send email start_scrip
email.start_email(secret.emailFrom, secret.emailTo, secret.password, actual_time_start)
# # Open Browser
browser.open_browser(secret.url, 10)
# moving pointer and pause unpause so youtube doesnt stop
computer.move_pointer(pointer_interval, wait_time_between_interval, wait_time_between_space)

# Condition for closing script
while t.time_now_hour() <= hour_end_time and t.time_now_minute() < minute_end_time:
    t.time_wait(10)
# Close Browse
browser.close_browser(5)
# End Time
actual_time_end = t.time_now()
end = t.format_time(t.start_time() - start)
# Send email stop_script
email.stop_email(secret.emailFrom, secret.emailTo, secret.password, actual_time_start, end, actual_time_end)
# Shut down the computer
computer.shut_down(5)
