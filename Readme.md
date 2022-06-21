# Python Automation Readme.md
-----------------------------
forked from https://github.com/ifrankandrade/automation

## Environment
This repo contains the course materials for the FreeCode course on python automation. It uses non-standard libraries (i.e. not usually installed libraries as part of a standard installation). A `requirements.txt` file defines the required libraries to run this code plus the cheat sheet he collects your personal information to obtain via email.

To create the virtual environment to run this code, do the following in a command-line shell
```bash
python3 -m venv venv
source ./venv/bin/activate
python3 -m pip install -r requirements.txt
```

## (0:00:31) Project 1a -- Table Extraction - Extract CSV Files from Websites
To start the first exercise, run `jupyter-lab`.  It will bring up a Jupyter server and display the current repo in the web browser.  For more information, see [link](https://codeberryschool.com/blog/en/how-to-run-a-python-program-in-jupyter-notebook/).
```bash
jupyter-lab
# web browser will display workspace
```

## (0:09:38) Project 1b -- Table Extraction - Extract Tables from PDFs

This video uses an IDE with code completion to run the `Extract Tables from PDFs.py` file.  It requires camelot be installed but the video directs you to install `camelot-py`. This won't work on a M1 Mac and you have to [install `opencv-python`, ghostscript, and tk to get it to work.](https://camelot-py.readthedocs.io/en/master/user/install-deps.html).

The following environment variable needs to be set:
```bash
export DYLD_LIBRARY_PATH=/opt/homebrew/lib
```

brew installs these dependencies for ghostscript (use this to cleanup):
```text
jbig2dec libidn little-cms2 openjpeg
```

## (0:13:06) Project #2 - Web Automation & Web Scraping - HTML Basics


