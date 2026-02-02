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
    Task A: Group Chat Shout-out (Dynamic Group Support)
    1. Go to Planet Tab
    2. Read 'groups.txt' to get a target group
    3. If group found: Search -> Enter
       If no group/file: Click Top 1 (Fallback)
    4. Anti-Spam Check
    5. Type & Send
    6. Return to Planet
    """
    logger.info("--- Starting Task A: Shout-out ---")
    
    # 1. Go to Planet Tab
    utils.navigate_to_planet()
    
    # 2. Determine Target Group
    target_group = utils.get_random_group_from_file("groups.txt")
    
    entered_via_search = False
    
    if target_group:
        logger.info(f"Mode: Multi-Group Search | Target: {target_group}")
        # Search Flow
        # Click Search Icon
        utils.safe_click(config.PLANET_SEARCH_ICON_X, config.PLANET_SEARCH_ICON_Y, "Planet Search Icon")
        utils.random_sleep(1.0, 2.0)
        
        # Click Input (if needed) and Type
        utils.safe_click(config.PLANET_SEARCH_INPUT_X, config.PLANET_SEARCH_INPUT_Y, "Search Input")
        utils.enter_text_safe(target_group)
        utils.random_sleep(2.0, 3.0)
        
        # Click Result
        utils.safe_click(config.PLANET_SEARCH_RESULT_X, config.PLANET_SEARCH_RESULT_Y, "Search Result")
        utils.random_sleep(2.0, 4.0) # Wait for chat to load
        entered_via_search = True
        
    else:
        logger.info("Mode: Single Fixed Group (Top 1)")
        # Fallback: Click Top 1 Group (Pinned)
        utils.safe_click(config.GROUP_TOP1_X, config.GROUP_TOP1_Y, "Top 1 Group")
        utils.random_sleep(2.0, 4.0)
    
    # [NEW] Anti-Spam Check
    # Checks if the last message is sent by me. If so, skips sending.
    if getattr(config, 'ENABLE_ANTI_SPAM', False):
        logger.info("Performing Anti-Spam Check...")
        if utils.check_last_message_is_mine(config.MY_AVATAR_FILE, getattr(config, 'LAST_MSG_CHECK_HEIGHT', 0.5)):
            logger.info(">>> SKIP: Last message is mine. Returning to Planet. <<<")
            utils.press_back() # Exit Chat
            if entered_via_search:
                utils.press_back() # Exit Search Page to Planet
            return
    
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
    logger.info("Exiting chat...")
    utils.press_back() # 1. Hide Keyboard
    utils.press_back() # 2. Exit Chat
    
    if entered_via_search:
         # If we entered via search, we are now back at the Search Results page
         # Need one more back to return to Planet Tab
         logger.info("Exiting Search Page...")
         utils.press_back() 
    
    logger.info("--- Task A Complete ---")

def perform_task_b_share_profile():
    """
    Task B: Share Profile Card (Refined Search Flow)
    1. Go to Planet Tab -> Profile
    2. Click More (...) -> Share Profile -> Chat
    3. Click Search -> Input Group Name -> Click Result
    4. Click Share/Send Button
    5. Return to Planet
    """
    logger.info("--- Starting Task B: Share Profile (Search Flow) ---")
    
    # 1. Go to Profile Page (via Planet Tab)
    utils.navigate_to_planet() 
    logger.info("Navigating to Profile...")
    utils.safe_click(config.NAV_PROFILE_ICON_X, config.NAV_PROFILE_ICON_Y, "Profile Icon")
    utils.random_sleep(2.0, 3.0)
    
    # 2. Open Menu and Share
    logger.info("Opening More Menu...")
    utils.safe_click(config.PROFILE_MORE_X, config.PROFILE_MORE_Y, "More (...) Icon")
    utils.random_sleep(1.0, 2.0)
    
    logger.info("Clicking Share Profile...")
    utils.safe_click(config.PROFILE_MENU_SHARE_X, config.PROFILE_MENU_SHARE_Y, "Share Profile Option")
    utils.random_sleep(2.0, 3.0)
    
    logger.info("Selecting 'Chat' channel...")
    utils.safe_click(config.SHARE_TO_CHAT_X, config.SHARE_TO_CHAT_Y, "Share to Chat Icon")
    utils.random_sleep(2.0, 4.0)
    
    # 3. Search for Target Group
    logger.info(f"Searching for group: {config.TARGET_GROUP_NAME}")
    # Click Search Box
    utils.safe_click(config.SHARE_SEARCH_X, config.SHARE_SEARCH_Y, "Search Input Box")
    utils.random_sleep(1.0, 1.5)
    
    # Input Name
    utils.enter_text_safe(config.TARGET_GROUP_NAME)
    # Give search results time to load
    utils.random_sleep(2.0, 3.0)
    
    # Click First Result
    logger.info("Selecting first search result...")
    utils.safe_click(config.SHARE_RESULT_1_X, config.SHARE_RESULT_1_Y, "First Search Result")
    utils.random_sleep(1.5, 2.5)
    
    # 4. Click Final Share/Send Button
    logger.info("Clicking Final Share Button...")
    utils.safe_click(config.SHARE_BOTTOM_BTN_X, config.SHARE_BOTTOM_BTN_Y, "Bottom Share Button")
    utils.random_sleep(3.0, 5.0)
    
    # 5. Return to Planet
    # User feedback: No "Planet" button on Profile page. Use System Back.
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
    MATCH_THRESHOLD = 0.9 
    
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
