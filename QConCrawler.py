import FileDownloader
import PageScraper

qconurl = 'https://qconlondon.com/schedule/london2019/tabular'
filepath = '/Users/cphalak/workspace/qcon/QCon/'

links = PageScraper.getLinks(qconurl)

print('Download started...')
for link in links:
    if (len(link)>0):
        FileDownloader.doDownload(link.decode("utf-8"), filepath)

print("Download of %d files completed." %len(links))
