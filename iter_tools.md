
# Python `itertools`

`itertools` is Python’s standard-library toolkit for building fast, memory‑efficient iterators. It lets you compose small iterator “lego bricks” to express powerful data pipelines without materializing intermediate lists.

> Works with: **Python 3.8+** (notes included for features added in 3.10 and 3.12)

---

## Why use `itertools`?

- **Speed & memory**: lazy iteration avoids creating big lists.
- **Composability**: functions snap together like pipes.
- **Clarity**: declarative, “what not how,” style.
- **Batteries included**: no external installs—`itertools` ships with Python.

---

## Quick Start

```python
from itertools import count, takewhile, cycle, islice

# even numbers under 20
evens_lt_20 = takewhile(lambda n: n < 20, (n for n in count(0, 2)))
print(list(evens_lt_20))  # [0, 2, 4, ..., 18]

# repeat a pattern
pat = islice(cycle("ABC"), 7)
print("".join(pat))  # ABCABCA
```

---

## Core Building Blocks

Below are the most commonly used tools with bite‑sized examples.

### Infinite Iterators
- `count(start=0, step=1)` – arithmetic progression.
  ```python
  from itertools import count, islice
  list(islice(count(10, 3), 5))   # [10, 13, 16, 19, 22]
  ```

- `cycle(iterable)` – repeat items forever.
  ```python
  from itertools import cycle, islice
  list(islice(cycle([1, 2, 3]), 7))  # [1,2,3,1,2,3,1]
  ```

- `repeat(object, times=None)` – repeat a value.
  ```python
  from itertools import repeat
  list(repeat("hi", 3))  # ["hi", "hi", "hi"]
  ```

### Combinatoric Iterators
- `product(*iterables, repeat=1)` – cartesian product.
  ```python
  from itertools import product
  list(product("AB", [0, 1]))  # [('A',0), ('A',1), ('B',0), ('B',1)]
  ```

- `permutations(iterable, r=None)` – ordered arrangements.
  ```python
  from itertools import permutations
  list(permutations("ABC", 2))  # [('A','B'), ('A','C'), ('B','A'), ...]
  ```

- `combinations(iterable, r)` – unordered, no replacement.
  ```python
  from itertools import combinations
  list(combinations([1,2,3], 2))  # [(1,2), (1,3), (2,3)]
  ```

- `combinations_with_replacement(iterable, r)` – unordered, allow repeats.
  ```python
  from itertools import combinations_with_replacement
  list(combinations_with_replacement("AB", 2))  # [('A','A'), ('A','B'), ('B','B')]
  ```

### Filtering & Slicing
- `compress(data, selectors)` – filter by a mask.
  ```python
  from itertools import compress
  list(compress("abcdef", [1,0,1,0,0,1]))  # ['a','c','f']
  ```

- `dropwhile(pred, iter)` / `takewhile(pred, iter)` – skip/take until predicate fails.
  ```python
  from itertools import dropwhile, takewhile
  list(dropwhile(lambda x: x < 3, [1,2,3,4]))  # [3,4]
  list(takewhile(lambda x: x < 3, [1,2,3,4]))  # [1,2]
  ```

- `filterfalse(pred, iter)` – inverse of `filter`.
  ```python
  from itertools import filterfalse
  list(filterfalse(lambda x: x % 2, range(6)))  # [0,2,4]
  ```

- `islice(iterable, start, stop[, step])` – iterator slicing.
  ```python
  from itertools import islice
  list(islice(range(10), 2, 9, 3))  # [2,5,8]
  ```

### Transforming & Combining
- `accumulate(iterable, func=operator.add, *, initial=None)` – running reduction.
  ```python
  from itertools import accumulate
  import operator
  list(accumulate([1,2,3,4]))               # [1,3,6,10]
  list(accumulate([1,2,3,4], operator.mul)) # [1,2,6,24]
  ```

- `chain(*iterables)` / `chain.from_iterable(iterables)` – flatten one level.
  ```python
  from itertools import chain
  list(chain("ab", "cd", "ef"))  # ['a','b','c','d','e','f']
  ```

