from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='dpos-deputy',
    version='0.0.1',
    packages=[''],
    long_description=readme(),
    url='https://github.com/BlockHub/dpos-CLI',
    license='MIT',
    author='Charles',
    author_email='karel@blockhub.nl',
    description='CLI for managing dpos delegates',
    install_requires=[
        'Click', 'Arky==1.3.1', 'dpostools==0.1.0', 'pid',
        'psycopg2-binary', 'raven', 'simple-crypt', 'pycrypto',
        'markdown'
    ],
    py_modules=['cli'],
    entry_points='''
        [console_scripts]
        deputy=deputy:main
    ''',
    include_package_data=True,
)
