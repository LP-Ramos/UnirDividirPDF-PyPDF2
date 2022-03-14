def check_com(value):
    try:
        com = int(value)
        if com > 3 or com < 0:
                return False
        else:
            return True
    except:
        return False
