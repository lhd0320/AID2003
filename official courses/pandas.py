import pandas as pd

fpath='/tarena/广州市南沙区组织员招聘第二批拟录用人员名单.xlsx'
ratings=pd.read.xlsx(fpath)
ratings.head()