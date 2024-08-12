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

