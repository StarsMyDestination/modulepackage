# from sound.effects import echo
from . import karaoke
from ..effects import echo

def vocoder_print():
	print('vocoder imported')
	demo = karaoke.Demo()
	demo.demoprint()
	echo.echo_print()


import sys
print(sys.version)



# if __name__ == '__main__':
# 	vocoder_print()