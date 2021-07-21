# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['py_linq']

package_data = \
{'': ['*']}

install_requires = \
['future>=0.18.2,<0.19.0']

setup_kwargs = {
    'name': 'py-linq',
    'version': '1.3.0',
    'description': 'LINQ (Language Integrated Query) is a popular querying language available in .NET. This library ports the language so that developers can query collections of objects using the same syntax. This library would be useful for Python developers with experience using the expressiveness and power of LINQ.',
    'long_description': '![Python package](https://github.com/viralogic/py-enumerable/workflows/Python%20package/badge.svg)\n\n# py-linq #\n\nLINQ (Language Integrated Query) is a popular querying language available in .NET. This library ports the language so\nthat developers can query collections of objects using the same syntax. This library would be useful for Python developers\nwith experience using the expressiveness and power of LINQ.\n\n## Install ##\n\nAvailable as a package from PyPI.\n\n```bash\npip install py-linq\n```\n\n## Usage\n\nTo access the LINQ functions an iterable needs to be wrapped by the Enumerable\n\n```python\nfrom py_linq import Enumerable\nmy_collection = Enumerable([1, 2, 3])\n```\n\n## Documentation ##\n\nPlease visit the project [site](https://viralogic.github.io/py-enumerable) for better documentation\n\n## Contributing ##\n\nContributions are welcomed. This project uses [poetry](https://python-poetry.org/docs/) to handle the few library dependencies. [Pre-commit](https://pre-commit.com/) is also used so that formatting and linting checks are performed on commit.\n\n1. Clone the repository using `git clone https://github.com/viralogic/py-enumerable.git`\n2. Install poetry globally as per the instructions [here](https://python-poetry.org/docs/)\n3. CD into the root of your cloned repository directory and `poetry install` to install all packages from the repository Pipfile.\n4. Install `pre-commit` by typing `poetry run pre-commit install`\n5. You should now be ready to start coding!\n\n\n\n',
    'author': 'Bruce Fenske',
    'author_email': 'bwfenske@ualberta.ca',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/viralogic/py-enumerable',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.1',
}


setup(**setup_kwargs)
