# import os
from poetry.factory import Factory
from poetry.utils._compat import Path
from poetry.utils.env import EnvManager


poetry = Factory().create_poetry(Path.cwd())

def get_poetry_venv_path():    
    manager = EnvManager(poetry)
    venv = manager.list()[0]
    return venv.path

# def get_venv_path():
#     stream = os.popen('poetry env list --full-path')    
#     path_with_activated = stream.read()
#     return path_with_activated


def get_packages():
    '''Return the non-dev poetry packages as a list of names'''
    #pkgs = []
    include_dev = False
    locked_repo = poetry.locker.locked_repository(include_dev)
    packages = locked_repo.packages
    return [package.name for package in packages ]
    #pkgs.append("Hey Moe")
    #pkgs.append("Hey Larry!")
    #return pkgs
    

if __name__ == "__main__":
#    print("Shelling: ", get_venv_path())
    print("Poetry: ", get_poetry_venv_path())
    print(get_packages())