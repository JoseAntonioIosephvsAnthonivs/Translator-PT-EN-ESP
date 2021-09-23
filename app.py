from sys import platform
from cx_Freeze import setup, Executable


base = None
if platform == 'win32':
	base = 'Win32Gui'

setup(
	name='tradutor_do_iosephvs',
	version='1.0',
	description='tradutor pt,eng,esp',
	options={
		'build_exe': {
			'includes':['tkinter','ttkthemes']
		}
	},
	executables=[
		Executable('tradutor.py', base=base)
	],
)