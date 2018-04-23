from setuptools import setup

setup(
    name='dpos-deputy',
    version='0.0.1',
    packages=[''],
    url='https://github.com/BlockHub/dpos-CLI',
    license='MIT',
    author='Charles',
    author_email='karel@blockhub.nl',
    description='CLI for managing dpos delegates',
    install_requires=[
        'Click', 'Arky==1.3.1', 'dpostools==0.1.0', 'pid',
        'psycopg2-binary', 'raven', 'simple-crypt', 'pycrypto',
    ],
    py_modules=['cli'],
    entry_points='''
        [console_scripts]
        deputy=deputy:main
    ''',
    include_package_data=True,
)
