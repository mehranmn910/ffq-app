import streamlit as st
import pandas as pd

st.title("📝 تست پرسشنامه FFQ")

st.write("لطفاً بسامد مصرف مواد غذایی زیر را وارد کنید (در هفته):")

foods = ['برنج', 'نان', 'مرغ', 'ماهی', 'شیر', 'سبزیجات']
data = {}

for food in foods:
    data[food] = st.number_input(f"{food} (بار در هفته)", min_value=0, max_value=21, step=1)

if st.button("📥 ارسال و دریافت خروجی"):
    df = pd.DataFrame([data])
    df.to_excel("output.xlsx", index=False)
    st.success("پرسشنامه ثبت شد ✅")
    with open("output.xlsx", "rb") as file:
        btn = st.download_button(
            label="📄 دانلود خروجی اکسل",
            data=file,
            file_name="ffq_output.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
