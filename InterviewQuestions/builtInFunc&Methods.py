'''# Key Difference: Built-in Function vs Method
| Type                    | What is it?                                 | Called on what?                              | Example                               |
| ----------------------- | ------------------------------------------- | -------------------------------------------- | ------------------------------------- |
| ✅ **Built-in Function** | A global function provided by Python itself | Works on variables or objects as *arguments* | `len(s)`, `type(x)`, `sorted(lst)`    |
| ✅ **Method**            | A function that **belongs to an object**    | Called **on the object itself**              | `"hello".upper()`, `[1, 2].append(3)` |

🎯 Built-in Function Examples
These are available globally (you don't need to import anything):

len("hello")          # returns 5
type(123)             # returns <class 'int'>
sorted([3, 1, 2])     # returns [1, 2, 3]
sum([1, 2, 3])        # returns 6
range(5)              # returns range object

You always pass something inside the parentheses.
Think of it as: function(object)

🎯 Method Examples
Methods are functions that belong to objects (like strings, lists, etc.).
"hello".upper()       # returns "HELLO" → string method
"hello".count('l')    # returns 2        → string method
[1, 2, 3].append(4)   # modifies list     → list method
[1, 2, 3].pop()       # removes last item → list method

You always call it with dot notation, like object.method()

🧪 Mnemonic to Remember
Built-in function: function(object)
Method: object.method()

✅ 1. Python Built-in Functions (with Examples)
These are available globally — no import needed.

| Function   | Description                    | Example                 | Output             |
| ---------- | ------------------------------ | ----------------------- | ------------------ |
| `len()`    | Length of an object            | `len("abc")`            | `3`                |
| `type()`   | Type of an object              | `type(123)`             | `<class 'int'>`    |
| `print()`  | Prints to console              | `print("Hi")`           | `Hi`               |
| `int()`    | Convert to integer             | `int("10")`             | `10`               |
| `str()`    | Convert to string              | `str(123)`              | `"123"`            |
| `float()`  | Convert to float               | `float("3.14")`         | `3.14`             |
| `sum()`    | Sum of iterable                | `sum([1, 2, 3])`        | `6`                |
| `max()`    | Largest item                   | `max([1, 3, 2])`        | `3`                |
| `min()`    | Smallest item                  | `min([1, 3, 2])`        | `1`                |
| `sorted()` | Returns sorted list (new list) | `sorted([3, 1, 2])`     | `[1, 2, 3]`        |
| `range()`  | Generates sequence             | `list(range(3))`        | `[0, 1, 2]`        |
| `input()`  | Takes user input               | `input("Enter name: ")` | *user input*       |
| `abs()`    | Absolute value                 | `abs(-5)`               | `5`                |
| `round()`  | Rounds a number                | `round(3.14159, 2)`     | `3.14`             |
| `bool()`   | Convert to boolean             | `bool("")`              | `False`            |
| `list()`   | Converts to list               | `list("abc")`           | `['a', 'b', 'c']`  |
| `dict()`   | Creates a dictionary           | `dict(a=1, b=2)`        | `{'a': 1, 'b': 2}` |


https://docs.python.org/3/library/functions.html

✅ 2. String Methods (used with "text".method())
| Method            | Example                        | Output            |
| ----------------- | ------------------------------ | ----------------- |
| `upper()`         | `"abc".upper()`                | `"ABC"`           |
| `lower()`         | `"ABC".lower()`                | `"abc"`           |
| `capitalize()`    | `"hello".capitalize()`         | `"Hello"`         |
| `title()`         | `"hello world".title()`        | `"Hello World"`   |
| `strip()`         | `"  hi  ".strip()`             | `"hi"`            |
| `lstrip()`        | `"  hi".lstrip()`              | `"hi"`            |
| `rstrip()`        | `"hi  ".rstrip()`              | `"hi"`            |
| `replace(a, b)`   | `"hi hi".replace("hi", "bye")` | `"bye bye"`       |
| `split(sep)`      | `"a,b,c".split(",")`           | `['a', 'b', 'c']` |
| `join(list)`      | `" ".join(["a", "b"])`         | `"a b"`           |
| `find(sub)`       | `"apple".find("p")`            | `1`               |
| `count(sub)`      | `"apple".count("p")`           | `2`               |
| `startswith(sub)` | `"apple".startswith("a")`      | `True`            |
| `endswith(sub)`   | `"apple".endswith("e")`        | `True`            |
| `isalpha()`       | `"abc".isalpha()`              | `True`            |
| `isdigit()`       | `"123".isdigit()`              | `True`            |
| `isalnum()`       | `"abc123".isalnum()`           | `True`            |

✅ 3. List Methods (used with list.method())
| Method         | Example              | Output / Action        |
| -------------- | -------------------- | ---------------------- |
| `append(x)`    | `lst.append(4)`      | Adds to end            |
| `extend(lst2)` | `lst.extend([5,6])`  | Adds multiple items    |
| `insert(i, x)` | `lst.insert(1, 100)` | Inserts at index 1     |
| `pop()`        | `lst.pop()`          | Removes last element   |
| `remove(x)`    | `lst.remove(3)`      | Removes first 3        |
| `clear()`      | `lst.clear()`        | Empties the list       |
| `index(x)`     | `lst.index(3)`       | Finds index of 3       |
| `count(x)`     | `lst.count(3)`       | Counts 3s in list      |
| `sort()`       | `lst.sort()`         | Sorts in-place         |
| `reverse()`    | `lst.reverse()`      | Reverses list in-place |
| `copy()`       | `lst2 = lst.copy()`  | Makes a copy           |

🧠 Summary to Remember

| You see…              | It's a…       | Example         |
| --------------------- | ------------- | --------------- |
| `len(x)`              | Built-in func | `len("abc")`    |
| `"abc".upper()`       | String method | `str.method()`  |
| `[1, 2, 3].append(4)` | List method   | `list.method()` |


# Confusion
sorted() vs list.sort()
reversed() vs list.reverse()

| Feature           | `sorted()` (function)                          | `list.sort()` (method)             |
| ----------------- | ---------------------------------------------- | ---------------------------------- |
| **Type**          | Built-in **function**                          | List **method**                    |
| **Returns**       | **New list** (doesn't modify original)         | **Sorts in-place**, returns `None` |
| **Works on**      | Any iterable (`list`, `tuple`, `string`, etc.) | Only on **lists**                  |
| **Original list** | Unchanged                                      | **Modified**                       |

nums = [3, 1, 2]

sorted_nums = sorted(nums)   # [1, 2, 3]
print(nums)                  # [3, 1, 2] (unchanged)
print(sorted_nums)           # [1, 2, 3]

nums.sort()                  # sorts nums itself
print(nums)                  # [1, 2, 3]


📌 Use sorted() when you want a new sorted copy, and sort() when you want to sort in-place.

 reversed() vs reverse() — What's the Difference?

 | Feature           | `reversed()` (function)  | `list.reverse()` (method)             |
| ----------------- | ------------------------ | ------------------------------------- |
| **Type**          | Built-in **function**    | List **method**                       |
| **Returns**       | **Iterator** (not list!) | **Reverses in-place**, returns `None` |
| **Works on**      | Any iterable             | Only on **lists**                     |
| **Original list** | Unchanged                | **Modified**                          |


nums = [1, 2, 3]
rev = reversed(nums)         # returns iterator
print(list(rev))             # [3, 2, 1]
print(nums)                  # [1, 2, 3] (unchanged)
nums.reverse()               # modifies nums
print(nums)                  # [3, 2, 1]


📌 Use reversed() when you want a temporary reverse (e.g., in a loop), and reverse() when you want to reverse the list in-place.


| Action           | Use This             | Returns         | Affects Original? |
| ---------------- | -------------------- | --------------- | ----------------- |
| Sort copy        | `sorted(iterable)`   | New sorted list | ❌ No              |
| Sort in-place    | `list.sort()`        | `None`          | ✅ Yes             |
| Reverse copy     | `reversed(iterable)` | Iterator        | ❌ No              |
| Reverse in-place | `list.reverse()`     | `None`          | ✅ Yes             |


Q1. What does sorted([3,1,2]) return?
A) None
B) [1, 2, 3]
C) [3, 1, 2]

Q2. What is the result of this?
python
Copy
Edit
nums = [3, 2, 1]
nums.sort()
print(nums)
A) [3, 2, 1]
B) [1, 2, 3]
C) None

Q3. What does reversed([1,2,3]) return?
A) [3, 2, 1]
B) An iterator
C) None

Q4. Which one changes the original list?
A) sorted()
B) reversed()
C) list.reverse()

Q5. Which gives a new reversed copy?
A) list.reverse()
B) reversed()
C) list.sort()

bbbcb



🔁 Common Confusions: Built-in Functions vs Methods


| Task                       | Built-in Function | Method                                   | ✅ Which to Use                                                 |
| -------------------------- | ----------------- | ---------------------------------------- | -------------------------------------------------------------- |
| Get length of string/list  | `len(s)`          | ❌                                        | ✅ Built-in                                                     |
| Convert to upper case      | ❌                 | `"text".upper()`                         | ✅ Method                                                       |
| Count items in string/list | ❌                 | `"aab".count("a")` or `[1,2,1].count(1)` | ✅ Method                                                       |
| Sort list (new list)       | `sorted(lst)`     | `lst.sort()`                             | Depends: <br> ➤ Copy? → `sorted()` <br> ➤ In-place? → `sort()` |
| Reverse list               | `reversed(lst)`   | `lst.reverse()`                          | Same as above                                                  |
| Sum of numbers             | `sum([1, 2, 3])`  | ❌                                        | ✅ Built-in                                                     |
| Convert to string          | `str(123)`        | ❌                                        | ✅ Built-in                                                     |
| Split string               | ❌                 | `"a,b".split(",")`                       | ✅ Method                                                       |
| Join strings               | ❌                 | `" ".join(["a", "b"])`                   | ✅ Method                                                       |
| Check digit                | ❌                 | `"123".isdigit()`                        | ✅ Method                                                       |
| Find max/min               | `max([1, 2])`     | ❌                                        | ✅ Built-in                                                     |


⚠️ Common Mistakes and Misconceptions

| Mistake               | Why it's wrong              | Correct            |
| --------------------- | --------------------------- | ------------------ |
| `"hello".len()`       | `len()` is NOT a method     | `len("hello")`     |
| `list.count([1,2,3])` | Called wrong object         | `[1,2,3].count(2)` |
| `"abc".sort()`        | Strings have no sort method | `sorted("abc")`    |



🔑 Keyword to Remember
🧩 “Function takes input” → function(object)
🔧 “Method belongs to object” → object.method()

🧠 Mini Cheat Phrase:
“If it starts with the object, it’s a method.
If it wraps the object, it’s a function.”

'''