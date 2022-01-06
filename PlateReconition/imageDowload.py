# import json
# from google_images_download import google_images_download


# def download_images():
#     google_images_downloader = google_images_download.googleimagesdownload()
#     with open("images_config.json") as config_file:
#         config_data = json.load(config_file)
#         for record in config_data["Records"]:
#             google_images_downloader.download(record)


# download_images()
from google_images_download import google_images_download

# instantiate the class
response = google_images_download.googleimagesdownload()
arguments = {"keywords": "lilly,hills", "limit": 2, "print_urls": True}
paths = response.download(arguments)
# print complete paths to the downloaded images
# print(paths)
