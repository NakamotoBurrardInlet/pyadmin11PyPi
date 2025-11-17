from setuptools import setup, find_packages

setup(
    name='sysadmin-toolkit',
    version='0.1.0',
    description='A cross-platform Python toolkit for secure system information gathering and logging.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Professional SysAdmin',
    url='https://github.com/NakamotoBurrardInlet/pyadmin11PyPi.git', # Replace with your repo
    packages=find_packages(),
    install_requires=[
        'psutil', # Used for cross-platform system metrics
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
    ],
    keywords='admin system monitoring cross-platform logging',
    python_requires='>=3.8',
)
