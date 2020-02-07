# import os
from poetry.factory import Factory
from poetry.utils._compat import Path
from poetry.utils.env import EnvManager

poetry = Factory().create_poetry(Path.cwd())

def make_lib_path(root_dir, lib_dir):
    '''Given a venv dir path at root_dir, and a library name at lib_dir, return full path'''
    LIB_DIR_ROOT = "Lib"
    LIB_DIR_PACKAGES  = 'site-packages'
    return root_dir.joinpath(LIB_DIR_ROOT, LIB_DIR_PACKAGES, lib_dir)

def get_poetry_venv_paths():    
    '''Get List of virutalEnv paths'''
    manager = EnvManager(poetry)        
    return [venv.path for venv in manager.list()]

def get_packages():
    '''Return the non-dev poetry packages as a list of names'''
    #pkgs = []
    include_dev = False
    locked_repo = poetry.locker.locked_repository(include_dev)
    packages = locked_repo.packages
    return [package.name for package in packages ]

def get_dev_library_directories():
    '''Based on virtualEv'''
    venvs = get_poetry_venv_paths()
    # Assume libs are in first venv.
    venv = venvs[0]
    packages = get_packages()
    dirs = []
    for package in packages:
        dirs.append(make_lib_path(venv, package))
    return dirs
    

if __name__ == "__main__":
    '''For now just prove the concept and exercise the functions'''
    print("Poetry: ", get_poetry_venv_paths())
    print("Type of path:  ", type(get_poetry_venv_paths()[0]))
    print(get_packages())
    for dir in get_dev_library_directories():
        print(dir)