from minio import Minio
from minio.error import S3Error


def main():
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    client = Minio(
        "minio.neubie.co.kr",
        access_key="1cB1u38t777BVtaz",
        secret_key="ov1gM1wxLWqQWy8FrGpP9F78KYpVlHSH",
    )

    # Make 'asiatrip' bucket if not exist.
    found = client.bucket_exists("test")
    if not found:
        client.make_bucket("test")
    else:
        print("Bucket 'test' already exists")

    # Upload '/home/user/Photos/asiaphotos.zip' as object name
    # 'asiaphotos-2015.zip' to bucket 'asiatrip'.
    client.fput_object(
        "test", "230414/test_file_obj", "/home/hcy/test_ws/EX.tutorial/minio/test_file",
    )
    print(
        "'/home/user/Photos/asiaphotos.zip' is successfully uploaded as "
        "object 'asiaphotos-2015.zip' to bucket 'asiatrip'."
    )


if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)