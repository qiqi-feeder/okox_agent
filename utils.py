# utils.py
import time
import random
import logging
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
    
    # 2. Click again to ensure we are focused / trigger scroll-to-top
    safe_click(config.NAV_PLANET_X, config.NAV_PLANET_Y, "Bottom Nav - Planet (Retry)")
    random_sleep(1.0, 1.5)
    
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
