---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.14.6
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

# pdm


## pdm 설치를 위한 pdm_test 폴더 생성

```python
%cd ~/
%rm -r -d pdm_test
%mkdir pdm_test
%cd pdm_test
```

## pdm 초기화

```python
!pdm init -n
```

```python
!pdm venv create -w virtualenv
```

```python
!pdm use --venv in-project
```

**<pdm init usage>**  

```
    Usage: pdm init [-h] [-v] [-g] [-p PROJECT_PATH] [-k SKIP] [-n]
                    [--python PYTHON]
                    [--backend {pdm-backend,setuptools,flit-core,hatchling,pdm-pep517}]
                    [--lib]

    Initialize a pyproject.toml for PDM

    Options:
      -h, --help            Show this help message and exit.
      -v, --verbose         Use `-v` for detailed output and `-vv` for more
                            detailed
      -g, --global          Use the global project, supply the project root with
                            `-p` option
      -p PROJECT_PATH, --project PROJECT_PATH
                            Specify another path as the project root, which
                            changes the base of pyproject.toml and __pypackages__
      -k SKIP, --skip SKIP  Skip some tasks and/or hooks by their comma-separated
                            names. Can be supplied multiple times. Use ":all" to
                            skip all hooks. Use ":pre" and ":post" to skip all pre
                            or post hooks.
      -n, --non-interactive
                            Don't ask questions but use default values
      --python PYTHON       Specify the Python version/path to use
      --backend {pdm-backend,setuptools,flit-core,hatchling,pdm-pep517}
                            Specify the build backend
      --lib                 Create a library project
```

```python
!pdm venv list
```

## library 설치

```python
!pdm add numpy
```

```python
!pdm list --graph
```

```python
!tree .
```
