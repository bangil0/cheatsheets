## Using Sphinx
  * In cmd or terminal > `sphinx-quickstart`
  * master document is the home page
  * `make html` OR `./make html` (in atom powershell) command to create html document, note to cd to folder where rst file is stored
  * Html pages stored under `_build/html` folder

## Themes
  * Built in themes: `alabaster` (default), `classic`, `sphinxdoc`, `scrolls`, `agogo`, `traditional`, `nature`, `haiku`, `pyramid`, `bizstyle`
  * Nicest theme is provided by readthedocs.org. View here on how to install https://pypi.python.org/pypi/sphinx_rtd_theme
  * `pip install sphinx_rtd_theme`
  * Add config.py with

``` 
import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
```

## Headings
  * header 1 ====
  * header 2 -------
  * header 3 \*\*\*\*\*\*\*
  
## Auto Docstrings
  * A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition
  * Ensure the docstrings are formatted correctly
  * Set `y` to set autodoc at `sphinx-quickstart` stage
  * At conf.py uncomment the following
  
```
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
```

  * Change abspath if python code is in different directory
  * In rst file, set python file name without extension

```
.. automodule:: filename
    :members:
```

## Sidebar
```
.. sidebar:: title
 
    *Paragraph 1*. Statement 1.
 
    *Paragraph 2*. Statement 2.
```

## Table of Contents
  * Define max depth to display based on headers === & ----
  * Add in additional pages (.rst files) using the file name
  * Add auto-numbering if necessary
  
```
.. toctree::
   :maxdepth: 1
   :caption: Contents
   :numbered:
  
   page 1
   page 2
```

## Tables
  * Use the table generator in the link: http://www.tablesgenerator.com/text_tables

## Other Commands
  * __Blocks__: enclosed in backticks \` \`
  * __Shell Code__: triple arrows give syntax highlighting `>>> print something`
  * __Small Red Block__: enclosed in double backticks \`\` \`\`
  * __Bold__: enclosed in double asterieks ** **
  * __Italics__: enclosed in asterieks * *
  * __Line Break__: pipe |
  * __Undo Commands__: \
  * __Images__: `.. image:: workflow.png`
  * __Hyperlink__: assign a variable then call hyperlink below:
  ```
  Document dated Jun 2000. Download_.

  .. _Download: https://tools.ietf.org/html/rfc2865
  ```
  

## Resources
  * __Sphinx Documentation__: http://www.sphinx-doc.org/en/stable/index.html
  * __Cheatsheet Matplotlib__: http://matplotlib.org/sampledoc/cheatsheet.html
  * __Cheatsheet Ralsina__: https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst
  * __Themes__: http://www.writethedocs.org/guide/tools/sphinx-themes/
  * __Docstrings__: https://www.python.org/dev/peps/pep-0257/
  * __Autodoc__: https://codeandchaos.wordpress.com/2012/07/30/sphinx-autodoc-tutorial-for-dummies/