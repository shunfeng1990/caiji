from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from chaojiying import Chaojiying_Client
import time

# 初始化超级鹰
chaojiying = Chaojiying_Client('超级鹰用户名', '超级鹰密码', '软件id')

# 1. 如果浏览器版本小于88 （过selenium 检测）
# web = Chrome()

# web.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#     "source": """
#     window.navigator.webdriver = undefined
#         Object.defineProperty(navigator, 'webdriver', {
#             get: () => undefined
#         })
#     """
# })

# 2. 如果谷歌浏览器版本大于88 （过selenium 检测）
option = Options()
option.add_argument('--disable-blink-features=AutomationControlled')

web = Chrome(options=option)
web.get('https://kyfw.12306.cn/otn/resources/login.html')
time.sleep(2)

web.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a').click()
time.sleep(2)

# 处理验证码
verify_img_element = web.find_element_by_xpath('//*[@id="J-loginImg"]')

# 用超级鹰识别验证码图片
dic = chaojiying.PostPic(verify_img_element.screenshot_as_png, 9004)
result = dic['pic_str']

# 验证码如果没识别到就停止程序
if len(result) == 0:
    print('验证码识别失败')
    web.close()
    exit()

# 识别到多个坐标格式： 112,76|253,81  识别到一个坐标格式：112,76 要根据不同情况进行处理
print(result)

# 如果坐标包含|，如下处理方式
if '|' in result:
    res_list = result.split('|')  # 处理下坐标
    for res in res_list:
        p_temp = res.split(',')
        x = int(p_temp[0])
        y = int(p_temp[1])
        # 让鼠标移动到 x y坐标位置，进行点击
        ActionChains(web).move_to_element_with_offset(verify_img_element, x, y).click().perform()
else:
    x = int(result.split(',')[0])
    y = int(result.split(',')[1])
    # 让鼠标移动到 x y坐标位置，进行点击
    ActionChains(web).move_to_element_with_offset(verify_img_element, x, y).click().perform()

time.sleep(1)
# 输入用户名和密码
web.find_element_by_xpath('//*[@id="J-userName"]').send_keys('123456')
web.find_element_by_xpath('//*[@id="J-password"]').send_keys('123456')

time.sleep(1)
# 点击登入
web.find_element_by_xpath('//*[@id="J-login"]').click()

time.sleep(4)
btn = web.find_element_by_xpath('//*[@id="nc_1__scale_text"]/span')
ActionChains(web).drag_and_drop_by_offset(btn, 300, 0).perform()
