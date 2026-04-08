import os

import boto3
from botocore.config import Config

from src.constants import (
    AWS_ACCESS_KEY_ID_ENV_KEY,
    AWS_DEFAULT_REGION_ENV_KEY,
    AWS_REGION_ENV_KEY,
    AWS_SECRET_ACCESS_KEY_ENV_KEY,
    AWS_SESSION_TOKEN_ENV_KEY,
    REGION_NAME,
)


class S3Client:

    s3_client=None
    s3_resource = None
    def __init__(self, region_name=REGION_NAME):
        """ 
        This Class gets aws credentials from env_variable and creates an connection with s3 bucket 
        and raise exception when environment variable is not set
        """

        if S3Client.s3_resource==None or S3Client.s3_client==None:
            __access_key_id = os.getenv(AWS_ACCESS_KEY_ID_ENV_KEY, "").strip()
            __secret_access_key = os.getenv(AWS_SECRET_ACCESS_KEY_ENV_KEY, "").strip()
            __session_token = os.getenv(AWS_SESSION_TOKEN_ENV_KEY, "").strip() or None
            __resolved_region = (
                os.getenv(AWS_REGION_ENV_KEY, "").strip()
                or os.getenv(AWS_DEFAULT_REGION_ENV_KEY, "").strip()
                or region_name
            )

            if not __access_key_id:
                raise Exception(
                    f"Environment variable {AWS_ACCESS_KEY_ID_ENV_KEY} is not set in the process running the pipeline."
                )
            if not __secret_access_key:
                raise Exception(
                    f"Environment variable {AWS_SECRET_ACCESS_KEY_ENV_KEY} is not set in the process running the pipeline."
                )
            if not __resolved_region:
                raise Exception(
                    f"AWS region is not configured. Set {AWS_REGION_ENV_KEY} or {AWS_DEFAULT_REGION_ENV_KEY}."
                )

            session = boto3.session.Session(
                aws_access_key_id=__access_key_id,
                aws_secret_access_key=__secret_access_key,
                aws_session_token=__session_token,
                region_name=__resolved_region,
            )
            s3_config = Config(signature_version="s3v4")

            S3Client.s3_resource = session.resource("s3", config=s3_config)
            S3Client.s3_client = session.client("s3", config=s3_config)
        self.s3_resource = S3Client.s3_resource
        self.s3_client = S3Client.s3_client
