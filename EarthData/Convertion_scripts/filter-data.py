import xarray as xr
import os

# تحديد المسار الحالي
current_dir = os.getcwd()

# مسار المجلد الذي يحتوي على ملفات NetCDF
input_dir = os.path.join(current_dir, 'downloaded_nc_files')

# مسار المجلد الذي سيتم إنشاء الملفات المفلترة بداخله
output_dir = os.path.join(current_dir, 'filteredData')

# إنشاء مجلد filteredData إذا لم يكن موجودًا
os.makedirs(output_dir, exist_ok=True)

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

# التحقق من وجود مجلد downloaded_nc_files
if not os.path.exists(input_dir):
    raise FileNotFoundError(f"المجلد المحدد غير موجود: {input_dir}")

# المرور على جميع الملفات ذات الامتداد .nc في المجلد
for filename in os.listdir(input_dir):
    if filename.endswith(".nc"):
        # تحديد المسار الكامل للملف
        file_path = os.path.join(input_dir, filename)

        try:
            # فتح ملف NetCDF الأصلي
            ds = xr.open_dataset(file_path)

            # تحديد المتغيرات المطلوبة
            ds_selected = ds[selected_variables]

            # تحديد مسار الملف المفلتر الجديد في مجلد filteredData
            output_file_path = os.path.join(output_dir, f'filtered_{filename}')

            # حفظ المتغيرات المحددة فقط في ملف NetCDF جديد
            ds_selected.to_netcdf(output_file_path)

            print(f"تم إنشاء ملف NetCDF جديد يحتوي على المتغيرات المطلوبة فقط وتم حفظه في: {output_file_path}")

        except PermissionError:
            print(f"خطأ: لا يوجد صلاحيات للكتابة في المسار المحدد: {output_file_path}")
        except FileNotFoundError as fnf_error:
            print(f"خطأ: {fnf_error}")
        except KeyError:
            print(f"خطأ: بعض المتغيرات المطلوبة غير موجودة في الملف: {file_path}")
        except Exception as e:
            print(f"حدث خطأ غير متوقع أثناء معالجة الملف {file_path}: {e}")
