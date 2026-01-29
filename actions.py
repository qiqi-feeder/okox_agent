# actions.py
import time
import random
import logging
from airtest.core.api import *
import config
import utils

logger = logging.getLogger("OKXBot")

def perform_task_a_shoutout():
    """
    Task A: Group Chat Shout-out
    1. Go to Planet Tab
    2. Click Top 1 Group
    3. Type random message
    4. Send (Double Safety)
    5. Return to Planet (Double Back)
    """
    logger.info("--- Starting Task A: Shout-out ---")
    
    # 1. Go to Planet Tab
    utils.navigate_to_planet()
    
    # 2. Click Top 1 Group (Pinned)
    utils.safe_click(config.GROUP_TOP1_X, config.GROUP_TOP1_Y, "Top 1 Group")
    utils.random_sleep(2.0, 4.0)
    
    # 3. Click Input Box
    utils.safe_click(config.CHAT_INPUT_X, config.CHAT_INPUT_Y, "Chat Input Box")
    utils.random_sleep(1.0, 2.0)
    
    # 4. Type Message
    msg = random.choice(config.MSG_POOL)
    utils.enter_text_safe(msg)
    
    # 5. Execute Send Logic (Robust Strategy)
    # Attempt 1: Send 'Enter'/'Action' event via ADB
    logger.info("Tentative: Sending EDITOR_ACTION (Enter)...")
    keyevent("EDITOR_ACTION")
    utils.random_sleep(0.5, 1.0)
    
    # Attempt 2: Click the Send Button Coordinate
    utils.safe_click(config.CHAT_SEND_X, config.CHAT_SEND_Y, "Send Button")
    utils.random_sleep(2.0, 3.0)
    
    # 6. Return to Planet (Exit Chat Logic)
    # User Request: Back twice (1st: Hide Input, 2nd: Exit Chat)
    logger.info("Exiting chat (Double Back Strategy)...")
    utils.press_back() # 1. Hide Keyboard
    utils.press_back() # 2. Exit Chat to Planet List
    
    logger.info("--- Task A Complete ---")

def perform_task_b_share_profile():
    """
    Task B: Share Profile Card
    """
    logger.info("--- Starting Task B: Share Profile ---")
    
    # 1. Go to Profile Page (via Planet Tab)
    utils.navigate_to_planet() 
    logger.info("Navigating to Profile...")
    utils.safe_click(config.NAV_PROFILE_ICON_X, config.NAV_PROFILE_ICON_Y, "Profile Icon")
    utils.random_sleep(2.0, 3.0)
    
    # 2. Click Share Icon
    utils.safe_click(config.PROFILE_SHARE_X, config.PROFILE_SHARE_Y, "Share Icon")
    utils.random_sleep(2.0, 4.0)
    
    # 3. Select Target Group (First in Recent)
    utils.safe_click(config.SHARE_RECENT_1_X, config.SHARE_RECENT_1_Y, "Recent Contact 1")
    utils.random_sleep(1.5, 2.5)
    
    # 4. Confirm Send (if needed)
    utils.safe_click(config.SHARE_CONFIRM_X, config.SHARE_CONFIRM_Y, "Confirm Share")
    utils.random_sleep(2.0, 3.0)
    
    # 5. Return to Planet
    utils.navigate_to_planet()
    logger.info("--- Task B Complete ---")

def perform_task_c_follow_back():
    """
    Task C: Follow Back (Mutual Follow) - Image Based Implementation
    Requirement: Verify 'Follow' button is BLACK (threshold=0.9) to avoid Unfollowing.
    """
    logger.info("--- Starting Task C: Follow Back (Image Based) ---")
    
    # 1. Go to Profile (via Planet Tab)
    utils.navigate_to_planet()
    logger.info("Navigating to Profile...")
    utils.safe_click(config.NAV_PROFILE_ICON_X, config.NAV_PROFILE_ICON_Y, "Profile Icon")
    utils.random_sleep(2.0, 3.0)
    
    # 2. Go to Followers List
    utils.safe_click(config.PROFILE_FANS_LIST_X, config.PROFILE_FANS_LIST_Y, "Fans/Followers List")
    utils.random_sleep(3.0, 5.0) # Wait for list to load
    
    # settings
    MAX_SWIPES = 5
    IMAGE_PATH = r"assets/btn_follow.png"
    MATCH_THRESHOLD = 0.9 
    
    total_followed = 0
    
    # 3. Detection and Action Loop
    for page in range(MAX_SWIPES):
        logger.info(f"Scanning Page {page + 1}/{MAX_SWIPES}...")
        
        # Inner loop: Keep finding and clicking buttons ONE BY ONE on the current screen
        # This prevents stale coordinates if layout shifts or state changes.
        follow_found_on_page = True
        while follow_found_on_page:
            try:
                # Limit check
                if total_followed >= 3:
                    logger.info("Test Limit Reached (Max 3). Stopping Task C.")
                    break
                
                # Look for ONE target
                pos = exists(Template(IMAGE_PATH, threshold=MATCH_THRESHOLD))
                
                if pos:
                    logger.info(f"Found Follow Button at {pos}")
                    touch(pos)
                    total_followed += 1
                    
                    # Wait for UI to update (Button turns gray/white)
                    # This is CRITICAL: Ensure the clicked button no longer matches 'Black' before scanning again
                    utils.random_sleep(2.0, 3.0) 
                else:
                    logger.info("No more 'Follow' buttons found on this page.")
                    follow_found_on_page = False
                    
            except Exception as e:
                logger.error(f"Error during click loop: {e}")
                follow_found_on_page = False

        if total_followed >= 3:
            break
        
        # 4. Scroll for next page
        logger.info("Scrolling down...")
        swipe((500, 1800), (500, 600))
        time.sleep(2.0)
        
    # 5. End of Task C
    logger.info("--- Task C Complete ---")
