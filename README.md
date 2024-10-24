# GooseDB

<img src="./assets/GooseDB.png" alt="GooseDB" width="300"/>

GooseDB, a chaotic wrapper around DuckDB that randomly interrupts your database operations with goose attacks! Here are the key features:

- Maintains all DuckDB functionality while adding unpredictable goose behavior
- Configurable honk_probability to control how aggressive the goose is
- Various goose attacks ranging from judgmental stares to keyboard pecking
- Dramatic pauses during attacks to maximize chaos
- Full passthrough to DuckDB methods when the goose isn't attacking

## Installation

You can install GooseDB via pip:

```sh
pip install goosedb
```

## Usage

Here is a quick example of how to use GooseDB:

```python
import goosedb

# Create a connection to GooseDB (which wraps DuckDB)
conn = goosedb.connect()

# Set the honk probability (0.2 means 20% chance of goose interference)
conn.honk_probability = 0.2

# Execute a query
conn.execute("SELECT * FROM my_table")
```

### Configuring Goose Behavior

GooseDB lets you control the level of chaos introduced by the goose:

- **honk_probability**: A float between 0 and 1 that represents how often the goose will attack. A higher value means a more aggressive goose.

Example:

```python
conn.honk_probability = 0.5  # 50% chance of goose interference
```

### Goose Attacks

GooseDB has several types of "goose attacks":

- **Judgmental Stares**: The goose stops your query with an unsettling stare.
- **Keyboard Pecking**: The goose pecks at your virtual keyboard, potentially causing errors.
- **Dramatic Pauses**: The goose takes over and delays execution to add chaos.

### Running Queries

GooseDB fully supports DuckDB's functionality when the goose isn't attacking:

```python
# Example of a standard query
results = conn.execute("SELECT COUNT(*) FROM users").fetchall()
print(results)
```

## Reducing the Image Size in README

To make the image smaller in your README, you can use HTML to specify the image width:

```html
<img src="./assets/GooseDB.png" alt="GooseDB" width="300" />
```

This allows you to control the size directly in Markdown.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
