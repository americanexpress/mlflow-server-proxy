# Copyright 2020 American Express Travel Related Services Company, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing permissions and limitations under
# the License.

import setuptools
from os import path

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="mlflow-server-proxy",
    version='0.1.0',
    url="https://github.com/americanexpress/mlflow-server-proxy",
    author="American Express",
    description="Jupyter server proxy extension for mlflow tracking server",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    keywords=['jupyter', 'mlflow', 'jupyterhub'],
    license='Apache 2.0 license',
    install_requires=[
        'jupyter-server-proxy'
    ],
    extras_require={
        "resources": ["mlflow"],
        "dev": ["autopep8", "pytest", "flake8", "pytest-cov>=2.6.1", "mock"],
    },
    entry_points={
        'jupyter_serverproxy_servers': [
            'mlflow = mlflow_server_proxy:setup_mlflow'
        ]
    },
    include_package_data=True
)
