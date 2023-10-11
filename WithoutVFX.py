import re
import sys
import os
import optparse



def loadin(filepath):
    #载入为列表
    with open(filepath,'r') as f:
        content = f.readlines()
    return content

def delVFX(content):
    #正则
    regular = "Flash|SetFilter|HallOfMirrors|ShakeScreen|Bloom|MoveDecoration|AddDecoration"
    #临时列表
    temp = list()
    #删除后的列表
    for a in content:
        if not re.search(regular,a):
            temp.append(a)
    return temp

def save(content_a):
    #修改后文件名
    folder_path = os.path.dirname(file_path)
    new_file_name,extension = os.path.splitext(os.path.basename(file_path))
    new_file_path = os.path.join(folder_path,f"{new_file_name}(Without VFX){extension}")

    #写入
    with open(new_file_path,'w') as f:
        f.writelines(content_a)
    
    print("OK")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        sys.exit(1)

    content_list = loadin(file_path)
    content_list = delVFX(content_list)
    save(content_list)