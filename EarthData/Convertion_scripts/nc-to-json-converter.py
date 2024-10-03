import xarray as xr
import os
import json

# تحديد المسار إلى ملف NetCDF باستخدام المسار الحالي
current_dir = os.getcwd()  # الحصول على المسار الحالي للمجلد
filePath = os.path.join(current_dir, 'ncFiles', 'filtered_aerosol_data.nc')

# تحديد المسار إلى مجلد JSON
output_dir = os.path.join(current_dir, 'jsonFiles')

# التحقق من وجود الملف
if not os.path.exists(filePath):
    raise FileNotFoundError(f"الملف المحدد غير موجود: {filePath}")

# إنشاء مجلد jsonFiles إذا لم يكن موجودًا
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"تم إنشاء المجلد: {output_dir}")

# تحديد اسم ملف JSON الذي سيتم إنشاؤه
output_file = os.path.join(output_dir, 'output2.json')

try:
    # فتح ملف NetCDF وتحويله إلى DataFrame ثم حفظه كملف JSON
    DS = xr.open_dataset(filePath)
    df = DS.to_dataframe()

    # تحويل DataFrame إلى JSON
    df.to_json(output_file, orient="split")  # يمكنك استخدام orient="records" لتنسيق أسهل للقراءة

    print(f"تم تحويل ملف NetCDF إلى JSON بنجاح وتم حفظه في: {output_file}")

except PermissionError:
    print(f"خطأ: لا يوجد صلاحيات للكتابة في المسار المحدد: {output_file}")
    print("يرجى تجربة تشغيل البرنامج كمسؤول (Run as administrator) أو تحديد مسار مختلف للحفظ.")
except FileNotFoundError as fnf_error:
    print(f"خطأ: {fnf_error}")
    print("تأكد من وجود ملف NetCDF في المسار المحدد وتحقق من صحة اسم الملف.")
except Exception as e:
    print(f"حدث خطأ غير متوقع: {e}")
