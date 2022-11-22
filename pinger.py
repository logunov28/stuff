import subprocess, ctypes, os
from time import sleep
from datetime import datetime

tempdir = os.getenv('TEMP')
os.chdir(tempdir)

drives = win32api.GetLogicalDriveStrings().split("\x00")[:-1]
flags = []
flag = False

# Первичная проверка
try:
    output = str(subprocess.check_output(["ping", "ya.ru"]).decode('cp866'))
    now = datetime.now().strftime("%H:%M")
    print('На ' + now + ' интернет доступен.')
    flag = True
except:
    print('На ' + now + ' интернет не доступен.')

for i in range(len(drives)):
    try:
        os.chdir(drives[i])
        now = datetime.now().strftime("%H:%M")
        print('На ' + now + ' диск ' + drives[i][0] + ' доступен.')
        flags.append('1')
        os.chdir(tempdir)
    except:
        now = datetime.now().strftime("%H:%M")
        print('На ' + now + ' диск ' + drives[i][0] + ' не доступен.')
        flags.append('0')

print('\nМониторим...\n')

sleep(10)

# мониторинг

while True:
    # Проверяем интернет
    if flag == False:
        try:
            output = str(subprocess.check_output(["ping", "ya.ru"]).decode('cp866'))
            now = datetime.now().strftime("%H:%M")
            print('Интернет появился в ' + now + '!')
            w = ctypes.windll.user32.MessageBoxW(None, u"Интернет заработал!", u"Ура!", 0x1000)
            flag = True
        except:
            pass
    else:
        try:
            output = str(subprocess.check_output(["ping", "ya.ru"]).decode('cp866'))
        except:
            w = ctypes.windll.user32.MessageBoxW(None, u"Интернет отвалился!", u"Беда!", 0x1000)
            now = datetime.now().strftime("%H:%M")
            print('Интернет отвалился в ' + now + '!')
            flag = False
    sleep(5)

    # Проверяем диски
    for i in range(len(drives)):
        if flags[i] == '0':
            try:
                os.chdir(drives[i])
                now = datetime.now().strftime("%H:%M")
                print('Диск ' + drives[i][0] + ' стал доступен в ' + now)
                w = ctypes.windll.user32.MessageBoxW(None, u"Диск " + drives[i][0] + " теперь доступен!", u"Ура!", 0x1000)
                flags[i] = '1'
                os.chdir(tempdir)
            except:
                pass
        else:
            try:
                os.chdir(drives[i])
                os.chdir(tempdir)
            except:
                now = datetime.now().strftime("%H:%M")
                print('Диск ' + drives[i][0] + ' отвалился в ' + now)
                w = ctypes.windll.user32.MessageBoxW(None, u"Диск " + drives[i][0] + " отвалился...", u"Беда!", 0x1000)
                flags[i] = '0'
        sleep(5)





