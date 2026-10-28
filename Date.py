import datetime

def jour():
    x = datetime.datetime.now()
    print(x)

def est_mercredi():
    if datetime.datetime.now().strftime("%A") == "Wednesday":
        return True
    return False

if __name__ == '__main__':
    jour()
    print(est_mercredi())