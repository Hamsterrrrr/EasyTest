from setuptools import setup, find_packages

setup(
    name='easytester',
    version='0.1',
    packages=find_packages(),
    description='A simple and easy-to-use testing library for web and mobile applications',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='hamsterrrrr',
    author_email='radzabovibragim80@gmail.com',
    url='https://github.com/Hamsterrrrr/EasyTest',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'selenium',
        'appium-python-client',
        'allure-pytest',
    ],
)