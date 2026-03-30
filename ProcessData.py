#ProcessData.py
#Name: Afrah Mohamoud
#Date: 03/27/2026
#Assignment: Lab 8 

def build_user_id(first_name, last_name, student_id):
  """Return first initial + last name (+x if short) + last 3 digits of ID."""
  last_part = last_name.lower()
  if len(last_part) < 5:
    last_part += "x"
  id_suffix = student_id[-3:]
  return first_name[0].lower() + last_part + id_suffix


def build_major_year(major, year):
  """Return the Major-Year value (e.g., MUS-JR)."""
  year_map = {
    "Freshman": "FR",
    "Sophomore": "SO",
    "Junior": "JR",
    "Senior": "SR",
  }
  major_letters = "".join(ch for ch in major if ch.isalpha())
  major_code = major_letters[:3].upper()
  year_code = year_map.get(year, year[:2].upper())
  return major_code + "-" + year_code


def main():
  # Open input/output files and transform each student record.
  record_count = 0
  with open("names.dat", "r") as in_file, open("StudentList.csv", "w") as out_file:
    for line in in_file:
      line = line.strip()
      if not line:
        continue

      fields = line.split()
      first_name = fields[0]
      last_name = fields[1]
      student_id = fields[3].replace("-", "")
      year = fields[5]
      major = " ".join(fields[6:])

      user_id = build_user_id(first_name, last_name, student_id)
      major_year = build_major_year(major, year)

      # Required output order: Last Name, First Name, UserID, Major-Year
      out_file.write(last_name + "," + first_name + "," + user_id + "," + major_year + "\n")
      record_count += 1

  print("Done. Wrote " + str(record_count) + " records to StudentList.csv")

if __name__ == '__main__':
  main()
