from setuptools import setup,find_packages

setup(
  name='codeit',
  packages = find_packages(),
  version='1.0.0',
  author='Aadhitya A',
  author_email='aadhitya864@gmail.com',
  description = 'A CLI tool to create CPP files for any contest',
  long_description = 'readme',
  long_description_content_type="text/markdown",
  license = 'GPL-3.0',
  py_modules=['codeit'],
  url="https://github.com/Arch2x/codeit",
  classifiers=(
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3.8'
    ),
  python_requires='>=3.5',
  include_package_data = True,
  install_requires=[
    'watchdog',
    'clint'
  ],
  entry_points={
    'console_scripts': [
      'codeit = codeit.codeit:main'
    ]
  }
)
