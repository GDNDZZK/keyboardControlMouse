# -*- encoding: utf-8 -*-
import os


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
    return result


def keyIsPress(keyCodes, rule):
    """
    传入配置文件读取的规则和键值列表,判断规定的键是否按下

    Args:
    - keyCodes:[164,91,79]
    - rule:"91+164|91+163"

    Returns:
    - bool
    """
    rule_split = rule.split("|")
    for a_rule in rule_split:
        rule_keys = a_rule.split("+")
        flag = True
        for key in rule_keys:
            if not int(key) in keyCodes:
                flag = False
                break
        if flag:
            return True
    return False
