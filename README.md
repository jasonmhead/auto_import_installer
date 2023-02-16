# install_imports

Given a Python file, this function installs any required packages that are imported but not already installed.

## Usage

```python
import auto_import_installer
`current_file_path = os.path.abspath(__file__)`
`imports_installed = auto_import_installer.install_imports(current_file_path)`

modules = install_imports('my_file.py')
```

# Parameters

    `filename`: A string representing the path to a Python file.

# Returns

A list of strings representing the names of the packages that were installed.

The function reads the given file and searches for import statements. If an import statement includes a package that is not installed, the function uses pip to install that package. Only the root package of each import statement is installed; subpackages are not installed. If a package is already installed, the function skips it and moves on to the next one.

Note that this function only works for Python files that are importable modules, and does not work for scripts that are intended to be executed from the command line.


Example
modules = install_imports('my_file.py')

Append this to the top of your file to attempt automatic import installs


`current_file_path = os.path.abspath(__file__)`
`imports_installed = install_imports(current_file_path)`

Note:\
This code was ChatGPT generated with the following instructions:\
This could have been be streamlined, but this was the genesis.\

```
create a python function that will check a .py file for all imports and return an array of imported modules

create a python function that will check a .py file for all imports and return an array of imported modules

modify get_imports function so it only trys to install the root package|
for example:
if given simple_http_server.Headers it should install simple_http_server before the .

modify get_imports function so it only trys to install the root package|
for example:
if given simple_http_server.Headers it should install simple_http_server before the .
```
