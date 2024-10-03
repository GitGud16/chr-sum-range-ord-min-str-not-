import xarray as xr
import os

# تحديد المسار إلى ملف NetCDF باستخدام المسار الحالي
current_dir = os.getcwd()  # الحصول على المسار الحالي للمجلد
filePath = os.path.join(current_dir, 'ncFiles', 'AERDB_L2_VIIRS_NOAA20.A2024260.0948.002.2024260220657.nc')

# تحديد المسار إلى مجلد CSV
output_dir = os.path.join(current_dir, 'csvFiles')

# التحقق من وجود الملف
if not os.path.exists(filePath):
    raise FileNotFoundError(f"الملف المحدد غير موجود: {filePath}")

# إنشاء مجلد csvFiles إذا لم يكن موجودًا
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"تم إنشاء المجلد: {output_dir}")

# تحديد اسم ملف CSV الذي سيتم إنشاؤه
output_file = os.path.join(output_dir, 'output.csv')

try:
    # فتح ملف NetCDF وتحويله إلى DataFrame ثم حفظه كملف CSV
    DS = xr.open_dataset(filePath)
    DS.to_dataframe().to_csv(output_file)
    print(f"تم تحويل ملف NetCDF إلى CSV بنجاح وتم حفظه في: {output_file}")

except PermissionError:
    print(f"خطأ: لا يوجد صلاحيات للكتابة في المسار المحدد: {output_file}")
    print("يرجى تجربة تشغيل البرنامج كمسؤول (Run as administrator) أو تحديد مسار مختلف للحفظ.")
except FileNotFoundError as fnf_error:
    print(f"خطأ: {fnf_error}")
    print("تأكد من وجود ملف NetCDF في المسار المحدد وتحقق من صحة اسم الملف.")
except Exception as e:
    print(f"حدث خطأ غير متوقع: {e}")
