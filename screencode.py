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

print("REM This script was generated with screencode.py")
print("REM The code is " + code)
print("STRING " + code)
print("WAIT_FOR_BUTTON_PRESS")
print("STRING " + code)
