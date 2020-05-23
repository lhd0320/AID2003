list01=["红桃","黑桃","方片","梅花"]
list02=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
list03=[r+c for r in list01 for c in list02]
print(list03)