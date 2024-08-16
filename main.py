import requests
from bs4 import BeautifulSoup
import lxml
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

website = response.text
soup = BeautifulSoup(website, "lxml")
name = soup.find_all(name="h3",class_="title")
title_name = [i.getText() for i in name]
movies = title_name[::-1]
with open("movie.txt", mode="w", encoding="utf8") as file:
    for i in movies:
        file.write(f"{i}\n")




