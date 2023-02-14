import hashlib

match "hello world":
    case "hello world" as f:
        print(hashlib.sha256(f.encode()).hexdigest())