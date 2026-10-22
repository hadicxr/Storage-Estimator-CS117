storage_gb = float(input("Enter storage in GB: "))
storage_mb = storage_gb * 1024
print("Storage in MB:", storage_mb)

# Task 2 Feature: Convert to Bytes
storage_bytes = storage_mb * 1024 * 1024
print("Storage in Bytes:", storage_bytes)

# Task 5 Feature: Convert to Terabytes
storage_tb = storage_gb / 1024
print("Storage in TB:", storage_tb)