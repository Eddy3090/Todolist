import os
import pandas as pd
import shutil
# save csv_file
def csv_save(content, header_info, out_file):
    '''
    description: 
    param {content, header_info, out_file}
    return {None} 
    author: zhangcheng
    '''  
    info_data = pd.DataFrame(content, columns=header_info)
    if header_info == None:
        info_data.to_csv(out_file,index=None, header=False, encoding="utf_8_sig")
    else:
        info_data.to_csv(out_file,index=None, encoding="utf_8_sig")

def main(base_folder, csvFile):
    namelist = os.listdir(base_folder)
    namelist.sort()
    df = pd.read_csv(csvFile, encoding='gbk')
    tors = list(df['seed_name'])
    maps = dict()
    for i in range(len(tors)):
        tor = tors[i].split('.')[-2]
        if tor in namelist:
            maps[tor] = df.iloc[i,1]
    for item in maps.items():
        src = os.path.join(base_folder, item[0])
        dst = os.path.join(base_folder, item[1])
        if os.path.exists(src):
            shutil.move(src, dst)

if __name__ == "__main__":
    base_folder = r'D:/资料/IPS/dalu20'
    csvFile = r'D:/资料/IPS/dalu20/down.csv'
    main(base_folder, csvFile)