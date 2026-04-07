def swith_func():
    """
    allows the user to turn devices on/off
    and displays the current settings
    """
    try:
        while True:
            user_asc = int(input("""
            1 - power|on
            2 - light|on
            3 - computer|on
            4 - monitor|on
            5 - show settings
            >>>
            """
                         )
                       )
            global swith
            if user_asc == 1:
                swith ^= 0x1
                if swith & 0x1:
                    print('power on')
                else:
                    print('power off')
            elif user_asc == 2:
                swith ^= 0x2
                if swith & 0x2:
                    print('light on')
                else:
                    print('light off')
            elif user_asc == 3:
                swith ^= 0x4
                if swith & 0x4:
                    print('computer on')
                else:
                    print('computer off')
            elif user_asc == 4:
                swith ^= 0x8
                if swith & 0x8:
                    print('monitor on')
                else:
                    print('monitor off')
            elif user_asc == 5:
                status.clear()
                if swith & 0b0001:
                    status.append('power')
                if swith & 0b0010:
                    status.append('light')
                if swith & 0b0100:
                    status.append('computer')
                if swith & 0b1000:
                    status.append('monitor')
                print(status)
    except KeyboardInterrupt:
        print("goodbye")


if __name__ == "__main__":
    status = []
    swith = 0x0
    swith_func()