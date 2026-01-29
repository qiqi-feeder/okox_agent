# main.py
import time
import random
import logging
import traceback
import utils
import config
import actions
from airtest.core.api import *

# Setup logger
logger = logging.getLogger("OKXBot")

def run_cycle():
    """
    Executes one full cycle of tasks.
    """
    logger.info(">>> Starting New Cycle <<<")
    
    # Fixed Sequence as per User Request:
    # 1. Share Profile (Task B)
    # 2. Shout-out (Task A)
    # 3. Follow Back (Task C)
    task_list = [
        actions.perform_task_b_share_profile,
        actions.perform_task_a_shoutout,
        actions.perform_task_c_follow_back
    ]
    # random.shuffle(task_list) # Disabled shuffle for fixed sequence
    
    for task_func in task_list:
        try:
            task_func()
            # Random sleep between tasks within the cycle
            utils.random_sleep(5.0, 10.0)
        except Exception as e:
            logger.error(f"Error during task execution: {e}")
            traceback.print_exc()
            # Try to recover to 'Planet' tab
            utils.navigate_to_planet()

    logger.info(">>> Cycle Complete <<<")

def main():
    logger.info("Initializing OKX Community Bot...")
    
    # 1. Connect to Device (Using optimized string in utils)
    try:
        utils.init_device_connection()
        utils.ensure_app_active()
    except Exception as e:
        logger.critical(f"Initialization Failed: {e}")
        return

    # 2. Main Loop
    cycle_count = 0
    while True:
        cycle_count += 1
        logger.info(f"=== Cycle #{cycle_count} ===")
        
        try:
            run_cycle()
        except Exception as e:
            logger.error(f"Critical Error in Cycle: {e}")
            traceback.print_exc()
            utils.navigate_to_planet()
        
        # 3. Sleep for Next Cycle
        wait_seconds = random.uniform(config.LOOP_WAIT_MIN, config.LOOP_WAIT_MAX)
        wait_minutes = wait_seconds / 60
        logger.info(f"Sleeping for {wait_minutes:.2f} minutes ({wait_seconds:.0f}s)...")
        time.sleep(wait_seconds)

if __name__ == "__main__":
    main()
