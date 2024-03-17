# -*- encoding: utf-8 -*-
import os

setting_dict = dict()
def getConfigDict():
    """
    读取配置文件并返回一个字典

    Returns:
    - dict
    """
    local_path = './local/config/config.ini'
    file_path = local_path if os.path.exists(local_path) else './config/config.ini'
    # 创建一个空字典
    result = {}
    # 打开文件
    with open(file_path, "r", encoding='utf-8') as f:
        # 遍历文件的每一行
        for line in f:
            # 去掉行尾的换行符
            line = line.strip()
            # 如果行不为空，且不以;开头
            if line and not line.startswith(";"):
                # 用等号分割键和值
                key, value = line.split("=", 1)
                # 将键值对添加到字典中
                result[key] = value
    # 返回字典
    global setting_dict
    setting_dict = result
    return result


def keyIsPress(keys, rule):
    """
    传入配置文件读取的规则和键列表,判断规定的键是否按下

    Args:
    - keys:['<cmd>','<alt_l>']
    - rule:"<cmd>与<alt_l>或<cmd>与<alt_gr>"

    Returns:
    - bool
    """
    global setting_dict
    rule_split = rule.split(setting_dict['OR'])
    for a_rule in rule_split:
        rule_keys = a_rule.split(setting_dict['AND'])
        flag = True
        for key in rule_keys:
            if not key in keys:
                flag = False
                break
        if flag:
            return True
    return False
