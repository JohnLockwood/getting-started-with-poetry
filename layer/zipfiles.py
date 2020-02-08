import os
from pathlib import Path
from poetry.factory import Factory
from poetry.utils.env import EnvManager

poetry = Factory().create_poetry(os.getcwd())

def is_project_file():
    return Path.is_file(Path('pyproject.toml'))

def make_lib_path(root_dir, lib_dir):
    '''Given a venv dir path at root_dir, and a library name at lib_dir, return full path'''
    LIB_DIR_ROOT = "Lib"
    LIB_DIR_PACKAGES  = 'site-packages'
    return root_dir.joinpath(LIB_DIR_ROOT, LIB_DIR_PACKAGES, lib_dir)

def get_poetry_venv_paths():    
    '''Return list of venv paths, though typically only the first matters'''
    manager = EnvManager(poetry)        
    return [venv.path for venv in manager.list()]

def get_package_path():
    '''Returns a tuple with the package name and full path to code'''
    name = poetry.package.name
    return (name, Path(os.getcwd()).joinpath(name))

def get_packages():
    '''Return the non-dev poetry packages as a list of names'''
    #pkgs = []
    include_dev = False
    locked_repo = poetry.locker.locked_repository(include_dev)
    packages = locked_repo.packages
    return [package.name for package in packages ]

def get_dev_library_directories():
    '''Return a list of tuples of non-dev dependencies: [(dependency_name, full_path_to_code)]'''
    venvs = get_poetry_venv_paths()
    # Assume libs are in first venv.
    venv = venvs[0]
    packages = get_packages()
    dirs = []
    for package in packages:
        item = (package, make_lib_path(venv, package))
        dirs.append(item)
    return dirs


def get_directory_tree(dir):
    '''Returns the files in the directory, recursively'''
    allfiles = []
    for root, subFolder, files in os.walk(dir):
        for item in files:
            fileNamePath = str(Path.joinpath(Path(root),item))
            if not '__pycache__' in fileNamePath:
                allfiles.append(fileNamePath)
    return allfiles
    
def run_demo():
    '''For now just prove the concept and exercise the functions'''
    # print("Poetry: ", get_poetry_venv_paths())
    # print("pyproject.toml exists? ", is_project_file())
    # print("Type of path:  ", type(get_poetry_venv_paths()[0]))
    # print(get_packages())
    print("Package dir:  ", get_package_path())


    print("Non-dev dependencies: ")
    for dir in get_dev_library_directories():
        name, path = dir
        if(name == 'requests'):
            files = get_directory_tree(path)
            for f in files:
                print("\t", f)
        print(dir)

if __name__ == "__main__":
    run_demo()