import os

if os.geteuid() == 0:
    print('Your mac address configuration')
    os.system('spoof-mac.py list')
    print("\n")

    interface = input('Please, type your interface (en0|en1): ')
    os.system('spoof-mac.py randomize ' + interface)
    print("\n")

    print('Here is your new mac address')
    os.system('spoof-mac.py list')
else:
    print('Please run it as ROOT or using SUDO')

