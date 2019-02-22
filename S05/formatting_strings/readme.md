Format
------
```python
<str> = f'{<el_1>}, {<el_2>}'
<str> = '{}, {}'.format(<el_1>, <el_2>)
```

```python
>>> Person = namedtuple('Person', 'name height')
>>> person = Person('Jean-Luc', 187)
>>> f'{person.height:10}'
'       187'
>>> '{p.height:10}'.format(p=person)
'       187'
```

### General Options
```python
{<el>:<10}       # '<el>      '
{<el>:>10}       # '      <el>'
{<el>:^10}       # '   <el>   '
{<el>:->10}      # '------<el>'
{<el>:>0}        # '<el>'
```



### String Options
**`'!r'` calls object's repr() method, instead of format(), to get a string.**
```python
{'abcde'!r:<10}  # "'abcde'   "
```

```python
{'abcde':.3}     # 'abc'
{'abcde':10.3}   # 'abc       '
```

### Number Options
```python
{1.23456:.3f}    # '1.235'
{1.23456:10.3f}  # '     1.235'
```

```python
{ 123456:10,}    # '   123,456'
{ 123456:10_}    # '   123_456'
{ 123456:+10}    # '   +123456'
{-123456:=10}    # '-   123456'
{ 123456: }      # ' 123456'
{-123456: }      # '-123456'
```

```python
{65:c}           # 'A'
{3:08b}          # '00000011' -> Binary with leading zeros.
{3:0<8b}         # '11000000' -> Binary with trailing zeros.
```

#### Float presentation types:
* **`'f'` - Fixed point: `.<precision>f`**
* **`'%'` - Percent: `.<precision>%`**
* **`'e'` - Exponent**

#### Integer presentation types:
* **`'c'` - character**
* **`'b'` - binary**
* **`'x'` - hex**
* **`'X'` - HEX**
