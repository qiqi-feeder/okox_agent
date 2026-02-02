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
NAV_PLANET_X, NAV_PLANET_Y = 0, 0 

# 星球页面顶部搜索入口 (Search Icon on Planet Page)
PLANET_SEARCH_ICON_X, PLANET_SEARCH_ICON_Y = 0, 0

# 搜索页面的输入框 (Search Input Box)
PLANET_SEARCH_INPUT_X, PLANET_SEARCH_INPUT_Y = 0, 0

# 搜索结果的第一个条目 (First Result Item)
PLANET_SEARCH_RESULT_X, PLANET_SEARCH_RESULT_Y = 0, 0

# 用户个人主页图标 (User Profile Icon)
NAV_PROFILE_ICON_X, NAV_PROFILE_ICON_Y = 0, 0

# 返回按钮 (Back Button)
NAV_BACK_X, NAV_BACK_Y = 0, 0

# --- Task A: Group Chat Shout-out ---
GROUP_TOP1_X, GROUP_TOP1_Y = 0, 0
CHAT_INPUT_X, CHAT_INPUT_Y = 0, 0
CHAT_SEND_X, CHAT_SEND_Y = 0, 0

# --- Task B: Share Profile Card (Refined Search Flow) ---
TARGET_GROUP_NAME = "TargetGroupName"

# 1. More/Three Dots Icon
PROFILE_MORE_X, PROFILE_MORE_Y = 0, 0

# 2. Share Profile Option (Popup)
PROFILE_MENU_SHARE_X, PROFILE_MENU_SHARE_Y = 0, 0

# 3. Share to Chat Icon
SHARE_TO_CHAT_X, SHARE_TO_CHAT_Y = 0, 0

# 4. Search Input Box
SHARE_SEARCH_X, SHARE_SEARCH_Y = 0, 0

# 5. First Search Result
SHARE_RESULT_1_X, SHARE_RESULT_1_Y = 0, 0

# 6. Bottom Share Button
SHARE_BOTTOM_BTN_X, SHARE_BOTTOM_BTN_Y = 0, 0

# --- Task C: Follow Back ---
PROFILE_FANS_LIST_X, PROFILE_FANS_LIST_Y = 0, 0

# Follow Scan Settings (Legacy/Fallback)
FOLLOW_BTN_X = 900
FOLLOW_BTN_Y_START = 500
FOLLOW_BTN_Y_END = 1800
FOLLOW_BTN_STEP = 250 

# ==============================================================================
# 3. TEXT POOL (SHOUT-OUT MESSAGES)
# ==============================================================================
MSG_POOL = [
    "互关互关",           # Mutual follow
    "必回关",             # Must follow back
    "一起发财",           # Get rich together
]

# ==============================================================================
# 4. TIMING & SCHEDULER
# ==============================================================================
CLICK_DELAY_MIN = 1.5
CLICK_DELAY_MAX = 3.5
TYPING_DELAY_MIN = 1.0
TYPING_DELAY_MAX = 2.0
LOOP_WAIT_MIN = 600
LOOP_WAIT_MAX = 900

# ==============================================================================
# 5. ANTI-SPAM (防刷屏设置)
# ==============================================================================
# 如果开启，机器人会在喊话前检查最后一条消息是否是自己发的。
# If enabled, checks if the last message is sent by you before shouting out.
ENABLE_ANTI_SPAM = False

# 你的头像截图路径 (截取一个小方块即可，不要包含背景)
# Path to your avatar screenshot (crop tightly, no background)
MY_AVATAR_FILE = "assets/my_avatar.png"

# 检测区域阈值 (0.0 - 1.0)
# 只有当你的头像出现在屏幕下方 (例如 > 50% 高度) 时才判定为最新消息。
LAST_MSG_CHECK_HEIGHT = 0.5
