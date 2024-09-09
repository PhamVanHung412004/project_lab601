import subprocess

# URL cơ bản của trang web
base_url = "https://vietnamnet.vn/giao-duc/diem-thi/tra-cuu-diem-thi-tot-nghiep-thpt/2022/"

# Danh sách số báo danh của các thí sinh
sobaodanh_list = ["01000001", "01000002", "01000003"]  # Thay thế bằng các số báo danh thực tế

tmp = "0"

for i in range(1000004,1097526):
    sobaodanh_list.append(tmp + str(i))
# Hàm tải nội dung trang web cho một số báo danh và lưu vào file HTML
ans = ".html"
def download_html(sobaodanh):
    url = f"{base_url}{sobaodanh}{ans}"
    curl_command = f'curl -s {url} -o {sobaodanh}.html'
    try:
        subprocess.run(curl_command, shell=True, check=True)
        print(f"Đã tải nội dung trang web và lưu vào {sobaodanh}.html")
    except subprocess.CalledProcessError as e:
        print(f"Lỗi khi tải nội dung trang web cho số báo danh {sobaodanh}: {e}")

# Tải nội dung trang web cho tất cả các thí sinh
for sobaodanh in sobaodanh_list:
    download_html(sobaodanh)
