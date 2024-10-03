import xarray as xr

# فتح ملف NetCDF
file_path = r"C:\Users\3ab3zeez\Desktop\EarthData\ncFiles\filtered_aerosol_data.nc"
    ##AERDB_L2_VIIRS_NOAA20.A2024260.0948.002.2024260220657.nc"
dataset = xr.open_dataset(file_path)

# استخراج المعلومات بشكل منظم
dataset_summary = f"File Name: {file_path.split('/')[-1]}\n"
dataset_summary += f"{'='*50}\n"
dataset_summary += "Global Attributes:\n"
dataset_summary += f"{'-'*50}\n"

# إضافة السمات العامة للملف
for attr, value in dataset.attrs.items():
    dataset_summary += f"{attr}: {value}\n"

dataset_summary += f"{'='*50}\n"
dataset_summary += "Dimensions:\n"
dataset_summary += f"{'-'*50}\n"

# إضافة الأبعاد
for dim, size in dataset.sizes.items():
    dataset_summary += f"{dim}: {size}\n"

dataset_summary += f"{'='*50}\n"
dataset_summary += "Variables:\n"
dataset_summary += f"{'-'*50}\n"

# إضافة المتغيرات مع تفاصيلها
for var in dataset.variables:
    var_data = dataset[var]
    dataset_summary += f"Variable Name: {var}\n"
    dataset_summary += f" - Dimensions: {var_data.dims}\n"
    dataset_summary += f" - Data Type: {var_data.dtype}\n"
    dataset_summary += f" - Attributes:\n"
    for attr, value in var_data.attrs.items():
        dataset_summary += f"    - {attr}: {value}\n"
    dataset_summary += f"{'-'*50}\n"

# غلق الملف بعد العرض
dataset.close()

# طباعة الملخص النهائي للبيانات
print(dataset_summary)
