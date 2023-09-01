# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 20:07:28 2023

@author: HP
"""

import pandas as pd

frnds=pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\friend_names.csv")
frnds
frnds.columns
df_fil=frnds.groupby(['quality'])['friendName'].count()
df_fil

boys=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\boys_names.xlsx")
boys
girls=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\girls_names.xlsx")
girls
boys_fil=boys.groupby(['quality'])['boys_name'].count()
boys_fil
girls_fil=girls.groupby(['quality'])['girls_name'].count()
girls_fil

father=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\FatherFamily_members.xlsx")
father
mother=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\motherFamily_members.xlsx")
mother
mother_fil=mother.groupby(['relation'])['mother_family_member'].count()
mother_fil
father_fil=father.groupby(['relation'])['family_member_name'].count()
father_fil

dal_items=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\dal_items.xlsx")
dal_items
dal_fil=dal_items.groupby(['Taste'])['item'].count()
dal_fil
veg=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\VEG_FOOD_ITEMS.xlsx")
veg
veg_fil=veg.groupby(['Taste'])['veg_food_item'].count()
veg_fil


soups=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\soup_items.xlsx")
soups
soups_fil=soups.groupby(['taste'])['veg_food_item'].count()
soups_fil
fry=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\fry_items.xlsx")
fry
fry_fil=fry.groupby(['taste'])['veg_food_name'].count()
fry_fil


chicken=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\Chicken_items.xlsx")
chicken
chicken_fil=chicken.groupby(['taste'])['NonVegFoodName'].count()
chicken_fil
mutton=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\mutton_items.xlsx")
mutton
mutton_fil=mutton.groupby(['taste'])['NonVegFoodName'].count()
mutton_fil


winter=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\winterseason_names.xlsx")
winter
winter_fil=winter.groupby(['season'])['MonthName'].count()
winter_fil
summer=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\summerseason_names.xlsx")
summer
summer_fil=summer.groupby(['season'])['MonthName'].count()
summer_fil
rainy=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\rainyseason_names.xlsx")
rainy
rainy_fil=rainy.groupby(['season'])['MonthName'].count()
rainy_fil

red=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\red_colour.xlsx")
red
red_fil=red.groupby(['colour'])['flower name'].count()
red_fil
white=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\whiteflowers_names.xlsx")
white
pink=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\pinkflowers_names.xlsx")
pink
pink_fil=pink.groupby(['colour'])['flower name'].count()
pink_fil
white_fil=white.groupby(['colour'])['flower name'].count()
white_fil
yellow=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\yellowflowers_names.xlsx")
yellow
yellow_fil=yellow.groupby(['colour'])['flower name'].count()
yellow_fil