import webbrowser as wb
import datetime, threading, time
import os
import pyautogui
import smtplib  # module defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon


class Time:
    def start_time(self):
        # starts the count in seconds
        return time.time()

    def format_time(self, format_time):
        # measured time is displayed in hour:minute:seconds
        format_time = time.strftime("%H:%M:%S", time.gmtime(format_time))
        return format_time

    def time_now(self):
        # indicates the actual date and time
        return time.ctime()

    def time_now_hour(self):
        # indicates time in hours
        return datetime.datetime.now().hour

    def time_now_minute(self):
        # indicates time in minutes
        return datetime.datetime.now().minute

    def time_wait(self, waittime):
        # pause actions before running
        time_event = threading.Event()
        waittime = time_event.wait(waittime)
        return waittime

    def date_now(self):
        #  this method is used for running condition when choosing hour
        return datetime.datetime.now()


class Browser:
    def open_browser(self, url, loading_time):
        wb.open(url)
        time_event = threading.Event()
        time_event.wait(loading_time)
        pyautogui.click(569, 454, button='left')  # starts the youtube video by click

    def close_browser(self, wait_time):
        time_event = threading.Event()
        time_event.wait(wait_time)
        return os.system('taskkill /im chrome.exe /f')


class Email:
    def start_email(self, email_from, email_to, password, starttime):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # is a way to take an existing insecure connection and upgrade it to a secure connection using SSL/TLS
        server.login(email_from, password)
        subject = 'STARTING the computer'
        text = f'The script started {starttime} and is running for morning wake up videos'
        msg = f'Subject: {subject}\n\n{text}'
        server.sendmail(email_from, email_to, msg, subject)
        server.quit()

    def stop_email(self, email_from, email_to, password,starttime, runtime, closetime):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # is a way to take an existing insecure connection and upgrade it to a secure connection using SSL/TLS
        server.login(email_from, password)
        subject = 'CLOSING the computer'
        text = f'The script opened {starttime} run for {runtime} until {closetime} and now is closing'
        msg = f'Subject: {subject}\n\n{text}'
        server.sendmail(email_from, email_to, msg, subject)
        server.quit()


class Computer:
    def shut_down(self, wait_time):
        # shutdown the computer
        time_event = threading.Event()
        time_event.wait(wait_time)
        shut_down = 'shutdown -s -t 0'
        return os.system(shut_down)

    def move_pointer(self, interval, waittime_between_interval, waittime_space):
        for _ in range(interval):
            # time_event = threading.Event()
            # time_event.wait(waittime_between_interval)
            time.sleep(waittime_between_interval)
            pyautogui.moveTo(638, 806, duration=1)
            pyautogui.moveTo(569, 454, duration=1)
            pyautogui.press('space')
            # time_event.wait(waittime_space)
            time.sleep(waittime_space)
            pyautogui.press('space')
