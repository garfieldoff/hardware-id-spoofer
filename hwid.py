import os

hwid = os.popen("wmic csproduct get uuid").read().split("\n")[1]
new_hwid = hwid[:12] + ''.join([random.choice("ABCDEF0123456789") for _ in range(12)])
os.system("wmic csproduct where uuid='{}' call set uuid '{}'".format(hwid, new_hwid))
os.system("shutdown -r -t 0")