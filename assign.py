"""
Assignment: Web Automation and Login Simulation using Selenium
Target Website: https://webdriveruniversity.com/Login-Portal/index.html
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def automated_login_assignment():
    """配置瀏覽器並執行自動化登入流程"""
    
    # 1. 進階配置選項 (參考 selenium2.py 的設定)
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # 若要在背景執行可取消註解
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    
    # 初始化 Chrome 瀏覽器
    driver = webdriver.Chrome(options=chrome_options)
    
    # 設置顯式等待 (Explicit Wait) 以確保網頁元素順利載入
    wait = WebDriverWait(driver, 10)
    
    try:
        # 2. 訪問指定的登入頁面
        target_url = "https://webdriveruniversity.com/Login-Portal/index.html?"
        driver.get(target_url)
        print(f"成功開啟網頁: {driver.title}")
        
        # 3. 定位帳號/使用者名稱輸入框並注入資料 (ID 定位法)
        # 根據頁面結構，使用者輸入框的 ID 為 "text"
        username_field = wait.until(
            EC.presence_of_element_located((By.ID, "text"))
        )
        username_field.send_keys("webdriver")
        print("已成功輸入帳號")
        
        # 4. 定位密碼輸入框並注入資料 (ID 定位法)
        # 根據頁面結構，密碼輸入框的 ID 為 "password"
        password_field = wait.until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password_field.send_keys("webdriver123")
        print("已成功輸入密碼")
        
        # 5. 定位登入按鈕並點擊 (ID 或 CSS Selector 定位法)
        # 根據頁面結構，登入按鈕的 ID 為 "login-button"
        login_button = wait.until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        )
        login_button.click()
        print("已點擊登入按鈕")
        
        # 6. 處理彈出視窗 (Alert) 或等待結果跳轉
        time.sleep(2)  # 暫停觀看執行結果
        try:
            alert = driver.switch_to.alert
            print("彈出視窗訊息:" ,{alert.text})
            alert.accept()  # 點擊確定關閉彈窗
        except Exception:
            print("未偵測到彈出視窗，可能已跳轉頁面")
            
    except Exception as e:
        print(f"自動化執行過程中發生錯誤: {str(e)}")
        
    finally:
        # 7. 關閉瀏覽器
        time.sleep(3)
        driver.quit()
        print("瀏覽器已關閉，作業執行完成。")

if __name__ == "__main__":
    automated_login_assignment()
