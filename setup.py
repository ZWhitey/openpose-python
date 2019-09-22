from setuptools import setup


setup(name='python-openpose',
      version='1.5.1',
      description='OpenPose for Pypi',
      author='Whitey',
      url='https://github.com/ZWhitey/openpose-python',
      license='GPL-3.0',
      keywords='openpose',
      packages=['openpose'],
      install_requires=[],
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Programming Language :: Python :: 3.6'

        ],
    include_package_data=True,
    package_data={'openpose':['*.pyd']},
      python_requires='~=3.6'
     )
