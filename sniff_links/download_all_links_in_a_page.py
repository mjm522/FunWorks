import urllib
import httplib2
from urlparse import urljoin
from bs4 import BeautifulSoup, SoupStrainer




class SniffLinks():

    def __init__(self, link_to_sniff, file_types, folder_to_save=None):
        self._link_to_sniff = link_to_sniff
        self._http = httplib2.Http()
        self._file_downloader = urllib.URLopener()

        if folder_to_save is None:
            self._folder_to_save = './'
        else:
            self._folder_to_save = folder_to_save

        self._urls = []
        self._file_names = []

        self._filetypes = file_types

    def download_file(self, file_link, save_file_name):
        try:
            self._file_downloader.retrieve(file_link, self._folder_to_save+save_file_name)
        except Exception, e:
            print "Exception occured while trying to download the link ", file_link
            print "Exception:", e
        
    def sniffer(self):
        status, response = self._http.request(self._link_to_sniff)
        for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
            if link.has_attr('href'):
                src_url = link['href']
                src_url_split = src_url.split('/')
                for file_type in self._filetypes:
                    if src_url_split[-1][-len(file_type):] == file_type:
                        self.download_file(urljoin(self._link_to_sniff, link['href']), src_url_split[-1])

    def run(self):
        self.sniffer()


def main():
    link_to_sniff = 'http://www.diag.uniroma1.it/~deluca/rob2_en/material_rob2_en.html'
    save_folder = '/Users/michaelmathew/Dropbox/Books for PhD/Useful Lecture Slides/Alesandaro De Luca _Robotics/'
    file_types=['.pdf']

    snifflinks = SniffLinks(link_to_sniff, file_types, save_folder)
    snifflinks.run()



if __name__ == '__main__':
    main()









