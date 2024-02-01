#!/usr/bin/env python3
"""Function that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def log_stats():
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    logs_count = nginx_collection.count_documents({})
    print(f"{logs_count} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check_count = nginx_collection.count_documents(
            {"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")
