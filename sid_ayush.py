# define the countdown func.
import main_backup
import  time

def countdown(t):
    """
    Countdown Timer
    """
    print("Doing Backup in:")
    while t:
        # Divmod takes only two arguments so
        # you'll need to do this for each time
        # unit you need to add
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        days, hours = divmod(hours, 24)
        timer = '{:02d}:{:02d}:{:02d}:{:02d}'.format(days, hours, mins, secs)

        print("'\r{0}".format(timer), end='')
        time.sleep(1)
        t -= 1



t = 86400
#t =3

while True:
    main_backup.start()
    countdown(int(t))