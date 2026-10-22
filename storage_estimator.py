storage_gb = float(input("Enter storage in GB: "))
storage_mb = storage_gb * 1024
print("Storage in MB:", storage_mb)

# Task 2 Improvement: Convert to Bytes
storage_bytes = storage_mb * 1024 * 1024
print("Storage in Bytes:", storage_bytes)