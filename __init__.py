import subprocess
import pkg_resources
import ast
import os

# install needed packages
def install_imports(filename):
    with open(filename) as f:
        node = ast.parse(f.read())

    imports = [n for n in node.body if isinstance(n, ast.Import)]
    module_imports = [n for n in node.body if isinstance(n, ast.ImportFrom)]

    modules = []
    for i in imports:
        modules += [n.name for n in i.names]

    for i in module_imports:
        module_name = i.module
        root_package = module_name.split('.')[0]
        if root_package not in modules:
            try:
                pkg_resources.get_distribution(root_package)
            except pkg_resources.DistributionNotFound:
                print(f"Installing {root_package}...")
                try:
                    output = subprocess.check_output(["pip", "install", root_package], stderr=subprocess.STDOUT)
                    print(output.decode('utf-8'))
                    print(f"{root_package} has been successfully installed.")
                except subprocess.CalledProcessError as e:
                    print(e.output.decode('utf-8'))
                    print(f"Error installing {root_package}.")
            modules.append(root_package)

    return modules