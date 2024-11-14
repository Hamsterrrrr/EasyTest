import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    APP_PACKAGE = os.getenv("APP_PACKAGE")
    APP_ACTIVITY = os.getenv("APP_ACTIVITY")
    PLATFORM_NAME = os.getenv("PLATFORM_NAME", "Android")
    DEVICE_NAME = os.getenv("DEVICE_NAME", "emulator-5554")
    APPIUM_SERVER_URL = os.getenv("APPIUM_SERVER_URL", "http://localhost:4723/wd/hub")
