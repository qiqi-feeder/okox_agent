# utils.py
import time
import random
import logging
import os
from airtest.core.api import *
from airtest.core.error import *
import config

# Setup generic logger
logger = logging.getLogger("OKXBot")
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Optimize Logging: Suppress Airtest noise
logging.getLogger("airtest").setLevel(logging.WARNING)
logging.getLogger("airtest.core.api").setLevel(logging.WARNING)
logging.getLogger("airtest.core.android.adb").setLevel(logging.WARNING)

def init_device_connection():
    """Initializes the ADB connection to the Android device with Optimization settings."""
    try:
        # Construct optimized connection string
        # Format: android://127.0.0.1:5037/{DEVICE_ID}?cap_method=JAVACAP&ori_method=ADBORI&
        # 127.0.0.1:5037 is the default local ADB server
        
        device_id = config.DEVICE_SERIAL if config.DEVICE_SERIAL else ""
        connect_str = f"android://127.0.0.1:5037/{device_id}?cap_method=JAVACAP&ori_method=ADBORI&"
        
        logger.info(f"Connecting with optimized string: {connect_str}")
        connect_device(connect_str)
        
        # Ensure screen is on
        wake()
        logger.info("Device connected and screen awake.")
    except Exception as e:
        logger.error(f"Failed to connect to device: {e}")
        raise

def random_sleep(min_s=None, max_s=None):
    """
    Sleeps for a random duration to mimic human behavior.
    """
    if min_s is None: min_s = config.CLICK_DELAY_MIN
    if max_s is None: max_s = config.CLICK_DELAY_MAX
    
    duration = random.uniform(min_s, max_s)
    logger.debug(f"Sleeping for {duration:.2f}s")
    time.sleep(duration)

def safe_click(x, y, description="Unknown Element"):
    """
    Performs a touch action at specific coordinates.
    """
    try:
        logger.info(f"Clicking '{description}' at ({x}, {y})")
        touch((x, y))
        random_sleep()
    except Exception as e:
        logger.error(f"Failed to click '{description}': {e}")

def enter_text_safe(text_content):
    """
    Enters text using Airtest's native text() API.
    CRITICAL: enter=False to avoid default behaviors that might fail or delay.
    We rely on clicking the app's Send button afterwards.
    """
    try:
        logger.info(f"Typing: {text_content}")
        # enter=False prevents Airtest from sending KEYCODE_ENTER automatically
        # search=False prevents clicking the search button on keyboard
        text(text_content, enter=False)
        
        # Optional: Hide keyboard if needed, or just sleep
        # keyevent("BACK") # sometimes needed to see the send button if keyboard covers it
        
        random_sleep(config.TYPING_DELAY_MIN, config.TYPING_DELAY_MAX)
        
    except Exception as e:
        logger.error(f"Failed to enter text: {e}")

def ensure_app_active():
    """
    Brings the app to foreground or starts it.
    """
    try:
        start_app(config.PACKAGE_NAME)
        random_sleep(3.0, 5.0)
    except Exception as e:
        # Don't fail hard on start_app, just log
        logger.error(f"Failed to start app: {e}")

def navigate_to_planet():
    """
    Navigates to the 'Planet' (星球) Tab AND ensures list is at the top.
    Strategies:
    1. Click Planet Tab.
    2. Click it again (force refresh/scroll top).
    3. Swipe Down (drag from top down) to ensure list is at top.
    """
    logger.info("Navigating to Planet Tab (Resetting State)...")
    
    # 1. Click Tab
    safe_click(config.NAV_PLANET_X, config.NAV_PLANET_Y, "Bottom Nav - Planet")
    random_sleep(1.0, 2.0)
    
    # 2. (Removed Double Click) - User feedback says app doesn't support it.
    
    # 3. Swipe Down to Ensure List is at Top
    # To scroll UP (show top content), we drag DOWN (e.g., 500 -> 1500).
    logger.info("Resetting list position (Swipe Down)...")
    try:
        # Check if swipe is available (it is imported from airtest.core.api)
        swipe((500, 500), (500, 1500)) 
        random_sleep(1.5, 2.5)
    except Exception as e:
        logger.error(f"Swipe failed: {e}")

def press_back():
    """
    Simulates pressing the Android Hardware Back button.
    """
    try:
        logger.info("Action: Press Back")
        keyevent("BACK")
        random_sleep(1.0, 1.5)
    except Exception as e:
        logger.error(f"Failed to press back: {e}")

def get_random_group_from_file(file_path="groups.txt"):
    """
    Reads the group list from a file and returns a random group name.
    Returns None if file doesn't exist or is empty.
    """
    if not os.path.exists(file_path):
        logger.warning(f"Group file not found: {file_path}")
        return None
        
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip() and not line.startswith('#')]
            
        if not lines:
            logger.warning(f"Group file is empty: {file_path}")
            return None
            
        selected_group = random.choice(lines)
        logger.info(f"Selected target group: {selected_group}")
        return selected_group
    except Exception as e:
        logger.error(f"Failed to read group file: {e}")
        return None

def check_last_message_is_mine(avatar_path, height_threshold=0.5):
    """
    Checks if the last message in the chat is sent by the current user.
    It looks for the user's avatar in the lower portion of the screen.
    
    Args:
        avatar_path (str): Path to the avatar image file.
        height_threshold (float): 0.0 to 1.0. Only considers matches below this relative height.
                                  e.g., 0.5 means lower half of the screen.
    Returns:
        bool: True if last message is likely mine, False otherwise.
    """
    if not os.path.exists(avatar_path):
        logger.warning(f"Anti-spam check skipped: Avatar file not found at '{avatar_path}'")
        return False

    logger.info("Checking if last message is mine...")
    
    try:
        # Find all occurrences of the avatar on screen
        # Use a high threshold to avoid false positives
        matches = find_all(Template(avatar_path, threshold=0.85))
        
        if not matches:
            logger.info("No avatar matches found on screen.")
            return False
            
        # Get screen height
        screen_height = G.DEVICE.display_info['height']
        threshold_y = screen_height * height_threshold
        
        # Sort matches by Y coordinate (descending) -> lowest on screen first
        # match['result'] is (x, y) center point
        sorted_matches = sorted(matches, key=lambda m: m['result'][1], reverse=True)
        
        most_recent_match = sorted_matches[0]
        match_y = most_recent_match['result'][1]
        
        logger.info(f"Found avatar at Y={match_y} (Threshold > {threshold_y})")
        
        if match_y > threshold_y:
            return True
        else:
            logger.info("Avatar found, but not at the bottom (old message).")
            return False
            
    except TargetNotFoundError:
        logger.info("Avatar not found on screen.")
        return False
    except Exception as e:
        logger.error(f"Error during anti-spam check: {e}")
        return False
