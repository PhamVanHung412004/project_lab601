from init import show_plot,piechart,plt,st,pd

subject = ["Toán","Ngữ Văn","Ngoại Ngữ","Vật Lý","Hóa Học","Sinh Học","Lịch Sử","Địa lý","GDCD"]

csv_file_path = 'data_clean.csv'
st.title("Điểm thi tốt nghiệp năm 2022 trên địa bàn thành phố Hà Nội")
st.write("Lưu ý là số báo danh bắt đầu bằng 0 ví dụ số báo danh trong file csv hiển thi là 1000001 thì số báo danh thật thêm số 0 đằng trước thành 01000001.")
df = pd.read_csv(csv_file_path)

df['Số báo danh'] = df['Số báo danh'].astype(str)
df.insert(0, 'STT', range(1, len(df) + 1))

st.write("Dữ liệu từ tệp CSV:")
st.dataframe(df)

st.write("Thống kê tóm tắt:")
st.write(df.describe())

st.write("5 hàng đầu tiên:")
st.write(df.head())

# subject = ["Toán","Ngữ Văn","Ngoại Ngữ","Vật Lý","Hóa Học","Sinh Học","Lịch Sử","Địa lý","GDCD"]

st.title("Biểu đồ phân tích")

read_file1 = pd.read_csv("Thisinhdithi.csv")
show1 = show_plot(10,
                  6,
                  read_file1["Môn"],
                  read_file1["Số lượng thí sinh đi thi"],
                  "Số Lượng Thí Sinh Đi Thi Theo Môn",
                  "Tên Môn",
                  "Số lượng",
                  True)
show1.plot()

read_file2 = pd.read_csv("Thisinhkhongdithi.csv")
show2 = show_plot(10,
                  6,
                  read_file2["Môn"],
                  read_file2["Số lượng thí sinh không đi thi"],
                  "Số Lượng Thí Sinh Không Đi Thi Theo Môn",
                  "Tên Môn",
                  "Số lượng",
                  True)
show2.plot()

read_file3 = pd.read_csv("thisinhthisoluongmon.csv")
labels = [str(i) + " Môn" for i in range(len(read_file3["Nhóm"]))]

show3 = piechart(read_file3["Số lượng"],    
                ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen', 'pink', 'cyan', 'orange', 'purple', 'red'],
                 labels,
                 "Biểu đồ tròn thể hiện số lượng thí sinh thi bao nhiêu")
show3.show()

file_path = "data_clean.csv"

for i in range(len(subject)):
    st.title("Phổ điểm môn " + subject[i])
    file_path1 = 'phodiemmon' + str(subject[i]) + '.csv'
    data = pd.read_csv(file_path1)
    show22 = show_plot(10,
                  6,
                  data["Điểm"],
                  data["Tần suất"],
                  "Phổ điểm môn " + subject[i],
                  "Điểm",
                  "Tần suất",
                  False)
    show22.plot()
