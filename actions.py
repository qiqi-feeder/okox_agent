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
    
    # Settings for Image Matching
    MAX_SWIPES = 5
    IMAGE_PATH = r"assets/btn_follow.png"
    MATCH_THRESHOLD = 0.9 # High threshold to distinguish Black vs Gray/White buttons
    
    # 3. Detection and Action Loop
    for page in range(MAX_SWIPES):
        logger.info(f"Scanning Page {page + 1}/{MAX_SWIPES}...")
        
        try:
            # find_all returns a list of coordinates for all matches
            # using record_pos=None to avoid clogging logs/reports if not needed
            matches = find_all(Template(IMAGE_PATH, threshold=MATCH_THRESHOLD))
            
            if not matches:
                logger.info("No 'Follow' buttons found on this page.")
            else:
                logger.info(f"Found {len(matches)} potential buttons. Limiting to first 3 for testing.")
                
                # Limit to first 3 matches only
                limited_matches = matches[:3]
                
                # Perform clicks
                for match in limited_matches:
                    try:
                        # CRITICAL FIX: find_all returns a dict, e.g. {'result': (x,y), ...}
                        # We must extract the coordinate tuple from 'result' key.
                        click_pos = match['result']
                        logger.info(f"Clicking Follow Button at {click_pos}")
                        touch(click_pos)
                        # Random sleep after each follow
                        utils.random_sleep(1.0, 2.0)
                    except Exception as e:
                        logger.error(f"Failed to click match: {e}")
                
                # For testing purposes, we stop after processing the first valid page/batch
                logger.info("Test Limit Reached (Max 3). Stopping Task C.")
                break
                        
        except TargetNotFoundError:
             logger.info("No targets found (TargetNotFoundError).")
        except Exception as e:
            logger.error(f"Error during detection loop: {e}")
        
        # 4. Scroll for next page (Only if we didn't break above)
        logger.info("Scrolling down...")
        swipe((500, 1800), (500, 600))
        time.sleep(2.0)
        
    # 5. Return to Planet
    utils.navigate_to_planet()
    logger.info("--- Task C Complete ---")
