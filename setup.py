from setuptools import setup, Extension

yespower_module = Extension('resistance_yespower',
                            sources = ['yespower-module.c',
                                       'yespower.c',
                                       'yespower-opt.c',
                                       'sha256.c'
                                       ],
                            extra_compile_args=['-O2', '-funroll-loops', '-fomit-frame-pointer'],
                            include_dirs=['.'])

setup (name = 'resistance_yespower',
       version = '1.0.1',
       author_email = 'developer@resistance.io',
       author = 'Resistance Developers',
       url = 'https://github.com/ResistancePlatform/resistance_yespower_python3',
       description = 'Bindings for yespower-1.0.1 proof of work used by Resistance',
       ext_modules = [resistance_yespower_module])
