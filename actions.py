# actions.py
import time
import random
import logging
from airtest.core.api import *
import config
import utils 

logger = logging.getLogger("OKXBot")

def _shoutout_to_single_group(group_name):
    """
    Helper function: Send shout-out message to a single group.
    Assumes we are on the Planet Tab.
    
    Args:
        group_name: Name of the group to shout-out in
        
    Returns:
        True if shout-out was successful, False otherwise
    """
    logger.info(f"Shouting out in group: '{group_name}'")
    
    try:
        # 1. Use OCR to find and click the group
        logger.info(f"Using OCR to find group: '{group_name}'")
        max_scroll = getattr(config, 'OCR_MAX_SCROLL', 3)
        found = utils.ocr_click_text(group_name, max_scroll=max_scroll, scroll_direction="down")
        
        if not found:
            logger.warning(f"OCR could not find group '{group_name}'. Skipping.")
            return False
        
        # Wait for chat to load
        utils.random_sleep(2.0, 4.0)
        
        # 2. Anti-Spam Check
        if getattr(config, 'ENABLE_ANTI_SPAM', False):
            logger.info("Performing Anti-Spam Check...")
            if utils.check_last_message_is_mine(config.MY_AVATAR_FILE, getattr(config, 'LAST_MSG_CHECK_HEIGHT', 0.5)):
                logger.info(">>> SKIP: Last message is mine. <<<")
                utils.press_back()  # Exit Chat
                return True  # Not an error, just skipped
        
        # 3. Click Input Box
        utils.safe_click(config.CHAT_INPUT_X, config.CHAT_INPUT_Y, "Chat Input Box")
        utils.random_sleep(1.0, 2.0)
        
        # 4. Type Message
        msg = random.choice(config.MSG_POOL)
        utils.enter_text_safe(msg)
        
        # 5. Execute Send Logic
        logger.info("Tentative: Sending EDITOR_ACTION (Enter)...")
        keyevent("EDITOR_ACTION")
        utils.random_sleep(0.5, 1.0)
        
        # Click Send Button
        utils.safe_click(config.CHAT_SEND_X, config.CHAT_SEND_Y, "Send Button")
        utils.random_sleep(2.0, 3.0)
        
        # 6. Return to Planet
        logger.info("Exiting chat...")
        utils.press_back()  # Hide Keyboard
        utils.press_back()  # Exit Chat
        
        logger.info(f"Successfully sent message to '{group_name}'")
        return True
        
    except Exception as e:
        logger.error(f"Failed to shout-out in '{group_name}': {e}")
        # Try to recover
        utils.press_back()
        utils.press_back()
        return False


def perform_task_a_shoutout():
    """
    Task A: Group Chat Shout-out (Multi-Group Support)
    
    New Flow:
    1. Read all groups from 'groups.txt'
    2. For each group:
       a. Go to Planet Tab
       b. Use OCR to find the group name in message list and click it
       c. Check anti-spam (if enabled)
       d. Type & Send message
       e. Return to Planet
    3. Complete
    """
    logger.info("--- Starting Task A: Shout-out (Multi-Group Mode) ---")
    
    # 1. Get all groups from file
    groups = utils.get_all_groups_from_file("groups.txt")
    
    if not groups:
        # Fallback to single group fixed position
        logger.warning("No groups in groups.txt. Using fallback (Top 1).")
        utils.navigate_to_planet()
        utils.safe_click(config.GROUP_TOP1_X, config.GROUP_TOP1_Y, "Top 1 Group")
        utils.random_sleep(2.0, 4.0)
        
        # Perform single shout-out
        utils.safe_click(config.CHAT_INPUT_X, config.CHAT_INPUT_Y, "Chat Input Box")
        utils.random_sleep(1.0, 2.0)
        
        msg = random.choice(config.MSG_POOL)
        utils.enter_text_safe(msg)
        
        keyevent("EDITOR_ACTION")
        utils.random_sleep(0.5, 1.0)
        
        utils.safe_click(config.CHAT_SEND_X, config.CHAT_SEND_Y, "Send Button")
        utils.random_sleep(2.0, 3.0)
        
        utils.press_back()
        utils.press_back()
        
        logger.info("--- Task A Complete (Fallback Mode) ---")
        return
    
    logger.info(f"Will shout-out in {len(groups)} group(s): {groups}")
    
    # 2. Loop through each group
    for i, group_name in enumerate(groups):
        logger.info(f"[{i+1}/{len(groups)}] Processing group: '{group_name}'")
        
        # Navigate to Planet first
        utils.navigate_to_planet()
        
        # Shout-out in this group
        _shoutout_to_single_group(group_name)
        
        # Brief pause between groups
        if i < len(groups) - 1:
            logger.info("Waiting before next group...")
            utils.random_sleep(3.0, 5.0)
    
    logger.info("--- Task A Complete ---")

