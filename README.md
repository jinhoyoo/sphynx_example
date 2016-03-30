Sphynx documentation example
=============================


1. Install Sphynx.

2. **MOST IMPORTANT**: Write code in Python by following the rule from ['sphynx-and-numpydoc'](https://codeandchaos.wordpress.com/2012/08/09/sphinx-and-numpydoc/).

3. Type ```sphinx-quickstart``` in the terminal on the **project root**. Just create ``` docs``` folder. It's more

  ```
  Welcome to the Sphinx 1.4 quickstart utility.

  Please enter values for the following settings (just press Enter to
  accept a default value, if one is given in brackets).

  Enter the root path for documentation.
  > Root path for the documentation [.]: docs

  You have two options for placing the build directory for Sphinx output.
  Either, you use a directory "_build" within the root path, or you separate
  "source" and "build" directories within the root path.
  > Separate source and build directories (y/n) [n]:n

  ....
  ....
  ....
  Please indicate if you want to use one of the following Sphinx extensions:
  > autodoc: automatically insert docstrings from modules (y/n) [n]: y
  > doctest: automatically test code snippets in doctest blocks (y/n) [n]: n
  > intersphinx: link between Sphinx documentation of different projects (y/n) [n]: n
  > todo: write "todo" entries that can be shown or hidden on build (y/n) [n]: y
  > coverage: checks for documentation coverage (y/n) [n]: n
  > imgmath: include math, rendered as PNG or SVG images (y/n) [n]: n
  > mathjax: include math, rendered in the browser by MathJax (y/n) [n]: n
  > ifconfig: conditional inclusion of content based on config values (y/n) [n]: n
  > viewcode: include links to the source code of documented Python objects (y/n) [n]: y
  > githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]: n
  .......
  ```

4. Check whether ```index.rst``` file is created in ```docs/source``` folder.

5. Change ```conf.py``` in ```docs/source``` folder to access upper module folder.
  ```
  # If extensions (or modules to document with autodoc) are in another directory,
  # add these directories to sys.path here. If the directory is relative to the
  # documentation root, use os.path.abspath to make it absolute, like shown here.
  sys.path.insert(0, os.path.abspath('..'))
  ```

6. Call the command like below to generate ```*.rst``` file for this module. See the [reference](http://www.sphinx-doc.org/en/stable/man/sphinx-apidoc.html).
```sphinx-apidoc -T -M -d 1 -o docs dooboo ```

7. Go to ```docs``` folder by ```cd docs```.

8. Run ```make html``` to create the HTML document.

9. Keep ```docs/conf.py```, ```docs/Makefile```, ```docs/index.rst``` under version control. Because it would be basic document configuration. So just ```sphinx-apidoc -T -M -d 1 -o docs dooboo ``` and run ```make html``` to generate ```dooboo``` packages' document.

Reference
------------
 * [Adding Numpydoc to Sphinx](https://codeandchaos.wordpress.com/2012/08/09/sphinx-and-numpydoc/)
 * [Google Python Style Guide](http://google.github.io/styleguide/pyguide.html)
 * [sphinx-apidoc manual](http://www.sphinx-doc.org/en/stable/man/sphinx-apidoc.html)
