import streamlit as st
import pandas as pd

df = pd.read_excel("list_files.xlsx")

maindfsd = df[df["jenjang"].str.upper() == "SD"]
maindftk = df[df["jenjang"].str.upper() == "TK"]

data = {"sd": maindfsd, "tk": maindftk}

st.set_page_config(
    layout="wide",
    page_title="Sertifikat Lomba Tahfidz",
    menu_items={
        "About": "https://github.com/zamzami16",
        "Report a bug": "https://api.whatsapp.com/send/?phone=6285161400863&text=Hi,"
        + " Your Bagi sertifikat Tahfidz app have a bug. Please help me.&type=phone_number&app_absent=0",
    },
)

btnCari = False
cari = ""
nama = ""
sekolah = ""

maindf = data["sd"]


def make_clickable(link):
    return f'<a target="_blank" href="{link}">Download</a>'


def WriteData(df):
    if len(df) > 0:
        with st.container():
            df = df.to_html(escape=False, justify="center", index=False)
            set_column_widht = """
                        <style>
                            thead tr th {width: 50%; min-widht: 40%}
                            thead tr th:first-child {width: 25px}
                            thead tr th:last-child {width: 25px}
                        </style>
                        """
            # Inject CSS with Markdown
            st.markdown(set_column_widht, unsafe_allow_html=True)
            st.write(df, unsafe_allow_html=True)
    else:
        st.write("Data Tidak ditemukan")


def FilterData():
    dff = maindf.sort_values(by=["No"]).copy()
    # df = dff[dff["Nama"].str.contains(f"{text}", case=False, na=False)]
    df = dff[
        dff["Nama"].str.upper().str.contains(f"{nama}".upper())
        & dff["Sekolah"].str.upper().str.contains(f"{sekolah}".upper())
    ]
    # link is the column with hyperlinks
    df["Links"] = df["Links"].apply(make_clickable)
    WriteData(df)


with st.container():
    st.title("Sertifikat Lomba Tahfidz LBB PEC")
    _semua = st.checkbox(
        "Lihat semua Data",
        help='Menampilkan Semua Data "Termasuk SD dan TK"',
        value=True,
    )
    _tk = st.checkbox(
        "**Lihat Data TK**",
        value=False,
        help="Menampilkan data TK, jika tidak dicentang akan menampilkan data SD",
    )
    if _semua:
        st.write("### **Menampilkan Semua Data**")
        maindf = df
    else:
        if _tk:
            st.write("### **Menampilkan Data TK**")
            maindf = data["tk"]
        else:
            st.write("### **Menampilkan Data SD**")
            maindf = data["sd"]

    nama = st.text_input("Cari Nama || Tekan Enter untuk memfilter", "")
    sekolah = st.text_input("Cari Sekolah || Tekan Enter untuk memfilter", "")
    btnCari = st.button("Cari", on_click=FilterData())

    st.markdown(
        """<div style="text-align: center"> Created with &#128153; by Zami16 </div>""",
        unsafe_allow_html=True,
    )