def _share_to_single_group(group_name):
    """
    Helper function: Share profile to a single group.
    Assumes we are already on the Profile page.
    
    Args:
        group_name: Name of the group to share to
        
    Returns:
        True if share was successful, False otherwise
    """
    logger.info(f"Sharing profile to group: '{group_name}'")
    
    try:
        # 1. Open Menu and Share
        logger.info("Opening More Menu...")
        utils.safe_click(config.PROFILE_MORE_X, config.PROFILE_MORE_Y, "More (...) Icon")
        utils.random_sleep(1.0, 2.0)
        
        logger.info("Clicking Share Profile...")
        utils.safe_click(config.PROFILE_MENU_SHARE_X, config.PROFILE_MENU_SHARE_Y, "Share Profile Option")
        utils.random_sleep(2.0, 3.0)
        
        logger.info("Selecting 'Chat' channel...")
        utils.safe_click(config.SHARE_TO_CHAT_X, config.SHARE_TO_CHAT_Y, "Share to Chat Icon")
        utils.random_sleep(2.0, 4.0)
        
        # 2. Search for Target Group
        logger.info(f"Searching for group: '{group_name}'")
        utils.safe_click(config.SHARE_SEARCH_X, config.SHARE_SEARCH_Y, "Search Input Box")
        utils.random_sleep(1.0, 1.5)
        
        # Input Name
        utils.enter_text_safe(group_name)
        utils.random_sleep(2.0, 3.0)
        
        # Click First Result
        logger.info("Selecting first search result...")
        utils.safe_click(config.SHARE_RESULT_1_X, config.SHARE_RESULT_1_Y, "First Search Result")
        utils.random_sleep(1.5, 2.5)
        
        # 3. Click Final Share/Send Button
        logger.info("Clicking Final Share Button...")
        utils.safe_click(config.SHARE_BOTTOM_BTN_X, config.SHARE_BOTTOM_BTN_Y, "Bottom Share Button")
        utils.random_sleep(3.0, 5.0)
        
        logger.info(f"Successfully shared to '{group_name}'")
        return True
        
    except Exception as e:
        logger.error(f"Failed to share to '{group_name}': {e}")
        return False


def perform_task_b_share_profile():
    """
    Task B: Share Profile Card (Multi-Group Support)
    
    New Flow:
    1. Read all groups from 'groups.txt'
    2. Navigate to Profile Page once
    3. For each group:
       a. Open Share menu -> Select Chat
       b. Search for group name -> Select -> Send
       c. (Stays on Profile page after share)
    4. Finally return to Planet
    """
    logger.info("--- Starting Task B: Share Profile (Multi-Group Mode) ---")
    
    # 1. Get all groups from file
    groups = utils.get_all_groups_from_file("groups.txt")
    
    if not groups:
        # Fallback to single group from config
        logger.warning("No groups in groups.txt. Using config.TARGET_GROUP_NAME as fallback.")
        groups = [config.TARGET_GROUP_NAME]
    
    logger.info(f"Will share to {len(groups)} group(s): {groups}")
    
    # 2. Navigate to Profile Page (ONCE at the beginning)
    utils.navigate_to_planet()
    logger.info("Navigating to Profile...")
    utils.safe_click(config.NAV_PROFILE_ICON_X, config.NAV_PROFILE_ICON_Y, "Profile Icon")
    utils.random_sleep(2.0, 3.0)
    
    # 3. Loop through each group (already on Profile page)
    for i, group_name in enumerate(groups):
        logger.info(f"[{i+1}/{len(groups)}] Processing group: '{group_name}'")
        
        # Share to this group (no need to navigate, already on Profile)
        _share_to_single_group(group_name)
        
        # Brief pause between shares
        if i < len(groups) - 1:
            logger.info("Waiting before next share...")
            utils.random_sleep(2.0, 4.0)
    
    # 4. Return to Planet
    logger.info("Returning to Planet (System Back)...")
    utils.press_back()
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
    
    # Settings
    MAX_SWIPES = 5
    IMAGE_PATH = r"assets/btn_follow.png"
    MATCH_THRESHOLD = getattr(config, 'FOLLOW_BTN_THRESHOLD', 0.9)
    
    # 3. Detection and Action Loop (Batch Processing)
    for page in range(MAX_SWIPES):
        logger.info(f"Scanning Page {page + 1}/{MAX_SWIPES}...")
        
        try:
            # Step 1: Scan ONCE (find_all returns list of dicts)
            matches = find_all(Template(IMAGE_PATH, threshold=MATCH_THRESHOLD))
            
            if not matches:
                logger.info("No 'Follow' buttons found on this page.")
            else:
                # Step 2: Deduplicate (Sort by Y, filter overlaps < 20px)
                matches.sort(key=lambda m: m['result'][1])
                unique_matches = []
                last_y = -999
                for match in matches:
                    curr_y = match['result'][1]
                    if abs(curr_y - last_y) > 20:
                        unique_matches.append(match)
                        last_y = curr_y
                
                logger.info(f"Found {len(matches)} raw -> {len(unique_matches)} unique buttons. Batch clicking...")
                
                # Step 3: Click ALL unique matches found on this screen
                for i, match in enumerate(unique_matches):
                    try:
                        pos = match['result']
                        logger.info(f"[{i+1}/{len(unique_matches)}] Clicking Follow at {pos}")
                        touch(pos)
                        
                        # Step 4: Short random sleep between clicks
                        # User Request: random.uniform(0.8, 1.5)
                        time.sleep(random.uniform(0.8, 1.5))
                        
                    except Exception as e:
                        logger.error(f"Failed to click match: {e}")
                        
        except TargetNotFoundError:
             logger.info("No targets found (TargetNotFoundError).")
        except Exception as e:
            logger.error(f"Error during detection loop: {e}")
        
        # Step 5: Scroll for next page
        logger.info("Scrolling down...")
        swipe((500, 1800), (500, 600))
        # Wait for scroll to settle
        time.sleep(2.0)
        
    # 5. End of Task C (Safe Exit & Reset)
    # User feedback: Might be deep in a profile page due to accidental clicks.
    # Action: Press Back slowly to exit any profile, then navigate to Planet.
    logger.info("Finishing Task C: Safe Exit Sequence...")
    for i in range(2): 
        utils.press_back()
        # Sleep > 2.0s to avoid "Press again to exit app" trigger
        time.sleep(3.0) 
    
    logger.info("Returning to Planet (Reset State)...")
    utils.navigate_to_planet()
    logger.info("--- Task C Complete ---")