- `pairwise(iterable)` – adjacent pairs (Python **3.10+**).
  ```python
  from itertools import pairwise
  list(pairwise([10, 20, 30]))  # [(10,20), (20,30)]
  ```

- `starmap(func, iterable_of_args)` – map with unpacked args.
  ```python
  from itertools import starmap
  list(starmap(pow, [(2,5), (3,2)]))  # [32, 9]
  ```

- `tee(iterable, n=2)` – independent iterator copies.
  ```python
  from itertools import tee
  a, b = tee(range(3))
  list(a), list(b)  # ([0,1,2], [0,1,2])
  ```

- `zip_longest(*iterables, fillvalue=None)` – zip to longest.
  ```python
  from itertools import zip_longest
  list(zip_longest("AB", [1], fillvalue="?"))  # [('A',1), ('B','?')]
  ```

- `groupby(iterable, key=None)` – group consecutive keys.
  ```python
  from itertools import groupby
  data = sorted(["ant", "bear", "bat", "bee"], key=lambda s: s[0])
  {k: list(g) for k, g in groupby(data, key=lambda s: s[0])}
  # {'a': ['ant'], 'b': ['bear', 'bat', 'bee']}
  ```

- `batched(iterable, n)` – fixed-size chunks (Python **3.12+**).
  ```python
  from itertools import batched
  list(batched(range(7), 3))  # [(0,1,2), (3,4,5), (6,)]
  ```

---

## Idiomatic Recipes (copy‑paste friendly)

```python
from itertools import islice, pairwise, accumulate, chain, batched
import operator

def window(iterable, n):
    "Sliding windows of size n -> tuples"
    # For 3.10+, use pairwise with offset zips:
    iters = [islice(iterable, i, None) for i in range(n)]
    return zip(*iters)

def sliding_diffs(nums):
    "First differences"
    return (b - a for a, b in pairwise(nums))

def running_max(iterable):
    "Monotone running maxima"
    return accumulate(iterable, func=max)

def flatten_once(nested):
    "Flatten one level"
    return chain.from_iterable(nested)

def chunks(iterable, n):
    "Batches using itertools.batched when available"
    try:
        from itertools import batched
        return batched(iterable, n)
    except ImportError:
        # fallback
        it = iter(iterable)
        while True:
            batch = list(islice(it, n))
            if not batch:
                return
            yield tuple(batch)
```

---

## Performance & Gotchas

- **Group boundaries**: `groupby` only groups *consecutive* items. Sort first (or choose a proper key) when needed.
- **`tee` memory**: copies are lazy but **cache** data; heavy fan‑out can grow memory.
- **Infinite iterators**: cap with `islice` / `takewhile` or you’ll loop forever.
- **Iterators are single‑use**: many iterators are consumed once; re-create or `tee` if you need to iterate again.
- **Avoid list() prematurely**: keep pipelines lazy for speed & memory.

---

## Real‑World Mini Examples

- **Log lines in 1k‑sized chunks to upload**:
  ```python
  from itertools import batched
  for chunk in batched(log_lines_stream(), 1000):
      upload("\n".join(chunk))
  ```

- **Rolling 7‑day sums**:
  ```python
  from itertools import islice
  def rolling_sum(xs, n=7):
      it = iter(xs)
      win = list(islice(it, n))
      s = sum(win)
      yield s
      for x_out, x_in in zip(xs, it):
          s += x_in - x_out
          yield s
  ```

- **Pairwise distances**:
  ```python
  from itertools import pairwise
  def path_length(points):
      from math import hypot
      return sum(hypot(x2-x1, y2-y1) for (x1,y1),(x2,y2) in pairwise(points))
  ```

---

## Testing Your Understanding

Try these:
1. Use `compress` to keep vowels from a string.
2. Use `dropwhile` to skip leading zeros then convert the rest to int.
3. Use `product` to generate all 3‑letter lowercase “PINs”.

---

## Version Notes

- `pairwise` – added in **Python 3.10**.
- `batched` – added in **Python 3.12**.

For older Python, see the “Idiomatic Recipes” section for backfills.

---

## See Also

- Module docs: `help('itertools')` or the official Python docs.
- `functools`, `operator`, and `collections` often pair well with `itertools`.

---

## License

MIT — do whatever you want; attribution appreciated.
