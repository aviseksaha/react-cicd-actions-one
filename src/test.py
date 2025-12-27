from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

import time
import subprocess
from datetime import datetime

# Global variable to hold the Appium session
appium_driver = None


def appium_start():
    global appium_driver

    if appium_driver is None:
        cap: Dict[str, Any] = {
            'platformName': 'Android',
            'automationName': 'uiautomator2',
            'newCommandTimeout': 500
        }
        # cap: Dict[str, Any] = {
        #     'platformName': 'Android',
        #     'automationName': 'uiautomator2',
        #     'appium:appPackage': 'com.lohjason.genericbatterydrainer',
        #     'appium:appActivity': '.ui.MainActivity',
        #     'appium:noReset': True
        # }
        url = 'http://127.0.0.1:4723'
        print("Starting Appium session...")
        appium_driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
        print("Appium session started:", appium_driver)
    else:
        print("Appium session already started:", appium_driver)

    return appium_driver


def verify_all_toggle_off():
    toggle_switches = {
        "switch_screen": "SCREEN",
        "switch_flash": "FLASH",
        "switch_gps": "GPS",
        "switch_wifi": "WiFi",
        "switch_bluetooth": "Bluetooth",
        "switch_cpu": "CPU",
        "switch_gpu": "GPU",
    }

    for switch_id, switch_name in toggle_switches.items():
        try:
            element = appium_driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                                 value=f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("com.lohjason.genericbatterydrainer:id/{switch_id}"))')
            if element.get_attribute("text") != "OFF":
                print(f"Turning off {switch_name}")
                element.click()
        except Exception as e:
            print(f"Error processing {switch_name}: {e}")

    # Check start button
    try:
        start_button = appium_driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                                  value='new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("com.lohjason.genericbatterydrainer:id/tv_start"))')
        if start_button.get_attribute("text") != "Start":
            print("Resetting Start button")
            start_button.click()
    except Exception as e:
        print(f"Error checking Start button: {e}")


def gps_use():
    try:
        # print("started test_gps_use")
        subprocess.check_output("adb shell am start -n com.lohjason.genericbatterydrainer/.ui.MainActivity", shell=True)
        time.sleep(5)

        gps_toggle = appium_driver.find_element(
            by=AppiumBy.ANDROID_UIAUTOMATOR,
            value='new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("com.lohjason.genericbatterydrainer:id/switch_gps"))'
        )
        start_button = appium_driver.find_element(
            by=AppiumBy.ANDROID_UIAUTOMATOR,
            value='new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("com.lohjason.genericbatterydrainer:id/tv_start"))'
        )

        verify_all_toggle_off()

        # print("enabling gps toggle")
        gps_toggle.click()
        time.sleep(2)

        # print("start gps test")
        start_button.click()
        time.sleep(300)  # 5-minute test duration

        # print("stop gps test")
        start_button.click()

        # print("disabling gps toggle")
        gps_toggle.click()

        battery_str = appium_driver.find_element(
            by=AppiumBy.ANDROID_UIAUTOMATOR,
            value='new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("com.lohjason.genericbatterydrainer:id/tv_battery_percentage"))'
        ).text
        battery = float(battery_str.strip('%'))
        print(f"Battery after gps test: {battery}%")

        subprocess.check_output("adb shell am force-stop com.lohjason.genericbatterydrainer", shell=True)
        return battery
    except Exception as e:
        print("Error in test_gps_use:", e)
        return None


def wifi_use():
    try:
        # print("started test_wifi_use")
        subprocess.check_output("adb shell am start -n com.lohjason.genericbatterydrainer/.ui.MainActivity", shell=True)
        time.sleep(5)

        wifi_toggle = appium_driver.find_element(
            by=AppiumBy.ANDROID_UIAUTOMATOR,
            value='new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("com.lohjason.genericbatterydrainer:id/switch_wifi"))'
        )
        start_button = appium_driver.find_element(
            by=AppiumBy.ANDROID_UIAUTOMATOR,
            value='new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("com.lohjason.genericbatterydrainer:id/tv_start"))'
        )

        verify_all_toggle_off()

        # print("enabling wifi toggle")
        wifi_toggle.click()
        time.sleep(2)

        # print("start wifi test")
        start_button.click()
        time.sleep(300)  # 5-minute test duration

        # print("stop wifi test")
        start_button.click()

        # print("disabling wifi toggle")
        wifi_toggle.click()

        battery_str = appium_driver.find_element(
            by=AppiumBy.ANDROID_UIAUTOMATOR,
            value='new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("com.lohjason.genericbatterydrainer:id/tv_battery_percentage"))'
        ).text
        battery = float(battery_str.strip('%'))
        print(f"Battery after wifi test: {battery}%")

        subprocess.check_output("adb shell am force-stop com.lohjason.genericbatterydrainer", shell=True)
        return battery
    except Exception as e:
        print("Error in test_wifi_use:", e)
        return None


