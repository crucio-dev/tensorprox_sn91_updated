from setuptools import setup, find_packages

setup(
    name="tensorprox",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "bittensor",
        "loguru",
        "aiohttp",
        "asyncssh",
        "pydantic",
        "numpy",
        "pyroute2",
    ],
)