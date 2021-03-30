#自己打包exe
#pyinstaller -F my_sum.py
#提取 資料夾內的.py文件 ok
#提取 運行程式的資料夾 OK
#跨出py檔案操作cmd 指令 ok
#刪除不重要的檔案
"""
多餘檔案
1."__pycache__" 資料夾
2."build" 資料夾
3."dist" 資料夾
4.提取 "dist" 中的到原本的path
5.刪除"dist"
"""
a =["__pycache__","build","dist"]

import os
import shutil

def copyfile(ori_path):
    #複製dist中的exe到原資料夾
    wd_temp = os.getcwd()
    #files_name_list = os.listdir(wd_temp)    
    shutil.move(ori_path,wd_temp)
    #移動檔案

wd = os.getcwd()# 這是路徑
command = "cd "+wd
os.system(command) 

files = os.listdir(wd)

# 以迴圈處理
for f in files:
  # 產生檔案的絕對路徑
  fullpath = os.path.join(wd, f)
  # 判斷 fullpath 是檔案還是目錄
  if os.path.isfile(fullpath):
    print("檔案：", f)
    if ".py" in f:
        
        pyname =f.split(".py")[0]
        print("程式碼檔名",pyname)
        
        comop = "pyinstaller -F "+f
        os.system(comop)
        for i in a:
            if i == "dist":
                copyfile(wd+"/"+i+"/"+pyname+".exe")
            shutil.rmtree(wd+"/"+i)
        os.remove(wd +"/"+pyname+".spec")
