import s3fs
import os
from utils.constants import AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY


def connect_to_s3():
    try:
        s3 = s3fs.S3FileSystem(anon=False,
                               key=AWS_ACCESS_KEY_ID,
                               secret=AWS_ACCESS_KEY)
        return s3
    except Exception as e:
        print(f"S3 bağlantı hatası: {e}")
        return None


def create_bucket_if_not_exists(s3: s3fs.S3FileSystem, bucket_name: str):
    if s3 is None:
        raise ValueError("S3 bağlantısı başarısız")

    try:
        if not s3.exists(bucket_name):
            s3.mkdir(bucket_name)
            print(f"Bucket {bucket_name} created")
        else:
            print(f"Bucket {bucket_name} already exists")
    except Exception as e:
        print(f"Bucket oluşturma hatası: {e}")
        raise


def upload_to_s3(s3: s3fs.S3FileSystem, file_path: str, bucket: str, s3_file_name: str):
    if s3 is None:
        raise ValueError("S3 bağlantısı başarısız")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dosya bulunamadı: {file_path}")

    try:
        s3_path = f"{bucket}/raw/{s3_file_name}"
        s3.put(file_path, s3_path)
        print(f"Dosya başarıyla yüklendi: {s3_path}")
    except Exception as e:
        print(f"Dosya yükleme hatası: {e}")
        raise