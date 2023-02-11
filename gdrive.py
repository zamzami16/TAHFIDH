from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import pandas as pd

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

# Link folders
# https://drive.google.com/drive/folders/1ajMjzdBsMjrKAlydsh77mXErGQRHU7PH?usp=share_link

#
# Contoh link files
# https://docs.google.com/presentation/d/1PG2s7o7AO7_MLcJWBSBJ3pKHhHTJ2PlNM1mBVdi7FZs/edit?usp=share_link
# link download
# https://drive.google.com/uc?export=download&id=1PG2s7o7AO7_MLcJWBSBJ3pKHhHTJ2PlNM1mBVdi7FZs

file_list = drive.ListFile(
    {"q": "'1ajMjzdBsMjrKAlydsh77mXErGQRHU7PH' in parents and trashed=false"}
).GetList()

no = []
nama = []
sekolah = []
links = []
i = 1
for file1 in file_list:
    print("title: %s, id: %s" % (file1["title"], file1["id"]))
    file_ = file1["title"].split("__")
    no.append(file_[0])
    nama.append(file_[1])
    sekolah.append(file_[2].replace(".pdf", ""))
    links.append(
        f"https://drive.google.com/uc?export=download&id={file1['id']}"
    )
    i += 1

df = pd.DataFrame({"No": no, "Nama": nama, "Sekolah": sekolah, "Links": links})
df.to_excel("list_files.xlsx", index=False)
