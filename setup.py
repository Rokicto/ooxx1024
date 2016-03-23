from setuptools import setup, find_packages

setup(
    name='ooxx1024',
    version='0.1.1',
	description='A high-speed Robust Torrent Download Package',
	author='Rokic',
	license="GPL",
	packages=find_packages(),
	include_package_data=True,
	zip_safe=False,
	classifiers=[
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
	],
    install_requires=[
        'requests',
		'beautifulsoup4>4.1',
		'lxml',
    ],
)