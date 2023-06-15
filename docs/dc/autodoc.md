# autodoc
Include documentation from **docstrings**\
※ docstrings: python class, method(function) 에 대한 설명(주석)

```{note}
For Sphinx (actually, the Python interpreter that executes Sphinx) to find your module, it must be importable. That means that the module or the package must be in one of the directories on sys.path – adapt your sys.path in the configuration file accordingly.
```
```{warning}
autodoc imports the modules to be documented. If any modules have side effects on import, these will be executed by autodoc when sphinx-build is run.

If you document scripts (as opposed to library modules), make sure their main routine is protected by a if __name__ == '__main__' condition.
```
## 