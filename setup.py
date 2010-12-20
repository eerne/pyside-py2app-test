from setuptools import setup

setup(
	app = ['test.py'],
	options = {
		'py2app': {
			'argv_emulation': False,
			#'plist': {
			#	'LSPrefersPPC': False,
			#},
			'includes': ['PySide.QtCore', 'PySide.QtGui', 'PySide.QtWebKit', 'PySide.QtNetwork'],
		}
	},
	data_files = ['test.html', 'iframe.html'],
	setup_requires = ['py2app'],
)
