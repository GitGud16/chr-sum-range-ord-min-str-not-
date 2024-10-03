import os
import requests
import xarray as xr
import json

# تحديد اسم ملف JSON الذي يحتوي على الروابط
#json_file_path = '/mnt/data/LAADS_query.2024-10-03T04_45.json'

current_dir = os.getcwd()  # الحصول على المسار الحالي للمجلد
json_file_path = os.path.join(current_dir, 'jsonFiles', 'LAADS_query.2024-10-03T04_45.json')

# قراءة الروابط من ملف JSON
with open(json_file_path, 'r') as file:
    data = json.load(file)

# استخراج الروابط من البيانات
base_url = "https://ladsweb.modaps.eosdis.nasa.gov"
download_links = []
for key, value in data.items():
    if isinstance(value, dict) and 'url' in value:
        download_links.append(base_url + value['url'])

# تحديد مجلد التنزيل
download_folder = 'downloaded_nc_files'
os.makedirs(download_folder, exist_ok=True)

# تنزيل الملفات من الروابط
downloaded_files = []
for link in download_links:
    file_name = os.path.basename(link)
    file_path = os.path.join(download_folder, file_name)
    
    # تنزيل الملف
    response = requests.get(link)
    if response.status_code == 200:
        with open(file_path, 'wb') as f:
            f.write(response.content)
        downloaded_files.append(file_path)
        print(f"تم تنزيل الملف: {file_name}")
    else:
        print(f"فشل تنزيل الملف: {file_name}")

# تحديد المتغيرات المطلوبة
selected_variables = [
    'Aerosol_Optical_Thickness_550_Land',
    'Aerosol_Type_Land',
    'Angstrom_Exponent_Land',
    'Total_Column_Ozone',
    'Precipitable_Water',
    'Wind_Speed',
    'Latitude',
    'Longitude'
]

# دمج الملفات مع المتغيرات المطلوبة
merged_dataset = xr.Dataset()

for nc_file in downloaded_files:
    try:
        # فتح ملف NetCDF
        ds = xr.open_dataset(nc_file)
        
        # اختيار المتغيرات المطلوبة فقط
        selected_ds = ds[selected_variables]
        
        # دمج البيانات مع المجموع الكلي
        merged_dataset = xr.merge([merged_dataset, selected_ds])
        print(f"تم دمج الملف: {nc_file}")
    except Exception as e:
        print(f"حدث خطأ أثناء معالجة الملف {nc_file}: {e}")

# حفظ الملف المدمج
output_file_path = os.path.join(download_folder, 'merged_aerosol_data.nc')
merged_dataset.to_netcdf(output_file_path)
print(f"تم إنشاء ملف NetCDF المدمج وحفظه في: {output_file_path}")
