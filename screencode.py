# ######################################################################################################################
#
#              """          screencode.py
#       -\-    _|__
#        |\___/  . \        Created on 22 Sep. 2024 at 10:17
#        \     /(((/        by hmelica
#         \___/)))/         hmelica@student.42.fr
#
# ######################################################################################################################

from random import randint

code = str(randint(0, 9999)).zfill(4)

script = []

script.append("REM This script was generated with screencode.py")
script.append("REM The code is " + code)
script.append("STRING " + code)
script.append("WAIT_FOR_BUTTON_PRESS")
script.append("STRING " + code)

with open("script.txt", "w") as f:
    f.write("\n".join(script))

with open("CODE.txt", "w") as f:
    f.write("Screentime code is " + code)
