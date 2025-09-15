# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

import threading
from collections import deque
from concurrent.futures import ThreadPoolExecutor
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def get_hostname(url):
            return url.split('/')[2]
        
        lock = threading.Lock()
        start_hostname = get_hostname(startUrl)
        visited = set([startUrl])
        q = deque([startUrl])

        def crawl_urls(url):
            new_urls = []
            for nextUrl in htmlParser.getUrls(url):
                with lock:
                    if get_hostname(nextUrl) == start_hostname and nextUrl not in visited:
                        visited.add(nextUrl)
                        new_urls.append(nextUrl)
            return new_urls

        with ThreadPoolExecutor(max_workers = 10) as executor:
            while q:
                futures = {executor.submit(crawl_urls, q.popleft()) for _ in range(len(q))}
                for future in futures:
                    q.extend(future.result())

 
        return list(visited)
        