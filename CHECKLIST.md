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
-   [x] **CHAT_SEND_X, CHAT_SEND_Y**: 请点击输入框右侧（或上方）的 **APP自带发送图标**。

### 3. 任务 B: 分享名片 (Task B: Share Profile - New Search Flow)
-   **目标群名**: 在 `config.py` 中设置 `TARGET_GROUP_NAME` 为您想分享的群全名。
-   *步骤 1：主页更多选项*
    -   [ ] **PROFILE_MORE_X, PROFILE_MORE_Y**: 个人主页右上角的 **"..." (三个点)** 图标。
-   *步骤 2：弹出菜单*
    -   [ ] **PROFILE_MENU_SHARE_X, PROFILE_MENU_SHARE_Y**: 菜单中的 **"分享主页"** 选项。
-   *步骤 3：分享渠道*
    -   [ ] **SHARE_TO_CHAT_X, SHARE_TO_CHAT_Y**: 分享面板中的 **"聊天 (Chat)"** 图标。 (不是复制链接，是分享到OKX内部聊天)
-   *步骤 4：搜索与选择*
    -   [ ] **SHARE_SEARCH_X, SHARE_SEARCH_Y**: 联系人选择页顶部的 **搜索输入框**。
    -   *（机器人会输入群名）*
    -   [ ] **SHARE_RESULT_1_X, SHARE_RESULT_1_Y**: 搜索结果列表出来的 **第1个结果**。
    -   [ ] **SHARE_BOTTOM_BTN_X, SHARE_BOTTOM_BTN_Y**: 屏幕最底部的 **"发送/确定"** 蓝色大按钮。

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

### 6. (可选) 防刷屏设置 (Anti-Spam Settings)
如果您希望在上一条消息是自己发的时候跳过喊话：
1.  **截图**: 截取一张您自己在聊天中的头像（越清晰越好，不带背景）。
2.  **保存**: 将图片命名为 `my_avatar.png` 并保存在 `assets/` 文件夹下。
3.  **配置**: 在 `config.py` 中设置 `ENABLE_ANTI_SPAM = True`。
