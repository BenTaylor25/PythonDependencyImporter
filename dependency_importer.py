"""
https://github.com/BenTaylor25/PythonDependencyImporter/blob/master/dependency_importer.py
"""

import os

def dep_import(package_name):
    try:
        globals()[package_name] = __import__(package_name)
    except:
        try:
            os.system(f"pip install {package_name}")
            globals()[package_name] = __import__(package_name)
        except:
            raise Exception(f"Could not install package '{package_name}'.")

def install_all(dependencies):
    """
    Call this function at the start of your program with a list of strings;
    the names of all pip dependencies you need to use in your program.
    This will make sure that they are all installed before preceding.
    """

    for d in dependencies:
        dep_import(d)

if __name__ == '__main__':
    colorama = None   # to hide IDE warning
    dep_import("colorama")
    print(colorama.init)
