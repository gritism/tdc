---
py-config:
  splashscreen:
    autoclose: true
  packages:
  - matplotlib
---

# Example with MyST

## `py-repl` and `py-terminal`

We can create a REPL which will output to a `div` and print `stdout` to a terminal with:

````md
```{py-repl}
:output: replOutput

print("hallo world")
import matplotlib.pyplot as plt
plt.plot([1, 2, 3])
plt.gcf()
```

<div id="replOutput"></div>

```{py-terminal}
```
````

Press `shift+enter` to run the code.

```{py-repl}
:output: replOutput

print("hallo world")
import matplotlib.pyplot as plt
plt.plot([1, 2, 3])
plt.gcf()
```

<div id="replOutput"></div>

```{py-terminal}
```

```{helloworld}