# 封装日志文件
import logging

def test_log():
    # 创建一个日志器
    logger = logging.getLogger()
    # 设置日志级别
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        # 输出日志到控制台去
        sh = logging.StreamHandler()
        logger.addHandler(sh)

        # 格式器
        fomatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s %(funcName)s %(message)s')
        sh.setFormatter(fomatter)

        # 文本处理器
        fh = logging.FileHandler('../log/log.txt')
        fh.setFormatter(fomatter)
        return logger


