# test_task_c.py
import logging
import utils
import actions
import traceback

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("TestTaskC")

def test_task_c():
    logger.info("=== Testing Task C: Follow Back (Image Based) ===")
    logger.info("Prerequisite: Ensure 'assets/btn_follow.png' exists and screen is unlocked.")
    
    try:
        # 1. Connect
        utils.init_device_connection()
        utils.ensure_app_active()
        
        # 2. Run Task C
        # Logic: Planet -> Profile Icon -> Fans List -> Image Scan & Click
        actions.perform_task_c_follow_back()
        
        logger.info("=== Test Passed: Task C Completed Successfully ===")
        
    except Exception as e:
        logger.error(f"Test Failed: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    test_task_c()
