import logging
import os
from datetime import datetime

class BotLogger:
    def __init__(self, log_dir="logs"):
        self.log_dir = log_dir
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        # إعداد logger رئيسي
        self.logger = logging.getLogger('ShadowBot')
        self.logger.setLevel(logging.DEBUG)
        
        # تنسيق السجلات
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        # ملف الأخطاء
        error_handler = logging.FileHandler(
            f"{log_dir}/error_{datetime.now().strftime('%Y%m%d')}.log"
        )
        error_handler.setLevel(logging.ERROR)
        error_handler.setFormatter(formatter)
        
        # ملف المعلومات
        info_handler = logging.FileHandler(
            f"{log_dir}/bot_{datetime.now().strftime('%Y%m%d')}.log"
        )
        info_handler.setLevel(logging.INFO)
        info_handler.setFormatter(formatter)
        
        # سجل التصحيح (اختياري)
        debug_handler = logging.FileHandler(
            f"{log_dir}/debug_{datetime.now().strftime('%Y%m%d')}.log"
        )
        debug_handler.setLevel(logging.DEBUG)
        debug_handler.setFormatter(formatter)
        
        # طباعة على الكونسول
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        
        self.logger.addHandler(error_handler)
        self.logger.addHandler(info_handler)
        self.logger.addHandler(debug_handler)
        self.logger.addHandler(console_handler)
    
    def get_logger(self):
        return self.logger

# إنشاء نسخة عالمية
bot_logger = BotLogger()
logger = bot_logger.get_logger()
