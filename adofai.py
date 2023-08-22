import json
import chardet
import re


class OneLineEncoder(json.JSONEncoder):
  def encode(self, o):
    return json.dumps(o, separators=(',', ':'))
  
class Encoder:

    def __init__(self, filename, indent=None): 
        self.filename = filename
        self.indent = indent
    
    def encode_and_dump(self):

      data = json.load(open(self.filename))
      
      # 处理actions单行格式化
      actions = [action for action in data['actions']]
      data['actions'] = actions
      
      # 编码并输出
      with open(self.filename,'w') as f:
          json.dump(data,f, cls=OneLineEncoder,indent=2)
      
      with open(self.filename, 'r') as f:
        content = f.read()
      
      content = content.replace("\\", "")

      with open(self.filename, 'w') as f:
        f.write(content)

      ...

def convert_encoding(file, to_enc):

    # 读取文件内容
    with open(file, 'rb') as f:
        data = f.read()

    # 检测编码    
    detected = chardet.detect(data)
    from_enc = detected['encoding']

    print(f"转换编码至utf-8")
    
    # 转换编码
    data = data.decode(from_enc).encode(to_enc)   

    # 保存文件
    with open(file, 'wb') as f:
         f.write(data)

# 修复JSON文件中的语法错误,并格式化代码
def fix_json(filename):

  # 读取文件内容
  with open(filename, encoding="utf-8") as f:
    content = f.read()

  # 使用正则表达式删除所有末尾逗号
  fixed_content = re.sub(r',(\s*})', r'\1', content)

  # 使用json.dumps格式化JSON格式
  formatted_content = json.dumps(json.loads(fixed_content), indent=2)

  # 保存格式化后的文件内容
  with open(filename, 'w') as f:
    f.write(formatted_content)

# 删除指定事件类型
# 删除指定事件类型
def remove_event(filename, event_type):

  with open(filename) as f:
    data = json.load(f)

  actions = []
  for action in data['actions']:
    if action['eventType'] != event_type:
      actions.append(action)

  data['actions'] = actions
  
  with open(filename, 'w') as f:
     json.dump(data, f)



name = input()
convert_encoding(name, 'utf-8')
fix_json(name)
encoder = Encoder(name)
remove_event(name, 'MoveCamera')
encoder.encode_and_dump()
