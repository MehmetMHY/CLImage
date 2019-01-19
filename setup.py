from setuptools import setup

setup(name='climage',
      version='0.1',
      description='Convert images to beautiful ANSI escape codes',
      url='http://github.com/pnappa/CLImage',
      author='Patrick Nappa',
      author_email='patricknappa@gmail.com',
      license='MIT',
      packages=['climage'],
      install_requires=[
          'PIL',
      ],
      zip_safe=False)