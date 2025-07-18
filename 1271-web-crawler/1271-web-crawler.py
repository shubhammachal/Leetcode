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

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        #get hostname
        def get_hostname(url):
            return url.split('/')[2]
        
        start_hostname = get_hostname(startUrl)
        visited = set()

        def dfs(url, htmlParser):
            visited.add(url)
            for next_url in htmlParser.getUrls(url):
                if get_hostname(next_url) == start_hostname and next_url not in visited:
                    dfs(next_url , htmlParser)
        dfs(startUrl, htmlParser)
        return visited
