from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

search_querries = ['horse', 'lion']

def download_images(query):
    arguments = {
        'keywords' : query,
        'format' : 'jpg',
        'limit' : 300,
        'print_urls' : True,
        'size' : 'medium',
        'aspect_ratio' : 'square'
    }

    try:
        response.download(arguments)
    except FileNotFoundError:
        arguments = {
            'keywords' : query,
            'format' : 'jpg',
            'limit' : 5,
            'print_urls' : True,
            'size' : 'medium',
        }
        try:
            response.download(arguments)
        except:
            pass


for query in search_querries:
    download_images(query)
    print()