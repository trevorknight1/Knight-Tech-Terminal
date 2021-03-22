from setuptools import setup


setup(
    name='terminal',
    version='0.1.0',
    packages=['terminal'],
    include_package_data=True,
    install_requires=[
        'Flask==1.1.1',
        'blessings==1.7',
        'sh==1.12.14',
    ],
)