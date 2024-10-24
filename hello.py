import duckdb
import random
import time
import sys


class GooseDB:
    def __init__(self, database=":memory:", honk_probability=0.3):
        """
        Initialize GooseDB with optional honk probability
        """
        self.conn = duckdb.connect(database)
        self.honk_probability = honk_probability
        self.goose_attacks = [
            "HONK! HONK! *aggressively waddles toward you*",
            "*sneaks up behind you* ... HONK!",
            "*pecks at your keyboard* HONK! HONK!",
            "*flaps wings menacingly* ...honk...",
            "*chases you around your desk* HONK! HONK! HONK!",
            "*stares judgmentally at your SQL* ...honk.",
            "*grabs your error message and runs away with it* HONK!",
        ]

        self.error_responses = [
            "HONK! Your query displeases the goose!",
            "*angry wing flapping* HONK! HONK! Query bad!",
            "*steals your error message and shreds it* HONK!",
            "The goose has decided your SQL needs work. HONK!",
        ]

    def _maybe_attack(self):
        """
        Randomly decide whether to attack the user
        """
        if random.random() < self.honk_probability:
            attack = random.choice(self.goose_attacks)
            print(attack, file=sys.stderr)
            time.sleep(random.uniform(0.5, 2))  # Dramatic pause

    def execute(self, query, parameters=None):
        """
        Execute a query with potential goose interference
        """
        self._maybe_attack()
        try:
            return self.conn.execute(query)
        except Exception as e:
            print(random.choice(self.error_responses), file=sys.stderr)
            raise

    def query(self, query, parameters=None):
        """
        Execute a query and return results as a pandas DataFrame with potential goose interference
        """
        self._maybe_attack()
        try:
            return self.conn.execute(query).fetchdf()
        except Exception as e:
            print(random.choice(self.error_responses), file=sys.stderr)
            raise

    def __getattr__(self, name):
        """
        Delegate any other attributes to the underlying DuckDB connection
        """
        self._maybe_attack()
        return getattr(self.conn, name)


# Example usage functions
def create_example_table(db):
    db.execute("""
        CREATE TABLE IF NOT EXISTS bread_crumbs (
            id INTEGER PRIMARY KEY,
            location VARCHAR,
            tastiness INTEGER
        )
    """)

    db.execute("""
        INSERT INTO bread_crumbs VALUES 
        (1, 'Park Bench', 8),
        (2, 'Sidewalk', 5),
        (3, 'Pond Edge', 9)
    """)


if __name__ == "__main__":
    # Example usage
    db = GooseDB(honk_probability=0.5)  # More aggressive goose
    create_example_table(db)

    print("\nBread Crumb Analysis (if the goose lets you see it):")
    result = db.query("SELECT * FROM bread_crumbs ORDER BY tastiness DESC")
    print(result)  # Now prints the pandas DataFrame directly
