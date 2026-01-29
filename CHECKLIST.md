# OKX 社区机器人配置清单 (Configuration Checklist)

**【重要更新】：** 所有功能都基于底部的 **"星球 (Planet)"** 板块。
请仔细测量该页面的坐标。

本机器人依赖 **坐标点击 (Coordinates)**。因此，您必须手动测量并在配置文件中填写适合您手机的 X, Y 坐标值。

## 如何测量坐标 (How to Measure Coordinates)
1.  在 Android 手机上，进入 **设置 > 开发者选项 (Settings > Developer Options)**。
2.  开启 **指针位置 (Pointer Location)** (开启后屏幕上方会显示当前触摸的 X, Y 坐标)。
3.  打开 OKX App。
4.  导航到下方列出的界面，点击对应的按钮，并记下屏幕上方显示的 `X` 和 `Y` 值。

## 需要编辑的文件: `d:/workspace/okox_agent/config.py`

### 1. 全局导航 - "星球" (Global Navigation - Planet Tab)
-   [x] **NAV_PLANET_X, NAV_PLANET_Y**: 点击底部的 **"星球"** 图标 (这是核心入口)。
-   [x] **NAV_PROFILE_ICON_X, NAV_PROFILE_ICON_Y**: **先点击"星球"进入该页面后**，再点击您的 **头像图标**。

### 2. 任务 A: 群聊喊话 (Task A: Group Chat Shout-out)
-   *首先点击 "星球" (Planet) Tab。*
-   [x] **GROUP_TOP1_X, GROUP_TOP1_Y**: 点击消息列表中 **置顶的第1个群组**。
-   *进入群聊界面后:*
-   [x] **CHAT_INPUT_X, CHAT_INPUT_Y**: 点击底部的 **文本输入框**。
-   [ ] **CHAT_SEND_X, CHAT_SEND_Y**: **关键点**: 不是键盘上的回车(键盘会被隐藏)。请点击输入框右侧（或上方）的 **APP自带发送图标** (通常是纸飞机或箭头)。

### 3. 任务 B: 分享名片 (Task B: Share Profile)
-   *首先点击 "星球" (Planet) Tab -> 再点击头像。*
-   [ ] **PROFILE_SHARE_X, PROFILE_SHARE_Y**: 点击右上角的 **分享图标**。
-   *等待分享面板弹出:*
-   [ ] **SHARE_RECENT_1_X, SHARE_RECENT_1_Y**: 点击 "最近 (Recent)" 分享列表中的 **第1个头像/群组**。
-   [ ] **SHARE_CONFIRM_X, SHARE_CONFIRM_Y**: 如果出现 "确认发送" 弹窗，点击确认按钮。

### 4. 任务 C: 粉丝回关 (Task C: Follow Back)
-   *首先点击 "星球" (Planet) Tab -> 再点击头像。*
-   [ ] **PROFILE_FANS_LIST_X, PROFILE_FANS_LIST_Y**: 点击 "粉丝 (Fans/Followers)" 数量，进入粉丝列表页面。
-   *在粉丝列表页面:*
-   [ ] **FOLLOW_BTN_X**: 观察 "回关/关注" 按钮的水平位置，记录其 **X 坐标**。
-   [ ] **FOLLOW_BTN_Y_START**: 记录列表中 **第1个** 可见按钮的 **Y 坐标**。
-   [ ] **FOLLOW_BTN_Y_END**: 记录列表中 **最后1个** 可见按钮的 **Y 坐标**。

### 5. 其他设置 (Other Settings)
-   [ ] **MSG_POOL**: 在 `config.py` 中编辑您的喊话内容列表。
-   [ ] **DEVICE_SERIAL**: 如果您连接了多台设备，请运行 `adb devices` 获取序列号并填入。

## 如何运行 (How to Run)
1.  打开命令提示符 (cmd)。
2.  进入项目目录: `cd d:/workspace/okox_agent`
3.  运行脚本: `python main.py`
