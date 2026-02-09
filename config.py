# config.py
# OKX 社区机器人配置文件 (Configuration for OKX Community Bot)
# 用户必须根据自己的设备分辨率填写 X,Y 坐标。
# (User MUST populate the X,Y coordinates suitable for their device resolution.)

# ==============================================================================
# 1. ADB & DEVICE SETTINGS (ADB 与设备设置)
# ==============================================================================
# 可选: 如果连接了多个设备，请指定设备序列号 (例如 "127.0.0.1:5555")
# (Optional: Specific device serial if multiple devices connected)
DEVICE_SERIAL = None 

# OKX App 的包名 (请检查是否与您所在地区的版本匹配)
# (Package Name for OKX App)
PACKAGE_NAME = "com.okinc.okex.gp"

# ==============================================================================
# 2. COORDINATES (X, Y) - CRITICAL FOR FLAG_SECURE SCREENS
# 关键设置: 坐标 (X, Y) - 用于绕过 Flag_Secure 黑屏限制
# ==============================================================================
# 使用说明 (INSTRUCTIONS):
# 1. 在 Android 开发者选项中开启 "指针位置" (Pointer Location)。
# 2. 点击屏幕，记录下方按钮的 X, Y 值。
# (Enable "Pointer Location" in Developer Options. Tap screen to find X, Y.)

# --- Global Navigation (全局导航) ---
# 底部导航栏 - "星球" Tab (Planet Tab) 
# *** 核心入口: 所有功能都在此页面 ***
NAV_PLANET_X, NAV_PLANET_Y = 854, 2578 

# 用户个人主页图标 (User Profile Icon)
# 必须先点击 "星球" Tab 才能看到此图标
NAV_PROFILE_ICON_X, NAV_PROFILE_ICON_Y = 162, 269 

# 返回按钮 (左上角) - 如果需要软返回键 (Back Button)
NAV_BACK_X, NAV_BACK_Y = 143, 213

# --- Task A: Group Chat Shout-out (任务 A: 群聊喊话) ---
# 1. 星球页面/消息列表中的置顶群组 (第1个) (Target Group - Pinned #1)
GROUP_TOP1_X, GROUP_TOP1_Y = 634, 985

# 2. 聊天界面的输入框 (Input Box)
CHAT_INPUT_X, CHAT_INPUT_Y = 575, 2550

# 3. 发送按钮 (Send Button)
# 【重要说明】: 由于 Yosemite 输入法会隐藏键盘，无法使用键盘上的回车发送。
# 必须使用 OKX 界面上输入框右侧的 "发送" 图标/箭头/纸飞机。
# (MUST be the App's UI Send Icon, NOT keyboard button, as keyboard is hidden.)
CHAT_SEND_X, CHAT_SEND_Y = 1110, 2555

# --- Task B: Share Profile Card (任务 B: 分享名片) ---
# 目标群组名称 (精确匹配) - 用于搜索
TARGET_GROUP_NAME = "MyTargetGroup" 

# 1. 个人主页右上角的 "..." (更多) 图标 (Three Dots / More)
PROFILE_MORE_X, PROFILE_MORE_Y = 980, 150

# 2. 弹出菜单中的 "分享主页" 选项 (Share Profile Option)
PROFILE_MENU_SHARE_X, PROFILE_MENU_SHARE_Y = 500, 1800 

# 3. 分享列表中的 "聊天" 图标 (Share to Chat)
SHARE_TO_CHAT_X, SHARE_TO_CHAT_Y = 500, 1500

# 4. 联系人选择页面的 "搜索" 输入框 (Search Input)
SHARE_SEARCH_X, SHARE_SEARCH_Y = 500, 300

# 5. 搜索结果列表中的 "第1项" (First Result)
SHARE_RESULT_1_X, SHARE_RESULT_1_Y = 500, 600

# 6. 底部的 "发送/分享" 确认按钮 (Bottom Send/Share Button)
SHARE_BOTTOM_BTN_X, SHARE_BOTTOM_BTN_Y = 800, 2500

# --- Task C: Follow Back (任务 C: 粉丝回关) ---
# 1. 个人主页的 "粉丝/关注者" 列表入口 (Fans/Followers list)
PROFILE_FANS_LIST_X, PROFILE_FANS_LIST_Y = 350, 650

# 2. 关注按钮扫描区域 (Follow Button Scan Area)
# 关注按钮的水平 X 坐标 (X-coordinate for Follow button)
FOLLOW_BTN_X = 900
# 扫描起始 Y 坐标 (Y-coordinate start)
FOLLOW_BTN_Y_START = 500
# 扫描结束 Y 坐标 (Y-coordinate end)
FOLLOW_BTN_Y_END = 1800
# 列表项之间的间距 (步长) (Distance between items)
FOLLOW_BTN_STEP = 250 

# ==============================================================================
# 3. TEXT POOL (SHOUT-OUT MESSAGES) (喊话话术池)
# ==============================================================================
# Constraint: NO English single quotes (') or special shell chars.
# Chinese works best with Airtest Yosemite input.
MSG_POOL = [
    "互关互关",           # Mutual follow
    "必回关",             # Must follow back
    "一起发财",           # Get rich together
    # "Follow for follow",  # Safe English
    # "Lets grow together", # Safe English (No apostrophe)
    # "F4F anyone",
    # "Active trader here",
]

# ==============================================================================
# 4. TIMING & SCHEDULER (SECONDS) (时间设置 - 秒)
# ==============================================================================
# 点击之间的随机延迟 (最小值, 最大值) (Delay between clicks)
CLICK_DELAY_MIN = 1.5
CLICK_DELAY_MAX = 3.5

# 输入文本后的延迟 (Delay for typing)
TYPING_DELAY_MIN = 1.0
TYPING_DELAY_MAX = 2.0

# 主循环等待时间 (15 到 30 分钟) (Main Loop Wait Time) - Updated as per user request
LOOP_WAIT_MIN = 900  # 15 mins
LOOP_WAIT_MAX = 1800 # 30 mins

# ==============================================================================
# 5. OCR SETTINGS (OCR 设置 - PaddleOCR)
# ==============================================================================
# 最大滑动次数（在消息列表中查找群组时）
# Maximum scroll attempts when searching for group in message list
OCR_MAX_SCROLL = 5
