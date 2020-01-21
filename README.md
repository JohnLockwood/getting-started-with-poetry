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

