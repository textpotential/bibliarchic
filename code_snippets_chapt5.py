

GET /verses/{version_id}:{book_id}.{chapter_number}.{verse_number}.js?include_marginalia=true

GET https://bibles.org/v2/verses/eng-ESV:2Cor.3.6.js?include_marginalia=true

GET https://bibles.org/v2/verses.js?keyword=book

verse object keys = ['footnotes', 'reference', 'label', 'auditid', 
					 'prev_osis_id', 'copyright', 'verse', 'id', 
					 'previous', 'lastverse', 'parent', 'crossreferences', 
					 'text', 'next', 'next_osis_id', 'osis_end']

'text':  <p class="p"><sup id="2Cor.3.6" class="v">6</sup>who has made us 
         sufficient to be <a href="#2Cor.3.6!x.1" id="link_2Cor.3.6!x.1" 
         class="notelink x-link"><span>+</span></a> ministers of <a 
         href="#2Cor.3.6!x.2" id="link_2Cor.3.6!x.2" class="notelink 
         x-link"><span>+</span></a> a new covenant, not of <a 
         href="#2Cor.3.6!x.3" id="link_2Cor.3.6!x.3" class="notelink 
         x-link"><span>+</span></a> the letter but of the Spirit.
         For the 
         letter kills, but <a href="#2Cor.3.6!x.4" id="link_2Cor.3.6!x.4" 
         class="notelink x-link"><span>+</span></a> the Spirit gives 
         life.</p>

import requests
from pprint import pprint

api_token = [my_personal_API_token]
pass_fake = 'X'

verse_endpoint = 'https://bibles.org/v2/verses.js?keyword=book'
verse_resp = requests.get(verse_endpoint, auth=(api_token, pass_fake))
verses = verse_resp.json()

pprint(verses)

'summary': {'query':    'book',
                        'rpp':          '15',
                        'sort':         'relevance',
                        'start':        1,
                        'testaments':   ['OT', 'NT'],
                        'total':        318,
                        'versions':     ['eng-NASB', 'eng-ESV', 'eng-MSG',
                                         'eng-KJVA', 'eng-CEVD', 'eng-AMP',
                                         'eng-GNTD', 'eng-CEV']
			}

# get just the list of verse objects from the API response
search_verses = verses['response']['search']['result']['verses']
book_bible = [] # define an empty list

for verse in search_verses: # look through all 318 verses returned
    book_bible.append(verse['text']) # add the text of each verse to the list

print(' '.join(book_bible)) # print all items of the list joined by a space

