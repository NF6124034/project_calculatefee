import streamlit as st

def calculate_fee(total_weeks, hourly_wage, hours_per_session, book_fee, notebook_fee, equipment_fee):
    tuition_fee = total_weeks * hourly_wage * hours_per_session + book_fee + notebook_fee + equipment_fee
    return tuition_fee

def main():
    st.title("🐈學校場地租借模式的費用計算🐈‍⬛")

    # Input parameters
    st.header("💲費用參數")
    total_weeks = st.number_input("請輸入總週數", min_value=0, value=0)
    hourly_wage = st.number_input("請輸入一小時薪水", min_value=0, value=0)
    hours_per_session = st.number_input("請輸入一次幾小時", min_value=0.0, value=0.0)
    book_fee = st.number_input("請輸入課本費用", min_value=0, value=0)
    notebook_fee = st.number_input("請輸入聯絡簿費用", min_value=0, value=0)
    equipment_fee = st.number_input("請輸入器材費用", min_value=0, value=0)

    # Calculate tuition fee
    if st.button("👁️‍🗨️計算學費"):
        tuition_fee = calculate_fee(total_weeks, hourly_wage, hours_per_session, book_fee, notebook_fee, equipment_fee)
        st.subheader("學費計算結果")
        st.write(f"每位學生總學費: {tuition_fee}")

if __name__ == "__main__":
    main()