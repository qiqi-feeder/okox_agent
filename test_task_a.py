# test_task_a.py
import logging
import utils
import actions
import traceback

# Configure logging to see output clearly
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("TestTaskA")

def test_task_a():
    logger.info("=== Testing Task A: Group Chat Shout-out ===")
    
    try:
        # 1. Connect to Device
        utils.init_device_connection()
        utils.ensure_app_active()
        
        # 2. Run Task A
        actions.perform_task_a_shoutout()
        
        logger.info("=== Test Passed: Task A Completed Successfully ===")
        
    except Exception as e:
        logger.error(f"Test Failed: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    test_task_a()