def bt_use():
    try:
        # print("started test_bt_use")
        subprocess.check_output("adb shell am start -n com.lohjason.genericbatterydrainer/.ui.MainActivity", shell=True)
        time.sleep(5)

        bt_toggle = appium_driver.find_element(
            by=AppiumBy.ANDROID_UIAUTOMATOR,
            value='new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("com.lohjason.genericbatterydrainer:id/switch_bluetooth"))'
        )

        start_button = appium_driver.find_element(
            by=AppiumBy.ANDROID_UIAUTOMATOR,
            value='new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("com.lohjason.genericbatterydrainer:id/tv_start"))'
        )

        verify_all_toggle_off()

        # print("enabling bt toggle")
        bt_toggle.click()
        time.sleep(2)

        # print("start bt test")
        start_button.click()
        time.sleep(300)  # 5-minute test duration

        # print("stop bt test")
        start_button.click()

        # print("disabling bt toggle")
        bt_toggle.click()

        battery_str = appium_driver.find_element(
            by=AppiumBy.ANDROID_UIAUTOMATOR,
            value='new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("com.lohjason.genericbatterydrainer:id/tv_battery_percentage"))'
        ).text
        battery = float(battery_str.strip('%'))
        print(f"Battery after BT test: {battery}%")

        subprocess.check_output("adb shell am force-stop com.lohjason.genericbatterydrainer", shell=True)
        return battery
    except Exception as e:
        print("Error in test_bt_use:", e)
        return None


def cpu_gpu_use():
    try:
        # print("started test_bt_use")
        subprocess.check_output("adb shell am start -n com.lohjason.genericbatterydrainer/.ui.MainActivity", shell=True)
        time.sleep(5)

        cpu_toggle = appium_driver.find_element(
            by=AppiumBy.ANDROID_UIAUTOMATOR,
            value='new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("com.lohjason.genericbatterydrainer:id/switch_cpu"))'
        )
        gpu_toggle = appium_driver.find_element(
            by=AppiumBy.ANDROID_UIAUTOMATOR,
            value='new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("com.lohjason.genericbatterydrainer:id/switch_gpu"))'
        )
        start_button = appium_driver.find_element(
            by=AppiumBy.ANDROID_UIAUTOMATOR,
            value='new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("com.lohjason.genericbatterydrainer:id/tv_start"))'
        )

        verify_all_toggle_off()

        cpu_toggle.click()
        time.sleep(2)

        gpu_toggle.click()
        time.sleep(2)

        # print("start bt test")
        start_button.click()
        time.sleep(300)  # 5-minute test duration

        # print("stop bt test")
        start_button.click()

        cpu_toggle.click()
        time.sleep(2)

        gpu_toggle.click()
        time.sleep(2)

        battery_str = appium_driver.find_element(
            by=AppiumBy.ANDROID_UIAUTOMATOR,
            value='new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("com.lohjason.genericbatterydrainer:id/tv_battery_percentage"))'
        ).text
        battery = float(battery_str.strip('%'))
        print(f"Battery after BT test: {battery}%")

        subprocess.check_output("adb shell am force-stop com.lohjason.genericbatterydrainer", shell=True)
        return battery
    except Exception as e:
        print("Error in test_bt_use:", e)
        return None


if __name__ == "__main__":
    appium_start()

    tests = [gps_use, wifi_use, bt_use, cpu_gpu_use]
    while True:
        for test in tests:
            # Get current date and time
            now = datetime.now()
            formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
            print("Current Date and Time:", formatted_time)

            battery = test()
            if battery is not None and 20.0 <= battery <= 25.0:
                print(f"Battery level {battery}% is between 20-25%. Stopping tests.")
                # break
                exit()
