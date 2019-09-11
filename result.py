import numpy as np
import pandas as pd

url_obstable = 'https://raw.githubusercontent.com/berkaycit/obs-result/master/obstable.csv?token=AEKDQ3VEFN45N6SQ5SSJ2D25QI2QE'

obs = pd.read_csv(url_obstable)
obs.head()

zScores = 0
sScores = 0
freeElective = 0
commonRequired = 0
totalCredit = 0

youHaveToTake = list()

df = pd.DataFrame(obs)

for index, row in df.iterrows():
  passState = row["Harf"] != "FF" and row["Harf"] != "FD"
  if(passState):
    totalCredit += row["Kredi"]
  elif(not passState and row["Z"] == "Z"):
    youHaveToTake.append(row["Ad"])

  if(passState and row['Z'] == "Z" and row["Kod"][:4] == "CENG"):
    zScores += row["Kredi"]
  elif(passState and row["Kod"][:4] == "CENG"):
    sScores += row["Kredi"]
  elif(passState and row["Kod"][:4] != "CENG" and row['Z'] == "S"):
    freeElective += row["Kredi"]
  elif(passState and row["Kod"][:4] != "CENG" and row['Z'] == "Z"):
    commonRequired += row["Kredi"]

colorZ = '\033[1;32;47m' if zScores >= 92 else '\033[1;31;47m'
colorS = '\033[1;32;47m' if sScores >= 60 else '\033[1;31;47m'
colorFree = '\033[1;32;47m' if freeElective >= 9 else '\033[1;31;47m'
colorCommon = '\033[1;32;47m' if commonRequired >= 56 else '\033[1;31;47m'
colorTotal = '\033[1;32;47m' if totalCredit >= 240 else '\033[1;31;47m'

print(colorZ,"Completed Credits of CENG Required (Z) Courses: ", zScores, " out of 92")
print(colorS,"Completed Credits of CENG Elective (S) Courses:  ", sScores, " out of 60")
print(colorFree, "Completed Credits of Courses taken as Free Elective : ", freeElective, " out of 9")
print(colorCommon, "Completed credits of Common Required(Z) Courses: ", commonRequired, " out of 56")
print(colorTotal, "Total Completed Credits: ", totalCredit, " out of 240")
