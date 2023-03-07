def get_yd(yd_link: str) -> '.csv':
    
    """Self-made function for getting data from Yandex.Disk. Returns data in csv format."""
    
    # libraries
    import requests
    from io import BytesIO
    from urllib.parse import urlencode
    
    # the basic url unifed for everything
    base_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?'

    # Build the download link
    final_url = (base_url + urlencode(dict(public_key=yd_link)))

    # Return a download link json encoded
    response = requests.get(final_url)

    # We need to take the 'href' key to get a link to data
    download_url = response.json()['href'] # returns the json-encoded content of a response

    # loads the file
    download_response = requests.get(download_url)
    
    return BytesIO(download_response.content)
