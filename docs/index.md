# Getting started

A number of common steps for combining pytest-bdd with pytest-splinter.

## Installation

```sh
pip install pytest-bdd-splinter
```

## Configuration
Create or update your `conftest.py` file to import the steps from this
library so that they are available within your feature files.

```python
from pytest_bdd_splinter import *  # noqa
```

The next step is to set a default base url, this can be done by creating the
following fixture:
```python
@pytest.fixture(scope="session")
def browser_base_url():
    return "http://localhost:5000"
```
