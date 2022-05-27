from myparse import parser as prs

class parser(prs):
    
    def getalltexts(self, url, tag, myclass, domain = '', start = None, end = None):
        texts = []
        links = self.getlinks(url, tag, myclass, domain)
        for link in links.values():
            print('Скачиваю текст отсюда: ' + link)
            text = self.gettext(link, start , end)
            texts.append(text)
        return texts












    
            
