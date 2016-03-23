from setuptools import setup, find_packages

setup(
    name='ooxx1024',
    version='0.1.0',
	description='A high-speed Robust Torrent Download Package',
	author='Rokic',
	packages=find_packages(),
	include_package_data=True,
	zip_safe=False,
    install_requires=[
        'requests',
		'beautifulsoup4>4.1',
		'lxml',
    ],
)