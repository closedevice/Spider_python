from urllib import request


class HtmlDownloader(object):
    def downloader(self, new_url):
        if new_url is None:
            return None

        response = request.urlopen(new_url)

        if response.getcode() != 200:
            return None

        return response.read()
