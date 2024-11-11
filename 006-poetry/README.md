Poetry is basically python's version of nodejs's npm. 

for a bit of background, see - https://towardsdatascience.com/ditch-requirements-use-poetry-00a936fe9b6d


You can install poetry by running a curl command - https://python-poetry.org/docs/#installing-with-the-official-installer




Then create a new poetry based project by running:

```bash
poetry new myApp1
```

For more info see - https://python-poetry.org/docs/basic-usage/


This ends up creating the following boiler plate:

```bash
$ tree myApp1 
myApp1
├── README.md
├── myapp1
│   └── __init__.py
├── pyproject.toml
└── tests
    └── __init__.py

3 directories, 4 files
```

Then copy in the earlier `python-study-guide/005-http-requests-and-json.py` into this tree, and run:

```bash
$ poetry run python myapp1/001-http-requests-and-json.py 
Creating virtualenv myapp1-KWSvBJ9V-py3.12 in /Users/sher/Library/Caches/pypoetry/virtualenvs
Traceback (most recent call last):
  File "/Users/sher/github/python-study-guide/006-poetry/myApp1/myapp1/001-http-requests-and-json.py", line 5, in <module>
    import requests
ModuleNotFoundError: No module named 'requests'

```

This fails as indicated above. So now update `pyproject.toml` wit the new dependency for `requests` module, as indicated here - https://pypi.org/project/requests/

Note, [https://pypi.org/](https://pypi.org/) is the python's equivalent of nodejs's [npmjs](https://www.npmjs.com/)

you can find the request module's version. 

then run `poetry install`:

```zsh
$ poetry install
Updating dependencies
Resolving dependencies... (0.3s)

Package operations: 5 installs, 0 updates, 0 removals

  - Installing certifi (2024.7.4)
  - Installing charset-normalizer (3.3.2)
  - Installing idna (3.7)
  - Installing urllib3 (2.2.2)
  - Installing requests (2.32.3)

Writing lock file

Installing the current project: myapp1 (0.1.0)
```

Now run `poetry show` to confirm that your new package is installed:

```zsh
$ poetry show
certifi            2024.7.4 Python package for providing Mozilla's CA Bundle.
charset-normalizer 3.3.2    The Real First Universal Charset Detector. Open, modern and actively maintained alte...
idna               3.7      Internationalized Domain Names in Applications (IDNA)
requests           2.32.3   Python HTTP for Humans.
urllib3            2.2.2    HTTP library with thread-safe connection pooling, file post, and more.
```

Also notice that `requests` didn't get installed at the system level:

```zsh
$ pip list                                              
Package            Version
------------------ --------
certifi            2024.7.4
charset-normalizer 3.3.2
idna               3.7
pip                24.2
urllib3            2.2.2
```


Now the run command should work:

```zsh
poetry run python myapp1/001-http-requests-and-json.py
{'people': [{'craft': 'ISS', 'name': 'Oleg Kononenko'}, {'craft': 'ISS', 'name': 'Nikolai Chub'}, {'craft': 'ISS', 'name': 'Tracy Caldwell Dyson'}, {'craft': 'ISS', 'name': 'Matthew Dominick'}, {'craft': 'ISS', 'name': 'Michael Barratt'}, {'craft': 'ISS', 'name': 'Jeanette Epps'}, {'craft': 'ISS', 'name': 'Alexander Grebenkin'}, {'craft': 'ISS', 'name': 'Butch Wilmore'}, {'craft': 'ISS', 'name': 'Sunita Williams'}, {'craft': 'Tiangong', 'name': 'Li Guangsu'}, {'craft': 'Tiangong', 'name': 'Li Cong'}, {'craft': 'Tiangong', 'name': 'Ye Guangfu'}], 'number': 12, 'message': 'success'}



Oleg Kononenko
Nikolai Chub
Tracy Caldwell Dyson
Matthew Dominick
Michael Barratt
Jeanette Epps
Alexander Grebenkin
Butch Wilmore
Sunita Williams
Li Guangsu
Li Cong
Ye Guangfu
```

Note you have to run the poetry command from somewhere inside the project, otherwise you'll see an error like this:

```zsh
$ poetry run python 006-poetry/myApp1            
Poetry could not find a pyproject.toml file in /Users/sher/github/python-study-guide or its parents
```


Next, to do `poetry run ...` in debug mode, first you need to run:

```
$ poetry debug info

Poetry
Version: 1.8.3
Python:  3.12.5

Virtualenv
Python:         3.12.5
Implementation: CPython
Path:           /Users/sher/Library/Caches/pypoetry/virtualenvs/myapp1-KWSvBJ9V-py3.12
Executable:     /Users/sher/Library/Caches/pypoetry/virtualenvs/myapp1-KWSvBJ9V-py3.12/bin/python
Valid:          True

Base
Platform:   darwin
OS:         posix
Python:     3.12.5
Path:       /Users/sher/.pyenv/versions/3.12.5
Executable: /Users/sher/.pyenv/versions/3.12.5/bin/python3.12
```

Then add the value of `Executable` to your clipboard, then open up vs code's command palette, e.g. using the shift+command+p short cut, then select "Python: Select Interpreter", then select the `Enter interpreter path...` then paste in the path from your clipboard. Here's a handy shortcut:

```zsh
poetry env info --path | pbcopy

```

After that you open up a file.py and click on the top right play icon, to run your code in debug mode. 

You can also run this on in terminal like this:

```
poetry run python ./006-poetry/myApp1/myapp1/001-http-requests-and-json.py
```

Also if you try run the following (while in the pyproject.toml directory):

```
poetry run python .
```

You'll get:

```
$ poetry run python .                  
/Users/sher/Library/Caches/pypoetry/virtualenvs/myapp1-KWSvBJ9V-py3.12/bin/python: can't find '__main__' module in '/Users/sher/github/python-study-guide/006-poetry/myApp1'
```

According to the [official docs](https://docs.python.org/3/library/__main__.html#main-py-in-python-packages), you just need to add a file called `__main__.py` at the repo's top level, i.e. same level as the `pyproject.toml`. 

