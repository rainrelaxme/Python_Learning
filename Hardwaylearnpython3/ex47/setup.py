try:
	from setuptools import setup 
except ImportError:
	from distutils.core import setup
	
config = {
	'description': 'My Project',
	'author': 'ShawnZhu',
	'url': 'URL to get it all.',
	'download_url': 'Where to download it.',
	'author_emali': 'zxr1110.love@163.com.',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'projectname'
	}