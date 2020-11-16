from setuptools import setup
import os

extras_require = {'c__input': ['pyreadline']}

if os.name == "nt":
    extras_require['SysTrayConsole'] = ['pywin32', 'wxPython']

setup(name='c__lib',
      version='1.0.2',
      description='A personal collection of some useful functionalities.',
      url='https://github.com/Cubiss/c__lib',
      author='Cubiss',
      author_email='cubiss.dev@gmail.com',
      license='WTFPL',
      packages=['c__lib'],
      zip_safe=True,
      extras_require=extras_require)
