# MLFlow Server Proxy 

This package was built using the [`jupyter-server-proxy` cookiecutter template](https://github.com/jupyterhub/jupyter-server-proxy/tree/master/contrib/template).

## Installation

You can currently install this package from PyPI.

```bash
pip install mlflow-server-proxy
```

To install with all the resources then use 

```bash
pip install 'mlflow-server-proxy[resources]'
```
The above command will install mlflow as well.

## Setup 

The environment variable `MLFLOW_STORE` has to be set as backend storage for mflow to log models and artifacts. Default is `/tmp`

## Requirements

#### Install Mlflow 

This package's executes the standard `mlflow server` command. This command assumes the `mlflow` executable required to start the application is globally available.

```bash
pip install mlflow
```

### Install Jupyter Notebook

This extension relies on the Jupyter Notebook to run. [Refer to Jupyter's official documentaion](https://jupyter.org/install) for installation instructions.

## Release History

* Version 0.0.1
    * Initial release 

## Contributing

We welcome Your interest in the American Express Open Source Community on Github. Any Contributor to
any Open Source Project managed by the American Express Open Source Community must accept and sign
an Agreement indicating agreement to the terms below. Except for the rights granted in this 
Agreement to American Express and to recipients of software distributed by American Express, You
reserve all right, title, and interest, if any, in and to Your Contributions. Please
[fill out the Agreement](https://cla-assistant.io/americanexpress/mlflow-server-proxy).

## License

Any contributions made under this project will be governed by the
[Apache License 2.0](./LICENSE.txt).

## Code of Conduct

This project adheres to the [American Express Community Guidelines](./CODE_OF_CONDUCT.md). By participating, you are expected to honor these
guidelines.

## Attributions

- [`jupyter-server-proxy`](https://github.com/jupyterhub/jupyter-server-proxy)

### Maintainer
 - Bharath
