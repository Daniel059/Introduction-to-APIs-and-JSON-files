# JSON and APIs — Introduction & Notes

> **Intermediate Importing Data in Python**
> 
> **Topic:** Interacting with APIs to Import Data from the Web

---

## 1. What is JSON?

**JSON (JavaScript Object Notation)** is a lightweight, human-readable format for storing and exchanging data. It was popularised by Douglas Crockford and is the standard format for real-time server-to-browser communication.

Key characteristics:
- Human readable and easy to understand
- Language-independent — used across Python, JavaScript, Java, and more
- The most common format returned by web APIs

### JSON to Python type mapping

| JSON Type | Example | Python Type |
|-----------|---------|-------------|
| String | `"Nairobi"` | `str` |
| Number (int) | `2006` | `int` |
| Number (float) | `5.6` | `float` |
| Boolean | `true` / `false` | `bool` |
| Null | `null` | `None` |
| Object | `{"key": "value"}` | `dict` |
| Array | `[1, 2, 3]` | `list` |

---

## 2. What is an API?

An **API (Application Programming Interface)** is a set of protocols and routines — essentially a bunch of code — that allows two software programs to communicate with each other.

In the context of data importing:
- APIs expose data from remote servers (e.g. movie databases, encyclopaedias, financial data)
- You send an **HTTP request** with parameters
- The server responds with structured **JSON** data
- You parse that JSON in Python for analysis or storage

### APIs are everywhere

Popular examples include:
- **OMDB API** — The Open Movie Database
- **Wikipedia API** — encyclopaedia data
- **Twitter/X API** — social media data
- **Uber Developers API** — ride and location data
- **Facebook Graph API** — social network data
- **Instagram API** — media and profile data

### Anatomy of an API URL

```
http://www.omdbapi.com/?t=hackers&apikey=YOUR_KEY
│──────────────────────│ │──────────────────────────│
      Base URL                 Query string / parameters

- http          → making an HTTP request
- omdbapi.com   → the API endpoint being queried
- ?t=hackers    → query parameter: search by title "hackers"
- &apikey=...   → authentication key
```

> **Tip:** API URLs are regular URLs — you can paste them directly into a browser to preview the raw JSON response before writing any Python code.

---

## 3. Loading and Exploring JSON in Python

### 3.1 Loading a local JSON file

```python
# Importing the json module and loading the data from the file
import json

with open('snakes.json', 'r') as json_file:
    json_data = json.load(json_file)

print(type(json_data))
```

**Output:**
```
<class 'dict'>
```

> `json.load()` reads from an **open file object** and returns a Python `dict` or `list`.

---

### 3.2 Exploring the JSON data

```python
# Exploring the data
for key, value in json_data.items():
    print(f'{key} : {value}')
```

**Output (snakes.json — Snakes on a Plane, 2006):**
```
Title : Snakes on a Plane
Year : 2006
Rated : R
Released : 18 Aug 2006
Runtime : 105 min
Genre : Action, Adventure, Crime
Director : David R. Ellis
Actors : Samuel L. Jackson, Julianna Margulies, Nathan Phillips, Rachel Blanchard
imdbRating : 5.6
imdbVotes : 114,668
imdbID : tt0417148
```

---

### 3.3 Alternative — using the `keys()` method

```python
# Alternatively
print("*********Using keys() method***********\n")

for key in json_data.keys():
    print(f'{key} : {json_data[key]}')
```

> Both approaches produce the same output. `.items()` is more Pythonic and concise; `.keys()` is useful when you want to inspect or filter keys before accessing values.

---

## 4. Key Functions — Quick Reference

| Function | Input | Use case |
|----------|-------|----------|
| `json.load(f)` | Open file object | Load JSON from a local file |
| `json.loads(s)` | String | Parse a JSON string in memory |
| `r.json()` | `requests` Response | Parse JSON from an HTTP API response |
| `json.dump(data, f)` | dict + file object | Write Python dict to a JSON file |

---

## 5. Connecting to a Live API

```python
import requests

# Build the request
url = 'http://www.omdbapi.com/'
params = {'t': 'Snakes on a Plane', 'apikey': 'YOUR_KEY'}

# Send GET request
r = requests.get(url, params=params)

# Parse and explore the response
json_data = r.json()

for key, value in json_data.items():
    print(f'{key} : {value}')
```

> `requests.get(url, params=params)` automatically encodes the `params` dict into the URL query string — cleaner and safer than building the URL manually.

---

## 6. Further Reading

- [OMDB API Documentation](http://www.omdbapi.com/)
- [Wikipedia API Documentation](https://www.mediawiki.org/wiki/API:Main_page)
- [Python `json` module docs](https://docs.python.org/3/library/json.html)
- [Python `requests` library docs](https://docs.python-requests.org/)