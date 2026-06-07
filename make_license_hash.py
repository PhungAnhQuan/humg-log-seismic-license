import hashlib

LICENSE_HASH_SALT = "HUMG_LOG_SEISMIC_REMOTE_LICENSE_V1"

license_key = input("Nhap license key can tao hash: ").strip()
license_hash = hashlib.sha256((LICENSE_HASH_SALT + "|" + license_key).encode("utf-8")).hexdigest()
print("License key:", license_key)
print("License hash:", license_hash)
