# test_task_b.py
import logging
import utils
import actions
import traceback
import config

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("TestTaskB")

def test_task_b():
    logger.info("=== Testing Task B: Share Profile (Search Group) ===")
    logger.info(f"Target Group: {config.TARGET_GROUP_NAME}")
    
    try:
        # 1. Connect
        utils.init_device_connection()
        utils.ensure_app_active()
        
        # 2. Run Task B
        actions.perform_task_b_share_profile()
        
        logger.info("=== Test Passed: Task B Completed Successfully ===")
        
    except Exception as e:
        logger.error(f"Test Failed: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    test_task_b()
