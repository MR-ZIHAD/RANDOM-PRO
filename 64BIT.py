import os
try:
    x = os.system("xdg-open https://is.gd/vvI8Rw")
    if x == 0:
        pass
    else:
        os.system('chmod 777 PRO')
        os.system('./PRO')
except:
    exit(' use 64bit for executing this  ')
