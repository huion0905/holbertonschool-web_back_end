#!/usr/bin/env python3
"""Function that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def log_stats(mongo_collection):
    """Provides stats about Nginx logs stored in logs database
    and nginx collection"""
    # Get the total number of logs
    total_logs = mongo_collection.count_documents({})

    # Get the number of logs for each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: mongo_collection.count_documents(
            {"method": method}) for method in methods}

    # Get the number of logs for a specific method and path
    specific_log_count = mongo_collection.count_documents(
            {"method": "GET", "path": "/status"})

    # Get the number of status check logs
    status_check_count = mongo_collection.count_documents({"path": "/status"})

    return total_logs, method_counts, specific_log_count, status_check_count


if __name__ == "__main__":
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    # Get and print the log statistics
    total_logs, method_counts, specific_log_count,\
    status_check_count = log_stats(logs_collection)

    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")
    print(f"{status_check_count} status check")
