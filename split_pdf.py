from PyPDF2 import PdfWriter, PdfReader
import pandas as pd
import time
import emoji


def run(inputpdf, inputNames, jenjang="SD"):
    print(f"preparing file(s) {jenjang}...")

    print(f"Check total row of file(s) {jenjang}...")
    if len(inputpdf.pages) == len(inputNames):
        print("File(s) is good...")
        print("Processing files ...")
        time.sleep(3)
        print("Splitting pdf file(s)...")
        print("")
        for i in range(len(inputpdf.pages)):
            output = PdfWriter()
            output.add_page(inputpdf.pages[i])
            with open(
                r"outputs/{0}__{1}__{2}__{3}.pdf".format(
                    inputNames.iloc[i][0],
                    inputNames.iloc[i][1],
                    inputNames.iloc[i][2],
                    jenjang,
                ),
                "wb",
            ) as outputStream:
                output.write(outputStream)
                print(
                    "{0} --> Create file: outputs/{0}-{1}-{2}.pdf".format(
                        inputNames.iloc[i][0], inputNames.iloc[i, 1], jenjang
                    )
                )
    else:
        print("Jumlah row dari file excel dan jumlah halamn pdf berbeda.")
        print("")
        print("")
        x = input("Created with \u2764 by mohyusufz. Press any key to quit..")


def main():
    print("Notes:")
    print("\t* Pastikan file sudah benar.!")
    print("\t* Pastikan jumlah file pdf dan excel punya jumlah data yang sama!")
    print("\t Pastikan Nama file berupa huruf kecil.")
    print('\t Pastikan Nama File "names__sd.xlsx" untuk files excel SD.')
    print('\t Pastikan Nama File "names__tk.xlsx" untuk files excel TK.')
    print('\t Pastikan Nama File "documents__sd.pdf" untuk files PDF SD.')
    print('\t Pastikan Nama File "documents__tk.pdf" untuk files PDF TK.')
    print("")
    x = input("Ingin melanjutkan? [Y]/n: ")
    if x == "" or x == "Y" or x == "y":
        _d = ["sd", "tk"]
        for d_ in _d:
            try:
                inputpdf = PdfReader(open(f"inputs/documents__{d_}.pdf", "rb"))
                inputNames = pd.read_excel(f"inputs/names__{d_}.xlsx")
                run(
                    inputpdf=inputpdf, inputNames=inputNames, jenjang=d_.upper()
                )
            except:
                print(
                    "Maaf, terjadi kesalahan. Silakan periksa dan ulangi lagi.."
                )
                break
        print("Selesai...")
        print("")
        print("")
        x = input(
            emoji.emojize("Created with :red_heart: ", variant="emoji_type")
            + "  by mohyusufz. \nPress any key to quit.."
        )
    else:
        print("Membatalkan...")
        _ = input("Tekan sembarang tombol untuk keluar.")


if __name__ == "__main__":
    main()
