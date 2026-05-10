#!/usr/bin/env python3
"""12-log_stats"""

from pymongo import MongoClient


def main():
    """Print stats about Nginx logs stored in MongoDB."""
    collection = MongoClient("mongodb://127.0.0.1:27017").logs.nginx
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print(f"{collection.count_documents({})} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {collection.count_documents({'method': method})}")
    print(
        f"{collection.count_documents({'method': 'GET', 'path': '/status'})} status check"
    )


if __name__ == "__main__":
    main()
