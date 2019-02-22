### Open Function
**Opens file and returns a corresponding file object.**

```python
<file> = open('<path>', mode='r', encoding=None)
```

#### Modes:
* **`'r'`  - فقط خواندن (پیش فرض).**
* **`'w'`  - نوشتن (truncate).**
* **`'x'`  - نوشتن (در صورتی که فایل وجود داشته باشد، با خطا روبرو می‌شود).**
* **`'a'`  - الحاق.**
* **`'w+'` - خواندن و نوشتن (truncate).**
* **`'r+'` - خواندن و نوشتن از ابتدای فایل.**
* **`'a+'` - خواندن و نوشتن از انتهای فایل.**
* **`'t'`  - حالت متنی (پیش‌فرض).**
* **`'b'`  - حالت باینری.**

#### تابع `seek()`:
```python
<file>.seek(0)                 # Move to start of the file.
<file>.seek(offset)            # Move 'offset' chars/bytes from the start.
<file>.seek(offset, <anchor>)  # Anchor: 0 start, 1 current pos., 2 end.
```

#### خواندن فایل
```python
def read_file(filename):
    with open(filename, encoding='utf-8') as file:
        return file.readlines()
```

#### نوشتن فایل
```python
def write_to_file(filename, text):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
```


### دستور `With`

```python
>>> with open('test.txt', 'w') as file:
...     file.write('Hello World!')
>>> with MyOpen('test.txt') as file:
...     print(file.read())
Hello World!
```
