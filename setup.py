from setuptools import setup


setup(name='python-openpose',
      version='1.5.1',
      description='A pre-built OpenPose wrapper',
      author='Whitey',
      url='https://github.com/ZWhitey/openpose-python',
      project_urls={ 
        'Bug Reports': 'https://github.com/ZWhitey/openpose-python/issues',
        'Source': 'https://github.com/ZWhitey/openpose-python',
      },
      license='GPL-3.0',
      keywords='openpose',
      packages=['pyopenpose'],
      install_requires=[],
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Environment :: Win32 (MS Windows)',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
        ],
        platforms=['win_amd64'],
    include_package_data=True,
    package_data={'pyopenpose':['*.pyd','*.dll']},
      python_requires='>=3.5'
     )
