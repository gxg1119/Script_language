from distutils.core import setup

setup(name = "Accident",
      version = '1.0',
      packages = ['Term', 'Term.res'],
      package_data = {'Term' : ['*'], 'Term.res' : ['*']},
      )