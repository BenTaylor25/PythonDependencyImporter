import os

def dep_import(package_name):
    try:
        globals()[package_name] = __import__(package_name)
    except:
        try:
            os.system(f"pip install {package_name}")
            globals()[package_name] = __import__(package_name)
        except:
            raise Exception("Could not install package.")

if __name__ == '__main__':
    colorama = None   # to hide IDE warning
    dep_import("colorama")
    print(colorama.init)
    