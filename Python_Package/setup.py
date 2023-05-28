from setuptools import setup, find_packages

setup(
    name='injectsqli',
    version='0.1',
    description='This will detect SQL injection attacks. and notify the user.',
    author='Pravish',
    author_email='pravisharodrigo7@gmail.com',
    packages=['injectsqli'],
    install_requires=[
        'requests',
    ],
)
