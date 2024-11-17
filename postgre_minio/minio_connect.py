import pandas as pd
import numpy as np
import urllib3
import urllib.request
from io import BytesIO
from PIL import Image
from minio import Minio
from matplotlib import pyplot as plt


class MinioConnect:
    def __init__(self, bucket='a-symbol'):
        self.bucket = bucket
        self.__access_key = 'minioadmin'
        self.__secret_key = 'minioadmin'
        self.__client = Minio("localhost:9000",
                              access_key=self.__access_key,
                              secret_key=self.__secret_key, secure=False
                              )

    def print_all_bucket(self, head=10):
        """
         head: Вывод первых-head bucket-ов
        :return: Печать всех доступных bucket
        """
        buckets = self.__client.list_buckets()
        for bucket in buckets[:min(head, len(buckets))]:
            print(bucket.name, bucket.creation_date)

    def print_all_objects(self, bucket_name='b-symbol', head=10):
        objects = self.__client.list_objects(bucket_name)
        fig = plt.figure(figsize=(6, 4))
        ax = fig.add_subplot()

        for idx, obj in enumerate(objects):
            response = self.__client.get_object(bucket_name, obj._object_name)
            im = Image.open(response)
            plt.subplot(1, 3, idx + 1)
            plt.imshow(im)
