# src/analytics_project/test-pyspark.py
"""Simple demo test for PySpark installation and basics.

What it does:
- Starts a local SparkSession
- Prints Spark version
- Creates a tiny DataFrame and shows it
- Validates row count and contents
- Stops Spark cleanly
- Exits 0 on success, 1 on failure
"""

from __future__ import annotations

import contextlib
import logging
import sys

from pyspark.sql import SparkSession


def main() -> None:
    """Run PySpark test to validate installation and basic functionality.

    Creates a local SparkSession, tests DataFrame operations, validates results,
    and exits with appropriate status codes (0 for success, 1 for failure).
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    spark = None
    try:
        logging.info("Starting SparkSession...")
        spark = (
            SparkSession.builder.appName("TestPySpark")
            .master("local[*]")
            .config("spark.driver.memory", "2g")
            .config("spark.executor.memory", "2g")
            .getOrCreate()
        )

        print(f"Spark Version: {spark.version}")

        # Sample data
        data: list[tuple[int, str]] = [
            (1, "Alice"),
            (2, "Bob"),
            (3, "Charlie"),
        ]
        # Create DataFrame
        df = spark.createDataFrame(data, ["ID", "Name"])

        print("Displaying DataFrame:")
        df.show()

        # Basic validations
        expected_rows = 3
        actual_rows = df.count()
        if actual_rows != expected_rows:
            print(f"FAIL: Expected {expected_rows} rows, got {actual_rows}")
            sys.exit(1)

        # Validate content (order-agnostic)
        expected_set = {("Alice", 1), ("Bob", 2), ("Charlie", 3)}
        actual_set = {(row["Name"], row["ID"]) for row in df.select("Name", "ID").collect()}
        if actual_set != expected_set:
            print("FAIL: DataFrame contents do not match expected values")
            print(f"Expected: {sorted(expected_set)}")
            print(f"Actual:   {sorted(actual_set)}")
            sys.exit(1)

        print("Test Passed")
        sys.exit(0)

    except Exception as exc:
        logging.error("An error occurred during PySpark test run", exc_info=exc)
        print("FAIL: Exception during test. See logs above.")
        sys.exit(1)
    finally:
        if spark is not None:
            logging.info("Stopping SparkSession...")
            with contextlib.suppress(Exception):
                spark.stop()
                pass


if __name__ == "__main__":
    main()
