# config.example.py
# 模板配置文件 (Template Configuration)
# 使用方法: 复制此文件并重命名为 config.py，然后修改其中的坐标。
# Usage: Copy this file to config.py and update coordinates for your device.

# ==============================================================================
# 1. ADB & DEVICE SETTINGS (ADB 与设备设置)
# ==============================================================================
DEVICE_SERIAL = None 
PACKAGE_NAME = "com.okinc.okex.gp"

# ==============================================================================
# 2. COORDINATES (X, Y)
# ==============================================================================
# 底部导航栏 - "星球" (Planet Tab)
NAV_PLANET_X, NAV_PLANET_Y = 742, 2118

# 用户个人主页图标 (User Profile Icon)
NAV_PROFILE_ICON_X, NAV_PROFILE_ICON_Y = 115,136

# 星球页面顶部搜索入口 (Search Icon on Planet Page)
PLANET_SEARCH_ICON_X, PLANET_SEARCH_ICON_Y = 569,153

# 搜索页面的输入框 (Search Input Box)
PLANET_SEARCH_INPUT_X, PLANET_SEARCH_INPUT_Y = 569,153

# 搜索结果的第一个条目 (First Result Item)
PLANET_SEARCH_RESULT_X, PLANET_SEARCH_RESULT_Y = 0, 0

# 返回按钮 (Back Button)
NAV_BACK_X, NAV_BACK_Y = 109, 126

# --- Task A: Group Chat Shout-out ---
GROUP_TOP1_X, GROUP_TOP1_Y = 585, 783
CHAT_INPUT_X, CHAT_INPUT_Y = 574, 2100
CHAT_SEND_X, CHAT_SEND_Y = 986,2051

# --- Task B: Share Profile Card (Refined Search Flow) ---

# 目标群组名称 (精确匹配) - 用于搜索
TARGET_GROUP_NAME = "test" 

# 1. 个人主页右上角的 "..." (更多) 图标 (Three Dots / More)
PROFILE_MORE_X, PROFILE_MORE_Y = 974, 121

# 2. 弹出菜单中的 "分享主页" 选项 (Share Profile Option)
PROFILE_MENU_SHARE_X, PROFILE_MENU_SHARE_Y = 535, 2118

# 3. 分享列表中的 "聊天" 图标 (Share to Chat)
SHARE_TO_CHAT_X, SHARE_TO_CHAT_Y = 128,2004

# 4. 联系人选择页面的 "搜索" 输入框 (Search Input)
SHARE_SEARCH_X, SHARE_SEARCH_Y = 553,392

# 5. 搜索结果列表中的 "第1项" (First Result)
SHARE_RESULT_1_X, SHARE_RESULT_1_Y = 548, 589

# 6. 底部的 "发送/分享" 确认按钮 (Bottom Send/Share Button)
SHARE_BOTTOM_BTN_X, SHARE_BOTTOM_BTN_Y = 548, 2090

# --- Task C: Follow Back ---
PROFILE_FANS_LIST_X, PROFILE_FANS_LIST_Y = 328, 600

# Follow Scan Settings (Legacy/Fallback)
FOLLOW_BTN_X = 900
FOLLOW_BTN_Y_START = 500
FOLLOW_BTN_Y_END = 1800
FOLLOW_BTN_STEP = 250 

# ==============================================================================
# 3. TEXT POOL (SHOUT-OUT MESSAGES)
# ==============================================================================
MSG_POOL = [
    "互关互关，秒回关",           # Mutual follow
    "互关秒回",             # Must follow back
    "互关互关，一起发财",           # Get rich together
]

# ==============================================================================
# 4. TIMING & SCHEDULER
# ==============================================================================
CLICK_DELAY_MIN = 0.8
CLICK_DELAY_MAX = 1.5
TYPING_DELAY_MIN = 1.0
TYPING_DELAY_MAX = 2.0
# 保留本地的等待时间配置
LOOP_WAIT_MIN = 600
LOOP_WAIT_MAX = 900

# ==============================================================================
# 5. OCR SETTINGS (OCR 设置 - PaddleOCR)
# ==============================================================================
# 最大滑动次数（在消息列表中查找群组时）
# Maximum scroll attempts when searching for group in message list
OCR_MAX_SCROLL = 5

# ==============================================================================
# 6. TASK C SETTINGS (任务 C 设置 - 粉丝回关)
# ==============================================================================
# 关注按钮图像识别阈值 (0.0-1.0)，越低越宽松
# Follow button image recognition threshold
FOLLOW_BTN_THRESHOLD = 0.9
