from setuptools import setup, find_packages
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='Py-loader',
  version='1.0',
  description='Simply Downloads File',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Ansh Dadwal',
  author_email='anshdadwal298@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Downloader', 
  packages=find_packages(),
  install_requires=['requests'] 
)
