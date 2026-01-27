#工程路径
import os

project_path = os.path.dirname(os.path.abspath(__file__))
datas_path = os.path.join(project_path, 'datas')
logs_path = os.path.join(project_path, 'logs')
#项目路径
project_url = "http://sky.nnzhp.cn"

phone_num = ""

if __name__ == '__main__':
    print(project_path)
    print(datas_path)