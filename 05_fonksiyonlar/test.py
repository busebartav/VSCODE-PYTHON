# çok çok çok önemli 
import requests
from bs4 import BeautifulSoup
url = "https://www.worldometers.info/coronavirus/?utm_campaign=homeAdvegas1?"
response = requests.get(url)
source = BeautifulSoup(response.content, "html.parser")
innerContent = source.find_all("div", attrs={"class": "maincounter-number"})
"""for i in range(len(innerContent)):
    print(innerContent[i].get_text().strip("\n"))
    print()
    print()"""

print("vaka → ", innerContent[0].get_text().strip('\n'))
print("vefat → ", innerContent[1].get_text().strip('\n'))
print("iyileşen hasta → ", innerContent[2].get_text().strip('\n'))
