import xarray as xr
import os

# تحديد المسار إلى ملف NetCDF
current_dir = os.getcwd()
file_path = os.path.join(current_dir, 'ncFiles', 'AERDB_L2_VIIRS_NOAA20.A2024260.0948.002.2024260220657.nc')

# التحقق من وجود الملف
if not os.path.exists(file_path):
    raise FileNotFoundError(f"الملف المحدد غير موجود: {file_path}")

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

# تحديد اسم ملف NetCDF الذي سيتم إنشاؤه (تحديد اسم الملف ضمن المسار)
output_file_path = r'C:\Users\3ab3zeez\Desktop\EarthData\ncFiles\filtered_aerosol_data.nc'

try:
    # فتح ملف NetCDF الأصلي
    ds = xr.open_dataset(file_path)

    # تحديد المتغيرات المطلوبة
    ds_selected = ds[selected_variables]

    # حفظ المتغيرات المحددة فقط في ملف NetCDF جديد
    ds_selected.to_netcdf(output_file_path)

    print(f"تم إنشاء ملف NetCDF جديد يحتوي على المتغيرات المطلوبة فقط وتم حفظه في: {output_file_path}")

except PermissionError:
    print(f"خطأ: لا يوجد صلاحيات للكتابة في المسار المحدد: {output_file_path}")
except FileNotFoundError as fnf_error:
    print(f"خطأ: {fnf_error}")
except Exception as e:
    print(f"حدث خطأ غير متوقع: {e}")
