# Learn how to install chromedriver

ChromeDriver is used by Selenium for the automated testing of webapps for Google Chrome.

Use this link to learn more about [ChromeDriver](https://chromedriver.chromium.org/)

## Prerequisites

You will need to accomplish the following:
- Install Google Chrome
- Install ChromeDriver
- Set Up a Python Virtual Environment
- Install Selenium

This guide walks you through these steps - [Installation Guide for Google Chrome, ChromeDriver, and Selenium in a Python Virtual Environment](https://katekuehl.medium.com/installation-guide-for-google-chrome-chromedriver-and-selenium-in-a-python-virtual-environment-e1875220be2f)

## MacOS and Homebrew

I used Homebrew to install `chromedriver` on my Mac.

### Homebrew install

I used this Homebrew formula to install `chromedriver`
https://formulae.brew.sh/cask/chromedriver

Running:
```bash
$ brew install --cask chromedriver
```

Installed the `chromedriver` file.

## MacOS error

When `pytest` tries to use `chromedriver`, you will likely get a MacOS error alert:

> “chromedriver” can’t be opened because Apple cannot check it for malicious software.
>
> This software needs to be updated. Contact the developer for more information.

Access to `chromedriver` is blocked.

More info here: 
https://docs.brew.sh/FAQ#why-cant-i-open-a-mac-app-from-an-unidentified-developer

One way to unblock the access, is to follow these steps:

1. Locate the file in Finder 
2. Hold down control
3. Click the application
4. Click open
5. Confirm the dialogue

Afterwards you should be able to open the app without the warning.
