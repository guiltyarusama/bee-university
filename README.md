# bee-university

Project thu thập điểm chuẩn đại học 2014 - 2018 và phân tích dữ liệu

> Project Open Source provide by BeeCost.Com

# Development
```markdown

#install python 

#install python 3.7


mkdir -p /bee_university

git clone https://github.com/tuantmtb/bee-university.git
git config credential.helper store
 
cd bee-university
virtualenv venv -p python3.7
source venv/bin/activate
pip install -r requirements.txt

# Update folder path in init.py
python init.py

# Crawl danh sách url trường đại học
python crawler/crawler_university_list.py
# Crawl điểm chuẩn từ 2014 - 2018
python crawler/crawl_diemchuan.py
```

# Output

> Output: /bee_university/crawler/common/university.gz

Download: [university.gz](https://github.com/beecost/bee-university/blob/master/output_data/crawler/common/university.gz) 

> Output: /bee_university/crawler/common/university_diemchuan.gz

Download: [university_diemchuan.gz](https://github.com/beecost/bee-university/blob/master/output_data/crawler/common/university_diemchuan.gz) 


# Format data

Dữ liệu Format .GZ (jsonl - Mỗi dòng là 1 bản ghi)

## University
 
File: `university.gz`

 ```javascript
{"url": "https://diemthi.tuyensinh247.com/diem-chuan/hoc-vien-cong-nghe-buu-chinh-vien-thong-phia-bac-BVH.html", "university_code": "BVH", "university_name": "Học Viện Công Nghệ Bưu Chính Viễn Thông ( 
Phía Bắc )"}
{"url": "https://diemthi.tuyensinh247.com/diem-chuan/hoc-vien-cong-nghe-buu-chinh-vien-thong-phia-nam-BVS.html", "university_code": "BVS", "university_name": "Học Viện Công Nghệ Bưu Chính Viễn Thông (p
hía Nam)"}
{"url": "https://diemthi.tuyensinh247.com/diem-chuan/dai-hoc-cong-nghiep-det-may-ha-noi-CCM.html", "university_code": "CCM", "university_name": "Đại Học Công Nghiệp Dệt May Hà Nội"}
{"url": "https://diemthi.tuyensinh247.com/diem-chuan/dai-hoc-kinh-te-nghe-an-CEA.html", "university_code": "CEA", "university_name": "Đại học Kinh Tế Nghệ An"}
{"url": "https://diemthi.tuyensinh247.com/diem-chuan/hoc-vien-canh-sat-nhan-dan-CSH.html", "university_code": "CSH", "university_name": "Học Viện Cảnh Sát Nhân Dân"}
```

## University điểm chuẩn 2014 - 2019
File: `university_diemchuan.gz`

```javascript
{"diemchuan_datas": [{"major_code": "CN1", "major_name": "Công nghệ Thông tin", "subject_group": "A00; A01; D07", "point": "23.75", "note": "", "year": 2018}, {"major_code": "CN2", "major_name": "Máy tính và Robot", "subject_group": "A00; A01; D07", "point": "21", "note": "", "year": 2018}, {"major_code": "CN3", "major_name": "Vật lý kỹ thuật", "subject_group": "A00; A01; D07", "point": "18.75", "note": "", "year": 2018}, {"major_code": "CN4", "major_name": "Cơ kỹ thuật", "subject_group": "A00; A01; D07", "point": "20.5", "note": "", "year": 2018}, {"major_code": "CN5", "major_name": "Công nghệ kỹ thuật xây dựng", "subject_group": "A00; A01; D07", "point": "18", "note": "", "year": 2018}, {"major_code": "CN6", "major_name": "Công nghệ kỹ thuật cơ điện tử", "subject_group": "A00; A01; D07", "point": "22", "note": "", "year": 2018}, {"major_code": "CN7", "major_name": "Công nghệ Hàng không vũ trụ", "subject_group": "A00; A01; D07", "point": "19", "note": "", "year": 2018}, {"major_code": "CN8", "major_name": "Khoa học máy tính", "subject_group": "A00; A01; D07", "point": "22", "note": "", "year": 2018}, {"major_code": "CN9", "major_name": "Công nghệ kỹ thuật điện tử - viễn thông", "subject_group": "A00; A01; D07", "point": "20", "note": "", "year": 2018}, {"major_code": "CN1", "major_name": "Công nghệ Thông tin", "subject_group": "A00; A01; D07", "point": "26", "note": "", "year": 2017}, {"major_code": "CN2", "major_name": "Máy tính và Robot", "subject_group": "A00; A01; D07", "point": "---", "note": "", "year": 2017}, {"major_code": "CN3", "major_name": "Vật lý kỹ thuật", "subject_group": "A00; A01; D07", "point": "19", "note": "", "year": 2017}, {"major_code": "CN4", "major_name": "Cơ kỹ thuật", "subject_group": "A00; A01; D07", "point": "23.5", "note": "", "year": 2017}, {"major_code": "CN5", "major_name": "Công nghệ kỹ thuật xây dựng", "subject_group": "A00; A01; D07", "point": "23.5", "note": "", "year": 2017}, {"major_code": "CN6", "major_name": "Công nghệ kỹ thuật cơ điện tử", "subject_group": "A00; A01; D07", "point": "23.5", "note": "", "year": 2017}, {"major_code": "CN7", "major_name": "Công nghệ Hàng không vũ trụ", "subject_group": "A00; A01; D07", "point": "---", "note": "", "year": 2017}, {"major_code": "CN8", "major_name": "Khoa học máy tính", "subject_group": "A00; A01; D07", "point": "26", "note": "", "year": 2017}, {"major_code": "CN9", "major_name": "Công nghệ kỹ thuật điện tử - viễn thông", "subject_group": "A00; A01; D07", "point": "26", "note": "", "year": 2017}, {"major_code": "QHITD2", "major_name": "Công nghệ kỹ thuật Xây dựng-Giao thông", "subject_group": "A00; A02", "point": "---", "note": "", "year": 2016}, {"major_code": "QHITD1", "major_name": "Kỹ thuật năng lượng", "subject_group": "A00; A02", "point": "81", "note": "", "year": 2016}, {"major_code": "7520401", "major_name": "Vật lý kỹ thuật", "subject_group": "A00; A02", "point": "87", "note": "", "year": 2016}, {"major_code": "7520214", "major_name": "Kỹ thuật máy tính", "subject_group": "A00; A02", "point": "---", "note": "", "year": 2016}, {"major_code": "7520101", "major_name": "Cơ kỹ thuật", "subject_group": "A00; A02", "point": "87", "note": "", "year": 2016}, {"major_code": "7510302CLC", "major_name": "Công nghệ kỹ thuật điện tử, truyền thông (CLC)", "subject_group": "A01; D07; D08", "point": "125", "note": "", "year": 2016}, {"major_code": "7510302", "major_name": "Công nghệ kỹ thuật điện tử, truyền thông", "subject_group": "A00; A02", "point": "95", "note": "", "year": 2016}, {"major_code": "7510203", "major_name": "Công nghệ kỹ thuật cơ điện tử", "subject_group": "A00; A02", "point": "94", "note": "", "year": 2016}, {"major_code": "7480201NB", "major_name": "Công nghệ Thông tin định hướng thị trường Nhật Bản", "subject_group": "A00; A02", "point": "---", "note": "", "year": 2016}, {"major_code": "7480201", "major_name": "Công nghệ thông tin", "subject_group": "A00; A02", "point": "103", "note": "", "year": 2016}, {"major_code": "7480104", "major_name": "Hệ thống thông tin", "subject_group": "A00; A02", "point": "98", "note": "", "year": 2016}, {"major_code": "7480102", "major_name": "Truyền thông và mạng máy tính", "subject_group": "A00; A02", "point": "98", "note": "", "year": 2016}, {"major_code": "7480101CLC", "major_name": "Khoa học Máy tính (CLC)", "subject_group": "A01; D07; D08", "point": "125", "note": "", "year": 2016}, {"major_code": "7480101", "major_name": "Khoa học máy tính", "subject_group": "A00; A02", "point": "98", "note": "", "year": 2016}, {"major_code": "7480201", "major_name": "Công nghệ thông tin", "subject_group": "", "point": "109", "note": "", "year": 2015}, {"major_code": "7480101", "major_name": "Khoa học máy tính", "subject_group": "", "point": "106.5", "note": "", "year": 2015}, {"major_code": "7480104", "major_name": "Hệ thống thông tin", "subject_group": "", "point": "106.5", "note": "", "year": 2015}, {"major_code": "7480102", "major_name": "Truyền thông và mạng máy tính", "subject_group": "", "point": "106.5", "note": "", "year": 2015}, {"major_code": "7510302", "major_name": "Công nghệ kĩ thuật điện tử, truyền thông", "subject_group": "", "point": "102.5", "note": "", "year": 2015}, {"major_code": "7D0401", "major_name": "Vật lí kĩ thuật", "subject_group": "", "point": "91.5", "note": "", "year": 2015}, {"major_code": "7D0101", "major_name": "Cơ kĩ thuật", "subject_group": "", "point": "97.5", "note": "", "year": 2015}, {"major_code": "7510203", "major_name": "Công nghệ kĩ thuật cơ điện tử", "subject_group": "", "point": "99.5", "note": "", "year": 2015}, {"major_code": "7480201", "major_name": "Công nghệ thông tin", "subject_group": "A", "point": "22", "note": "", "year": 2014}, {"major_code": "7480201", "major_name": "Công nghệ thông tin", "subject_group": "A1", "point": "22", "note": "", "year": 2014}, {"major_code": "7480101", "major_name": "Khoa học máy tính", "subject_group": "A", "point": "22", "note": "", "year": 2014}, {"major_code": "7480101", "major_name": "Khoa học máy tính", "subject_group": "A1", "point": "22", "note": "", "year": 2014}, {"major_code": "7480104", "major_name": "Hệ thống thông tin", "subject_group": "A", "point": "22", "note": "", "year": 2014}, {"major_code": "7480104", "major_name": "Hệ thống thông tin", "subject_group": "A1", "point": "22", "note": "", "year": 2014}, {"major_code": "7480102", "major_name": "Truyền thông và mạng máy tính", "subject_group": "A", "point": "22", "note": "", "year": 2014}, {"major_code": "7480102", "major_name": "Truyền thông và mạng máy tính", "subject_group": "A1", "point": "22", "note": "", "year": 2014}, {"major_code": "7510302", "major_name": "Công nghệ kỹ thuật điện tử, truyền thông", "subject_group": "A", "point": "19.5", "note": "", "year": 2014}, {"major_code": "7510302", "major_name": "Công nghệ kỹ thuật điện tử, truyền thông", "subject_group": "A1", "point": "19.5", "note": "", "year": 2014}, {"major_code": "7520401", "major_name": "Vật lý kỹ thuật", "subject_group": "A", "point": "18", "note": "", "year": 2014}, {"major_code": "7510203", "major_name": "Công nghệ kỹ thuật cơ điện tử", "subject_group": "A", "point": "18", "note": "", "year": 2014}, {"major_code": "7520101", "major_name": "Cơ kỹ thuật", "subject_group": "A", "point": "18", "note": "", "year": 2014}], "university_meta": {"url": "https://diemthi.tuyensinh247.com/diem-chuan/dai-hoc-cong-nghe-dai-hoc-quoc-gia-ha-noi-QHI.html", "university_code": "QHI", "university_name": "Đại Học Công Nghệ – Đại Học Quốc Gia Hà Nội"}}
{"diemchuan_datas": [{"major_code": "7380101", "major_name": "Luật", "subject_group": "C00", "point": "24.5", "note": "", "year": 2018}, {"major_code": "7380101", "major_name": "Luật", "subject_group": "A00", "point": "18.5", "note": "", "year": 2018}, {"major_code": "7380101", "major_name": "Luật", "subject_group": "D01", "point": "18.5", "note": "", "year": 2018}, {"major_code": "7380101", "major_name": "Luật", "subject_group": "D03", "point": "18", "note": "", "year": 2018}, {"major_code": "7380101", "major_name": "Luật", "subject_group": "D78", "point": "19", "note": "", "year": 2018}, {"major_code": "7380101", "major_name": "Luật", "subject_group": "D82", "point": "19", "note": "", "year": 2018}, {"major_code": "7380101 CLC", "major_name": "Luật Chất lượng cao", "subject_group": "A01; D01; D07; D78", "point": "18.25", "note": "", "year": 2018}, {"major_code": "7380110", "major_name": "Luật kinh doanh", "subject_group": "A00; A01; D01; D03; D78; D82", "point": "20.75", "note": "", "year": 2018}, {"major_code": "7380109", "major_name": "Luật Thương mại Quốc tế", "subject_group": "A00; A01; D01; D03; D78; D82", "point": "---", "note": "", "year": 2018}, {"major_code": "", "major_name": "Các ngành đào tạo đại học", "subject_group": "", "point": "---", "note": "", "year": 2017}, {"major_code": "7380101", "major_name": "Luật", "subject_group": "A00; C00; D01; D03; D78; D82", "point": "27.25", "note": "", "year": 2017}, {"major_code": "7380101CLC", "major_name": "Luật chất lượng cao đáp ứng Thông tư 23", "subject_group": "A01; D01; D07; D07; D78", "point": "---", "note": "", "year": 2017}, {"major_code": "7380110", "major_name": "Luật kinh doanh", "subject_group": "A00; A01; D01; D03; D78; D82", "point": "24", "note": "", "year": 2017}, {"major_code": "7380109", "major_name": "Luật kinh doanh*", "subject_group": "A00; D01; D02; D03", "point": "---", "note": "", "year": 2016}, {"major_code": "7380101", "major_name": "Luật", "subject_group": "C00; D01; D02; D03", "point": "---", "note": "", "year": 2016}, {"major_code": "7380101", "major_name": "Luật học", "subject_group": "", "point": "100.5", "note": "", "year": 2015}, {"major_code": "7380109", "major_name": "Luật kinh doanh", "subject_group": "", "point": "103", "note": "", "year": 2015}, {"major_code": "7380101", "major_name": "Luật học", "subject_group": "A", "point": "20", "note": "", "year": 2014}, {"major_code": "7380101", "major_name": "Luật học", "subject_group": "A1", "point": "20", "note": "", "year": 2014}, {"major_code": "7380101", "major_name": "Luật học", "subject_group": "C", "point": "20", "note": "", "year": 2014}, {"major_code": "7380101", "major_name": "Luật học", "subject_group": "D1", "point": "20", "note": "", "year": 2014}, {"major_code": "7380101", "major_name": "Luật học", "subject_group": "D3", "point": "20.5", "note": "", "year": 2014}, {"major_code": "7380109", "major_name": "Luật kinh doanh", "subject_group": "A", "point": "22", "note": "", "year": 2014}, {"major_code": "7380109", "major_name": "Luật kinh doanh", "subject_group": "A1", "point": "22", "note": "", "year": 2014}, {"major_code": "7380109", "major_name": "Luật kinh doanh", "subject_group": "D1", "point": "21.5", "note": "", "year": 2014}, {"major_code": "7380109", "major_name": "Luật kinh doanh", "subject_group": "D3", "point": "21.5", "note": "", "year": 2014}], "university_meta": {"url": "https://diemthi.tuyensinh247.com/diem-chuan/khoa-luat-dai-hoc-quoc-gia-ha-noi-QHL.html", "university_code": "QHL", "university_name": "Khoa Luật – Đại Học Quốc Gia Hà Nội"}}
```

# Stack

Python
Numpy
Pandas
Spark



# Author

Tran Minh Tuan - [tuantmtb](https://facebook.com/tuantmtb) - tuan@beecost.com

# BeeCost - Tiện ích mua sắm Online

BeeCost là Trợ lý mua sắm online. Giúp bạn mua hàng tiết kiệm hơn trên Shopee, Tiki, Sendo, Lazada, Adayroi. Ứng dụng được tạo từ việc phân tích hơn 50 triệu sản phẩm thương mại điện tử mỗi ngày. 

Tính năng chính của tiện ích BeeCost:

- Lịch sử giá hơn 50 triệu sản phẩm
- So sánh giá tìm nơi bán rẻ nhất
- Price Alert (Thông báo khi giảm giá)
- Tìm kiếm mã giảm giá tự động

> Tìm hiểu BeeCost tại [Trang chủ](https://www.beecost.com)

> Download [BeeCost Extension](https://www.beecost.com/download/extension?pub=github_opensource) trên Google Chrome

> Download [BeeCost Android](https://play.google.com/store/apps/details?id=com.beecost.assistance.shopee&hl=vi) trên Mobile