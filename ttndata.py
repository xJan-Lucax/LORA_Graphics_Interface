import ttn_storage_api

key = "NNSXS.KMD3MBZAVR4HCFMYJ3UTCVWZ34SVFRG3FAGGOWI.AWFTZON664S3GATFSI3COT7KAKKB42UK2D4QKIBOB3VXYYRU325A"
print(ttn_storage_api.sensor_pull_storage("rfm95-sensor-data-atmega16", key, "1h"))