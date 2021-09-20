from requests_html  import HTMLSession


session = HTMLSession()
url = "https://www.mendoza.gov.ar/prensa/comunicados/"

r = session.get(url)
articles = r.html.find('article')

sets = {'link'}
for item in articles:
	newsitem = item.find('a',first=True)
	title = newsitem.text
	links = newsitem.absolute_links
	sets = sets.union(links)

print(list(lista))

