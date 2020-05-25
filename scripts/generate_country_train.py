import requests
from tqdm import tqdm
import re

out_filename = "new_data/country.txt"

country_url = "https://gist.githubusercontent.com/kalinchernev/486393efcca01623b18d/raw/daa24c9fea66afb7d68f8d69f0c4b8eeb9406e83/countries"
res = requests.get(country_url)
country_list = res.text.split("\n")
with open(out_filename, "w") as f:
  for country_name in tqdm(country_list, desc="Processing all countries"):
    for i, word in enumerate(country_name.split()):
      if "{" in word or "}" in word:
        continue

      if i:
        f.write(f"{word} I-LOC\n")
      else:
        f.write(f"{word} B-LOC\n")
    f.write("\n")
