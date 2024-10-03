import xarray as xr
import os
import json

# تحديد المسار إلى المجلد الذي يحتوي على ملفات NetCDF
current_dir = os.getcwd()  # الحصول على المسار الحالي للمجلد
input_dir = os.path.join(current_dir, 'filteredData')  # مسار المجلد الذي يحتوي على ملفات NetCDF

# تحديد المسار إلى مجلد JSON الذي سيتم حفظ الملفات المحولة فيه
output_dir = os.path.join(current_dir, 'filteredData-json')

# التحقق من وجود المجلد filteredData
if not os.path.exists(input_dir):
    raise FileNotFoundError(f"المجلد المحدد غير موجود: {input_dir}")

# إنشاء مجلد filteredData-json إذا لم يكن موجودًا
os.makedirs(output_dir, exist_ok=True)
print(f"تم إنشاء المجلد أو التحقق من وجوده: {output_dir}")

# المرور على جميع الملفات ذات الامتداد .nc في المجلد filteredData
for filename in os.listdir(input_dir):
    if filename.endswith(".nc"):
        # تحديد المسار الكامل للملف
        file_path = os.path.join(input_dir, filename)

        # تحديد اسم ملف JSON الذي سيتم إنشاؤه
        output_file = os.path.join(output_dir, f'{os.path.splitext(filename)[0]}.json')

        try:
            # فتح ملف NetCDF وتحويله إلى DataFrame ثم حفظه كملف JSON
            ds = xr.open_dataset(file_path)
            df = ds.to_dataframe()

            # تحويل DataFrame إلى JSON
            df.to_json(output_file, orient="split")  # يمكنك استخدام orient="records" لتنسيق أسهل للقراءة

            print(f"تم تحويل ملف NetCDF {filename} إلى JSON بنجاح وتم حفظه في: {output_file}")

        except PermissionError:
            print(f"خطأ: لا يوجد صلاحيات للكتابة في المسار المحدد: {output_file}")
            print("يرجى تجربة تشغيل البرنامج كمسؤول (Run as administrator) أو تحديد مسار مختلف للحفظ.")
        except FileNotFoundError as fnf_error:
            print(f"خطأ: {fnf_error}")
            print("تأكد من وجود ملف NetCDF في المسار المحدد وتحقق من صحة اسم الملف.")
        except Exception as e:
            print(f"حدث خطأ غير متوقع أثناء معالجة الملف {file_path}: {e}")
