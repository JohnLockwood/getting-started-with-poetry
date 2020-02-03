# getting-started-with-poetry

This repository documents some first steps with Poetry.

I first installed Poetry the [recommended way](https://github.com/python-poetry/poetry/blob/master/README.md), as follows:

```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

## Working around an issue

In my environment, however, I would see an warning when running poetry:

```
poetry The _posixsubprocess module is not being used. Child process reliability may suffer if your program uses threads.
```

Also, I noticed that by default Poetry was setting up new projects to use Python2.7 rather than 3.6, which is what "python" resolved to.

If that wasn't a problem for you, scroll down to [Creating Your First Project](Creating-your-first-project).

I found that this was related to [Poetry issue #1312](https://github.com/python-poetry/poetry/pull/1312), a duplicate of [Poetry issue #1042](https://github.com/python-poetry/poetry/pull/1042)

TL;DR --

A workaround is to go into  ~/.poetry/bin/poetry, and change this:

```
#!/usr/bin/env python
```

to this:

```
#!/usr/bin/env python3
```

Once this is done, the warning should go away and you should be able to create new Python 3 projects.  When this defect is fixed you won't have to worry about this "temporary" solution.

## Creating your first project

Let's see what happens if we let Poetry set up a project for us.  In honor of Poetry's name, let's write a couplet.

```
poetry new couplet
cd couplet
```

If you look around in this directory, you'll see that Poetry has created a few nice things for you -- a directory named couplet, with a starter __init__.py so you know it's trying to set up a [regular package](https://docs.python.org/3/reference/import.html#regular-packages), and, oh look a "tests" directory.  All due respect to the venerable Pip and the controversial Pipenv, so far that's pretty cool.

The root directory contains our main project file that poetry uses, pyproject.toml.  We can see here, for example, that Poetry has also helpfully included pytest for us:

```
[tool.poetry.dev-dependencies]
pytest = "^5.2"
```

So let's try running our tests!  As with Pipenv, you can run a command in the shell using run, so:

```
poetry run pytest
```

This will take several seconds the first time it's run as the virtual environment is set up for you, then:

```
...
== 1 passed in 0.11 seconds ==
...
```
Curious about where Poetry put your virtual environment? The env command lets you find out.

```
poetry env list --full-path

C:\Users\<username>\AppData\Local\pypoetry\Cache\virtualenvs\couplet-oQtpg30g-py3.7 (Activated)
```

## Exporting a requirements.txt file

For builds requiring a requirements.txt file, you can do:

```
poetry export -f requirements.txt -o requirements.txt
```