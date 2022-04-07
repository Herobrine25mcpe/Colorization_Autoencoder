from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()
arguments = {"keywords":"liquid abstract","limit":100, "print_urls":False, "format":"jpg"}

paths = response.download(arguments)

print(paths)