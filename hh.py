from bs4 import BeautifulSoup
import requests
import pprint

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/539.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 OPR/82.0.4227.33"
}
url = "https://hh.ru/vacancies/analitik"
response = requests.get(url, headers=header)
soup = BeautifulSoup(response.text, 'lxml')
vacancy_header = soup.find_all(class_="vacancy-serp-item__row vacancy-serp-item__row_header")
results = []

for i in vacancy_header:
    text = i.a.get_text()
    lnk = i.a.get('href')
    zp = i.find(attrs={"data-qa": "vacancy-serp__vacancy-compensation"})
    if (zp == None):
        zp = "Not defined"
    else:
        zp = zp.text.replace('\u202f', '')

    total = text + " | " + zp + " | " + lnk
    results.append(total)

pp = pprint.PrettyPrinter(indent=0)
pp.pprint(results)

# print(vacancy_header)

# <div class="vacancy-serp-item__row vacancy-serp-item__row_header">
#     <div class="vacancy-serp-item__info">
#         <span data-qa="bloko-header-3"
#               class="bloko-header-section-3 bloko-header-section-3_lite">
#             <span class="resume-search-item__name">
#                 <span class="g-user-content">
#                     <a class="bloko-link"
#                        data-qa="vacancy-serp__vacancy-title"
#                        target="_blank"
#                        href="https://hh.ru/vacancy/49881796?query=%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D1%82%D0%B8%D0%BA&amp;hhtmFrom=vacancy_search_catalog">
#                         Аналитик направления цифрового маркетинга (BI\SQL\Python)
#                     </a>
#                 </span>
#             </span>
#         </span>
#     </div>
#     <div class="vacancy-serp-item__sidebar">
#         <span data-qa="vacancy-serp__vacancy-compensation"
#               class="bloko-header-section-3 bloko-header-section-3_lite">
#             170000 – 210000
#             <!-- -->руб.
#         </span>
#     </div>
# </div>


