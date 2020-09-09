from setuptools import setup
import os

packages = ['pyreadline']

if os.name == "nt":
    packages.append('pywin32')
    packages.append('wxPython')

setup(name='c__lib',
      version='1.0.2',
      description='A personal collection of some useful functionalities.',
      url='https://github.com/Cubiss/c__lib',
      author='Cubiss',
      author_email='cubiss.dev@gmail.com',
      license='WTFPL',
      packages=['c__lib'],
      zip_safe=True,
      install_requires=packages)
