from PyPDF2 import PdfWriter, PdfReader
import pandas as pd
import time
import emoji


def run():
    print("preparing file(s)...")
    inputpdf = PdfReader(open("inputs/documents.pdf", "rb"))
    inputNames = pd.read_excel("inputs/names.xlsx")

    print("Check total row of file(s)...")
    if len(inputpdf.pages) == len(inputNames):
        print("FIle(s) is good...")
        print("Processing files ...")
        time.sleep(3)
        print("Splitting pdf file(s)...")
        print("")
        for i in range(len(inputpdf.pages)):
            output = PdfWriter()
            output.add_page(inputpdf.pages[i])
            with open(
                r"outputs/{0}__{1}__{2}.pdf".format(
                    inputNames.iloc[i][0],
                    inputNames.iloc[i][1],
                    inputNames.iloc[i][2],
                ),
                "wb",
            ) as outputStream:
                output.write(outputStream)
                print(
                    "{0} --> Create file: outputs/{0}-{1}.pdf".format(
                        inputNames.iloc[i][0], inputNames.iloc[i, 1]
                    )
                )
        print("Selesai...")
        print("")
        print("")
        x = input(
            emoji.emojize("Created with :red_heart: ", variant="emoji_type")
            + "  by mohyusufz. \nPress any key to quit.."
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
    print("")
    x = input("Ingin melanjutkan? [Y]/n: ")
    if x == "" or x == "Y" or x == "y":
        run()


if __name__ == "__main__":
    main()
