"""
配置文件 - 简化版TradingAgents
只使用 DeepSeek 和 Tushare
"""
import os
from dotenv import load_dotenv

load_dotenv()

# API配置
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")
TUSHARE_TOKEN = os.getenv("TUSHARE_TOKEN", "")

# DeepSeek配置
DEEPSEEK_API_BASE = "https://api.deepseek.com/v1"
DEEPSEEK_MODEL = "deepseek-chat"

# 股票池配置 - 可以在这里配置要监控的股票
STOCK_WATCHLIST = [
    "001203.SZ",  # 大中矿业
    "600103.SH",  # 青山纸业  
    "600259.SH",  # 中稀有色
    "000981.SZ",  # 山子高科
    "000980.SZ",  # 众泰汽车
    "601899.SH",  # 紫金矿业
    "600293.SH",  # 三峡新材
    "600111.SH",  # 北方稀土
    "002131.SZ",  # 利欧股份
    "600010.SH",  # 包钢股份
]

# 定时任务配置 - 双时段分析
PRE_MARKET_TIME = "07:30"   # 开盘前分析时间
MIDDAY_TIME = "12:00"       # 中午分析时间

# 兼容性保持
DAILY_REPORT_TIME = PRE_MARKET_TIME

# 报告配置
REPORT_DIR = "reports"
LOG_DIR = "logs"
DATA_CACHE_DIR = "data/cache"

# 分析配置
MAX_DEBATE_ROUNDS = 2  # 辩论轮次
ENABLE_NEWS_ANALYSIS = True  # 是否启用新闻分析
ANALYSIS_HISTORY_DAYS = 60  # 分析历史数据天数

# LLM配置
LLM_CONFIG = {
    "temperature": 0.7,
    "max_tokens": 4000,
    "top_p": 0.95,
}

# 验证配置
def validate_config():
    """验证配置是否完整"""
    if not DEEPSEEK_API_KEY:
        raise ValueError("请设置 DEEPSEEK_API_KEY 环境变量")
    if not TUSHARE_TOKEN:
        raise ValueError("请设置 TUSHARE_TOKEN 环境变量")
    print("✅ 配置验证通过")
    print(f"📊 监控股票数量: {len(STOCK_WATCHLIST)}")
    print(f"⏰ 推送时间: {DAILY_REPORT_TIME}")
    return True

