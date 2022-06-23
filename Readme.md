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

This video uses an IDE with code completion to run the `Extract Tables from PDFs.py` file.  It requires camelot be installed but the video directs you to install `camelot-py`. This won't work on a M1 Mac and you have to [install `opencv-python`, ghostscript, and tk to get it to work](https://camelot-py.readthedocs.io/en/master/user/install-deps.html).

The following environment variable needs to be set:
```bash
export DYLD_LIBRARY_PATH=/opt/homebrew/lib
```

brew installs these dependencies for ghostscript (use this to cleanup):
```text
jbig2dec libidn little-cms2 openjpeg
```

## (0:13:06) Project #2 - Web Automation & Web Scraping - HTML Basics

HTML Element: Tags, tag attributes, content

Common tags:
```html
<head>
<title>
<body>
<header>
<article>
<p> for paragraph
<h1>, <h2>, <h3>: headings

<div> divider
<nav> navigational
<li> list item in an ordered <ol> or unordered list <ul>
<a> anchor for a link reference <a href='https://example.com'> This is an example </a>

<button>
<table> 
<td>: table data
<tr>: table row
<iframe> embeds a page w/i a page
```

## (0:20:57) Web Automation & Web Scraping - HTML Basics - Tree Structure

[Example site](http://subslikescript.com/movie/Titanic-120338)
```html
<article class="main article">
 <h1> Titanic (1997) </h1>
 <p class="plot"> 84 years later ... </p>
 <div class="full-script"> 13 meters. You ... </div>
</article>
```
the site uses a tree structure with a parent node and    repeating sibling nodes using the class attribute
- root: <article class="main-article">
- title: <h1 class="title">
- description: <p class="plot">
- transcript: <div class="full-script">

## (0:24:22) Web Automation & Web Scraping - XPath - Syntax, Functions and Operators

XPath (XML Path Language) is a query language used for selecting nodes from an XML document. It can also be used to scrape websites. The CSS (Cascading Style Sheets) can be used for HTML element attributes to key on repeating elements.

- //tagName selects all elements with a specific name (e.g. //h1 would select all h1 elements in document)
- //tagName[1] select the 1st element
- //tagName[@AttributeName="Value"] 
- functions: contains(), starts-with(), text()
  //tagName[contains(@AttributeName,"Value")]/text()
- Operators: and, or
  //tagName[(expression #1) and (expression #2)]

## (0:28:06) Web Automation & Web Scraping - XPath - Test Your XPath

[XPATH Expression Tester](https://scrapinghub.github.io/xpath-playground)

```html
<article class="main article">
 <h1> Titanic (1997) </h1>
 <p class="plot"> 84 years later ... </p>
 <p class="plot2"> In the end ... </p>
 <div class="full-script"> 
 "13 meters. You should see it."
 "Okay, take her up and over the bow rail."
 </div>
</article>
```

## (0:33:38) Web Automation & Web Scraping - XPath - Special Characters and Syntax

- // selects root nodes anywhere in document (e.g. //article)
- / selects siblings of parent nodeset (e.g. //article/h1)
- .. refers to parent node (e.g. //article/..)
- . refers to current node (e.g. //article/.)
- * (wildcard) refers to all elements (e.g. //article/* returns all the nodes inside article)

Using the [example site](http://subslikescript.com/movie/Titanic-120338) in Chrome to illustrate the full page example.

thanks to [site](https://www.youtube.com/watch?v=Dev9YkNtYks&ab_channel=QAAutomationWorld) for discussion on how to 
search content with XPath on Chrome. On MacOS 12 with Brave, I used **F12** to display the developer's view and 
**COMMAND-F** to display the XPATH analysis feature (the video says control-F which is wrong).

Special characters previously discussed:

- @: select with an attribute
- (): grouping an expression
- [n]: select node #n (starts with 1)

## (0:38:17) 2. Automate The News - Installing Selenium and ChromeDriver

Visit the [Chromedriver site](https://chromedriver.chromium.org/downloads) to download the web driver for your version of Chrome or Brave.  On MacOS, there are separate X86 and M1 versions. The driver is a process that listens to port 9515 when you run the executable inside the Zip file.

Selenium is a python library installed as part of the requirements.txt file with pip3.

## (0:40:34) 2. Automate The News - Creating The Driver

Notes on configuring IntelliJ (and maybe Pycharm) 

[Adding Virtual Environment](https://www.jetbrains.com/help/idea/configuring-local-python-interpreters.html)
[Adding modules with requirements.txt](https://www.jetbrains.com/help/idea/managing-dependencies.html)
[detailed video of virtual environments](https://www.youtube.com/watch?v=o1Vue9CWRxU&ab_channel=EuroPythonConference)

1. define the Python Interpreter in the **Project Structure** (command ;) by clicking '+' under the SDK listing in 
the middle panel, **not** at the bottom of any existing SDK.
2. Specify a virtual environment on the leftmost panel.
3. Specify a directory to store the virtual environment. **It must be empty**.
4. Click OK.
5. In the **Tools > Sync Python Requirements...** menu option, make sure the configuration file `requirements.txt` 
is set in the **Package Requirements File** field and 'Don't Specify Version' is selected for the 
**Version In Requirements** selector.

Initially, running the 1.news-extract-data.py script on MacOS 12 may give the error **“chromedriver” can’t be opened 
because Apple cannot check it for malicious software.** From the **System Preferences > Security & Privacy** control 
panel, click on the **General** tab, and unlock the Padlock by clicking on it and entering your Admin password. 

When Chrome runs, it will display "Chrome is being controlled by automated test software." below the URL bar. Sometimes, 
the Chromedriver will crash with a **unknown error: cannot determine loading status** error. This may be due to 
the site throttling the responce and can occur if you run the application to frequently in succession.

