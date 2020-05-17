from edgar import Edgar
from tqdm import tqdm
import string

out_filename = "new_data/company_train.txt"

edgar = Edgar()
all_company_names = edgar.all_companies_dict.keys()
with open(out_filename, "w") as f:
  for company_name in tqdm(all_company_names, desc="Processing all companies"):
    if len(company_name) == 0 or company_name[0] not in string.ascii_letters:
      continue
    for i, word in enumerate(company_name.split()):
      if i:
        f.write(f"{word} I-ORG\n")
      else:
        f.write(f"{word} B-ORG\n")
    f.write("\n")
