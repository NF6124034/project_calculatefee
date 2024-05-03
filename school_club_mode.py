import streamlit as st

def calculate_fee(hourly_rate, num_sessions, num_weeks_1, admin_fee, num_students):
    try:
        tuition_fee = (hourly_rate * num_sessions * num_weeks_1) / admin_fee / num_students
        return tuition_fee
    except ZeroDivisionError:
        return 0

def calculate_material_fee(book_fee, notebook_fee, admin_fee_per_session, num_sessions,num_weeks_2, equipment_fee):
    try:
        material_fee = (book_fee + notebook_fee + (admin_fee_per_session * num_sessions * num_weeks_2) + equipment_fee)
        return material_fee
    except ZeroDivisionError:
        return 0

def main():
    

    st.title("🐈學校主辦社團模式的費用計算🐈‍⬛")
    
    # Input parameters for tuition fee
    st.header("💲學費計算")
    hourly_rate = st.number_input("請輸入教師鐘點費", min_value=0, value=0)
    num_hours = st.number_input("請輸入每週課程節數", min_value=0, value=0)
    num_weeks_1 = st.number_input("請輸入課程週數", min_value=0, value=0)
    admin_fee = st.number_input("請輸入管理授權(%)", min_value=0.0, value=0.0)
    num_students = st.number_input("請輸入每班人數", min_value=0, value=0)

    # Input parameters for material fee
    st.header("📖學習教材費計算")
    book_fee = st.number_input("請輸入課本費用", min_value=0, value=0)
    notebook_fee = st.number_input("請輸入聯絡簿費用", min_value=0, value=0)
    admin_fee_per_session = st.number_input("請輸入每節管理費", min_value=0, value=0)
    num_sessions = st.number_input("請輸入一週課程節數", min_value=0, value=0)
    num_weeks_2 = st.number_input("請輸入總週數", min_value=0, value=0)
    equipment_fee = st.number_input("請輸入器材設備費", min_value=0, value=0)


    if st.button("👁️‍🗨️計算總費用"):
            # Calculate fees
            tuition_fee = calculate_fee(hourly_rate, num_hours, num_weeks_1, admin_fee, num_students)
            material_fee = calculate_material_fee(book_fee, notebook_fee, admin_fee_per_session, num_sessions,num_weeks_2, equipment_fee)

            # Display total fee
            total_fee = tuition_fee + material_fee
            st.subheader("總費用")
            st.write(f"學費: {tuition_fee}")
            st.write(f"學習教材費: {material_fee}")
            st.write(f"總費用: {total_fee}")

if __name__ == "__main__":
    main()
    
