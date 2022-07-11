import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Its time to do Exercise",
            message = '''It will help you to control your weight and Reduce your risk of heart diseases.''',
            app_icon = "D:\PYTHON PROJECTS\REMINDER\exercise_sport_13306.ico",
            timeout = 10
        )
        time.sleep(60*60)