import configparser

cf = configparser.ConfigParser()
cf.read("./config.ini", encoding='utf-8')

src_bili_path = cf.get("process", "src_bili_path")
src_json_encode = cf.get("process", "src_json_encode")
det_bili_path = cf.get("process", "det_bili_path")