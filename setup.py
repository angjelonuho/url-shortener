from setuptools import setup, find_packages

setup(
    name='urlshortener',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'fastapi',
        'uvicorn',
        'SQLAlchemy',
        'pytest',
        'pytest-asyncio',
        'requests',
        'psycopg2-binary',
        'SQLAlchemy-Utils',
    ],
)
