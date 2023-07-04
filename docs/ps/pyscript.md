---
py-config:
  splashscreen:
    autoclose: true
  packages:
  - matplotlib
---

# pyscript

## hello world
### 1) code
````md
```{py-repl}
:output: replOutput_1

print("hello world")
```
````

### 2) result

```{py-repl}
:output: replOutput_1

print("hello world")
```

<div id="replOutput_1"></div>

## basic chart
### 1) code

````md
```{py-repl}
:output: replOutput_2
import matplotlib.pyplot as plt
plt.plot([1, 2, 3])
plt.gcf()
```
````

### 2) result
* do 'shift+enter' key stroke
```{py-repl}
:output: replOutput_2
import matplotlib.pyplot as plt
plt.plot([1, 2, 3])
plt.gcf()
```

<div id="replOutput_2"></div>

```{py-terminal}
```

## py-script
### 1) code
````md
```{py-script}
:file: pys_test.py
```

print("Let's compute π:")
def compute_pi(n):
    pi = 2
    for i in range(1,n):
        pi *= 4 * i ** 2 / (4 * i ** 2 - 1)
    return pi

pi = compute_pi(100000)
s = f"π is approximately {pi:.3f}"
print(s)
````

### 2) result

```{literalinclude} pys_test.py
:language: python
```

```{py-script}
:file: pys_test.py
:output: replOutput_3
```

<div id="replOutput_3"></div>

```{py-terminal}
```
