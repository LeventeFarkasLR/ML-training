import pandas as pd
from shutil import copyfile

# xl = pd.ExcelFile("train_labels.xlsx")
# print(xl.sheet_names)
# df = xl.parse("train_labels.csv")
#
# def copy(src, dst):
#     copyfile(src, dst)
#
#
# for index, row in df.iterrows():
#     print(row)
#     if row["isHappy"] == 1:
#         print("HAPPY!!")
#         copy("trainData/" + str(row["ID"]) + ".png", "trainData/happy/" + str(row["ID"]) + ".png")
#     if row["isHappy"] == 0:
#         print("SAD!!!")
#         copy("trainData/" + str(row["ID"]) + ".png", "trainData/sad/" + str(row["ID"]) + ".png")
#

xl = pd.ExcelFile("beHappy.xlsx")
print(xl.sheet_names)
df = xl.parse("beHappy.csv")

def copy(src, dst):
    copyfile(src, dst)


for index, row in df.iterrows():
    print(row)
    if row["isHappy"] == 1:
        print("HAPPY!!")
        copy("testData/" + str(row["ID"]) + ".png", "testData/happy/" + str(row["ID"]) + ".png")
    if row["isHappy"] == 0:
        print("SAD!!!")
        copy("testData/" + str(row["ID"]) + ".png", "testData/sad/" + str(row["ID"]) + ".png")



if __name__ == '__main__':
    pass
