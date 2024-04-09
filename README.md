# Pytest Selenium WebDriver Example
This repo contains the sample code for the article - [How To Use Pytest With Selenium For Web Automation Testing](https://pytest-with-eric.com/automation/pytest-selenium/).

## Selenium Chrome Driver

You will need the Selenium chromedriver

Running:
```bash
chromedriver --version
```

Returns (something like):
```bash
ChromeDriver 123.0.6312.105 (399174dbe6eff0f59de9a6096129c0c827002b3a-refs/branch-heads/6312@{#761})
```

If `chromedriver` is not install [read here to learn how to install chromedriver](CHROMEDRIVER.md)

## Requirements

You will need Python 3.10+ and `pytest` 8+ 

### Use a virtual environment

NOTE: pytest is a third-party library, and you should use a virtual environment and `pip` to install it.
[Read here to learn how to use a virtual environment](VIRTUALENV.md)

## Getting Started - a pytest-selenium example

This is an example of how to install and run `pytest-selenium`, a Selenium plugin for the `pytest` runner.

## Use pip to install pytest

Confirm pip version by running:
```bash
(.venv) $ pip --version
```

Returns:
```bash
pip 24.0 from /Users/ ... /tdd-exercises-python/.venv/lib/python3.11/site-packages/pip (python 3.11)
```

To upgrade, run:
```bash
(.venv) $ pip install --upgrade pip
```

### Install pytest

Install `pytest` by running:
```bash
(.venv) $ pip install pytest
```

Confirm the pytest version by running:
```bash
(.venv) $ pytest --version
```

Returns:
```bash
pytest 8.1.1
```

## Use pip to install pytest-selenium

Install pytest-selenium by running:
```bash
(.venv) $ pip install pytest-selenium
```

# Run the tests
Now, run the automated tests.

Running:
```bash
(.venv) $ pytest
```

Returns
```bash
================================== test session starts ===================================
platform darwin -- Python 3.11.7, pytest-8.1.1, pluggy-1.4.0
driver: Chrome
sensitiveurl: .*
rootdir: /Users/ ... /pytest-selenium-example
configfile: pytest.ini
plugins: variables-3.1.0, html-4.1.1, metadata-3.1.1, base-url-2.1.0, selenium-4.1.0
collected 3 items                                                                        

tests/test_basic_selenium.py ..                                                    [ 66%]
tests/test_page_object_model.py .                                                  [100%]

=================================== 3 passed in 5.58s ====================================
```