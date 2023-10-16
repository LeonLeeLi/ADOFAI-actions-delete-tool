import json
import os
import re
import sys


class OneLineEncoder(json.JSONEncoder):
    def encode(self, o):
        return json.dumps(o, separators=(",", ":"))


class Encoder:
    def __init__(self, filename, event_type, indent=None):
        self.filename = filename
        self.event_type = event_type
        self.indent = indent

    def encode_and_dump(self):
        with open(self.filename, 'r', encoding='utf-8-sig') as f:
            data = json.load(f)

        # 处理actions单行格式化
        actions = [action for action in data["actions"]]
        data["actions"] = actions

        # 编码并输出
        with open(self.filename, "w", encoding='utf-8-sig') as f:
            json.dump(data, f, cls=OneLineEncoder, indent=2)

        with open(self.filename, "r", encoding='utf-8-sig') as f:
            content = f.read()

        content = content.replace("\\", "")

        with open(self.filename, "w", encoding='utf-8-sig') as f:
            f.write(content)

    # 修复JSON文件中的语法错误,并格式化代码
    def fix_json(self):
        # 读取文件内容
        with open(self.filename, encoding="utf-8-sig") as f:
            content = f.read()

        # 使用正则表达式删除所有末尾逗号
        fixed_content = re.sub(r",(\s*})", r"\1", content)
        fixed_content = re.sub(r",,", r",,", fixed_content)

        # 使用json.dumps格式化JSON格式
        formatted_content = json.dumps(json.loads(fixed_content), indent=2)

        # 保存格式化后的文件内容
        with open(self.filename, "w", encoding='utf-8-sig') as f:
            f.write(formatted_content)

    # 删除指定事件类型
    def remove_event(self):
        file_name = os.path.splitext(self.filename)[0]
        file_extension = os.path.splitext(self.filename)[1]

        with open(self.filename, 'r', encoding='utf-8-sig') as f:
            data = json.load(f)

        actions = []
        for action in data["actions"]:
            if action["eventType"] not in self.event_type:
                actions.append(action)

        data["actions"] = actions

        new_filename = f'{file_name}(Without VFX){file_extension}'
        with open(new_filename, "w", encoding='utf-8-sig') as f:
            json.dump(data, f)


def Help():
    filepath = sys.argv[0]
    print(
        f"""
    A Dance Of Fire And Ice VFX Remove Helper
        
RemoveVFX: {filepath} \033[31mYourAdofaiFilePath\033[0m or \033[31mDrag On exe(py)\033[0m
Help: {filepath} --help
"""
    )


if __name__ == "__main__":
    try:
        filepath = sys.argv[1]
        if filepath == "--help":
            Help()
    except:
        Help()
        os.system("pause")
        sys.exit(0)
        ...

    print('''
    请选择需要移除的项，例: ACD --> 删除"移动轨道","滤镜"和"镜厅"
    A:移动轨道
    B:设置轨道颜色
    C:重新设置轨道颜色
    D:滤镜
    E:镜厅
    F:振屏
    G:绽放
    H:运镜
    ''')
    options={
        'A':'MoveTrack',
        'B':'ColorTrack',
        'C':'RecolorTrack',
        'D':'SetFilter',
        'E':'HallOfMirrors',
        'F':'ShakeScreen',
        'G':'Bloom',
        'H':'MoveCamera'
    }
    selected = input().upper()
    selected_options = []
    for option in selected:
        if option in options:
            selected_options.append(options[option])
    os.system("pause")
    encoder = Encoder(filepath,selected_options)
    encoder.fix_json()
    encoder.remove_event()
    encoder.encode_and_dump()
    
