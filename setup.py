from setuptools import setup, find_packages

setup(
    name='gpx2csv',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'gpx2csv=gpx2csv.converter:main',
        ],
    },
)
