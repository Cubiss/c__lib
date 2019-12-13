from setuptools import setup
import os

packages = ['wxPython', 'pyreadline']

if os.name == "nt":
    packages.append('pywin32')

setup(name='c__lib',
      version='0.6',
      description='A personal collection of some useful functionalities.',
      url='https://drive.google.com/open?id=1fv5MRd_305AriXc_qm2eInxup-YeCHis',
      author='Cubiss',
      author_email='cubiss.dev@gmail.com',
      license='WTFPL',
      packages=['c__lib'],
      zip_safe=True,
      install_requires=packages)
