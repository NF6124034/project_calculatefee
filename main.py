import streamlit as st

def main():
    st.title("😺計費模式選擇")

    option = st.sidebar.radio("請選擇計費模式", ("學校主辦社團模式", "學校場地租借模式"))

    if option == "學校主辦社團模式":
        st.write("您選擇了學校主辦社團模式。")
        st.write("正在導向到該模式的計費頁面...")
        st.markdown("[點擊進入學校主辦社團模式計費頁面](http://192.168.65.6:8502)")

    elif option == "學校場地租借模式":
        st.write("您選擇了學校場地租借模式。")
        st.write("正在導向到該模式的計費頁面...")
        st.markdown("[點擊進入學校場地租借模式計費頁面](http://192.168.65.6:8503)")

if __name__ == "__main__":
    main()