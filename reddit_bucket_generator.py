# reddit_bucket_generator.py
import sys

def generate_buckets(base_name):
    suffixes = [
        "uploads", "images", "static", "media", "data", "assets",
        "cdn", "public", "test", "backup", "archive", "logs",
        "photos", "videos", "usercontent", "storage", "snapshots",
        "staging", "content", "files"
    ]
    
    environments = ["", "-dev", "-stg", "-prod"]

    buckets = []
    for env in environments:
        for suffix in suffixes:
            bucket_name = f"{base_name}-{suffix}{env}"
            buckets.append(bucket_name)
    return buckets

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <company_name>")
        sys.exit(1)
    
    company_name = sys.argv[1].lower()
    all_buckets = generate_buckets(company_name)
    
    print("\nGenerated bucket names:")
    for b in all_buckets:
        print(b)
