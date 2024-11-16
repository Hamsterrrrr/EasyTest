from setuptools import setup, find_packages # type: ignore

setup(
    name="EasyTest",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pytest",
        "allure-pytest",
        "appium-python-client",
        "python-dotenv",
    ],
)