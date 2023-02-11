import streamlit as st
import pandas as pd


maindf = pd.read_excel("list_files.xlsx")
st.set_page_config(layout="wide")

btnCari = False
cari = ""


def make_clickable(link):
    return f'<a target="_blank" href="{link}">Download</a>'


def WriteData(df):
    if len(df) > 0:
        with st.container():
            # CSS to inject contained in a string
            hide_table_row_index = """
                        <style>
                            thead tr {text-align: center}
                            thead tr th:first-child {display:none}
                            tbody th {display:none}
                        </style>
                        """
            # Inject CSS with Markdown
            st.markdown(hide_table_row_index, unsafe_allow_html=True)
            st.write(df, unsafe_allow_html=True)
    else:
        st.write("Data Tidak ditemukan")


def FilterData(tnama: str = "", tsekolah: str = ""):
    dff = maindf.sort_values(by=["No"]).copy()
    # df = dff[dff["Nama"].str.contains(f"{text}", case=False, na=False)]
    df = dff[
        dff["Nama"].str.contains(f"{tnama}")
        & dff["Sekolah"].str.contains(f"{tsekolah}")
    ]
    # link is the column with hyperlinks
    df["Links"] = df["Links"].apply(make_clickable)
    df = df.to_html(escape=False, justify="center")
    WriteData(df)


with st.container():
    st.write("# Sertifikat Lomba Tahfidz LBB PEC")
    nama = st.text_input("Cari Nama || Tekan Enter untuk memfilter", "")
    sekolah = st.text_input("Cari Sekolah || Tekan Enter untuk memfilter", "")
    btnCari = st.button("Cari", on_click=FilterData(nama, sekolah))

    st.markdown(
        """<div style="text-align: center"> Created with &#128153; by Zami16 </div>""",
        unsafe_allow_html=True,
    )
