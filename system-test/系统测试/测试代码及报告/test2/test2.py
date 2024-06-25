from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 初始化 Edge WebDriver
driver = webdriver.Edge()

try:
    driver.get('http://localhost:8080')  # 替换为你的应用程序运行的 URL

    # 显式等待页面加载完成
    wait = WebDriverWait(driver, 20)  # 增加等待时间

##  注册功能


    # 点击 Sign Up 按钮，激活右侧面板
    sign_up_button = wait.until(EC.element_to_be_clickable((By.ID, 'signUp')))
    sign_up_button.click()

    # 填写 Sign Up 表单
    sign_up_username = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Username"]')))
    sign_up_id = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Id"]')
    sign_up_password = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Password"]')
    sign_up_submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn')))

    sign_up_username.send_keys('testuser')
    sign_up_id.send_keys('testid')
    sign_up_password.send_keys('testpassword')

    # 滚动到按钮位置，确保可见
    driver.execute_script("arguments[0].scrollIntoView(true);", sign_up_submit)

    # 确保按钮没有被其他元素覆盖
    sign_up_submit.click()

    # 显式等待注册成功后的某个标志性元素加载完成
    wait.until(EC.element_to_be_clickable((By.ID, 'signIn')))

## 登录功能


    # 点击 Sign In 按钮，激活左侧面板
    sign_in_button = wait.until(EC.element_to_be_clickable((By.ID, 'signIn')))
    sign_in_button.click()

    # 填写 Sign In 表单
    sign_in_id = wait.until(EC.presence_of_element_located((By.ID, '111')))
    sign_in_password = driver.find_element(By.ID, '222')
    sign_in_submit = wait.until(EC.element_to_be_clickable((By.ID, '333')))

    sign_in_id.send_keys('testid')
    sign_in_password.send_keys('testpassword')

    # 滚动到按钮位置，确保可见
    driver.execute_script("arguments[0].scrollIntoView(true);", sign_in_submit)
    # 等待一段时间确保页面元素加载完全
    time.sleep(2)
    # 确保按钮没有被其他元素覆盖
    sign_in_submit.click()

    # 打印当前 URL 用于调试
    print(f"Current URL before waiting: {driver.current_url}")

    # 显式等待登录成功后的行为，比如跳转到某个特定页面
    # 使用 url_contains 而不是 url_to_be


    time.sleep(2)

    # 找到"SVM"链接并点击
    svm_element = driver.find_element(By.ID, 'svm')
    # 然后你可以对找到的元素进行操作，比如点击
    svm_element.click()

    print(f"Current URL before waiting: {driver.current_url}")

    # 验证是否成功导航到了正确的页面
    assert "http://localhost:8080/#/menu/menu2/r2" in driver.current_url
    # 点击检测按钮
    detect_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'start'))
    )
    detect_button.click()

    # 等待检测完成，例如等待结果图片加载完成
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'scaled-image'))
    )

    # 这里可以添加断言来验证检测结果
    print("Test passed: SVM link navigation successful!")

finally:
    driver.quit()
