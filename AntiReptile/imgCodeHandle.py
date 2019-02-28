import time
import random
from selenium import webdriver
from selenium.webdriver import ActionChains


def get_track(distance):
    """
    构造模拟人手动滑动轨迹
    不适用firedriver
    :param distance:
    :return:
    """
    track = []
    current = 0
    mid = distance
    t = 1
    v = 0
    while current < distance:
        if current < mid:
            a = 2
        else:
            a = -3
        v0 = v
        v = v0 + a * t
        move = v0 * t + 1 / 2 * a * t * t
        current += move
        track.append(round(move))
    return track


class VerificationHandle(object):
    def __init__(self):
        self.url = "https://s.taobao.com//search/_____tmd_____/punish?x5secdata=5e0c8e1365474455070961b803bd560607b52cabf5960afff39b64ce58073f78f68ede033dd239842063c29628191423773f1e4d712042da0b04859e7922f0cd0dce7a438dc2ea628cb8dc6014ce642b16f57a84c5d18cbaabab5fa518eeb11d45cb0ce36cef9f62cbd52852a03cf8ba461ee819ca12264cfd380e1ff9a31817c6ad559947c20869772414b84433d16914183493287775442c4521afd50dcf5a11c1735eeef60e66481766bde956ec4079a52a883b8d79c21b1904b01749f64ff68ede033dd239842063c29628191423c2512d1f2d6af203e486d1ae27585a506b8357c40b8852e10bee2dd322fdfa01b85d13ca384528f05b373d3a77a70575ad921bb1d36afdc5973c0455682491a957f7918a4f2572499cc398910575bb4ae5b2a48d9c0185c8d8521d59b4860b9243a2952e026506275152d2dce642e18a4440bf0b3e57db00024c36b841c1cc35ed81c65bebf3b9df46dd6afed6f199892c38573d94a1e033206e485398b2371f33c4d8e2e6b00ba097d8786478a58309bf29683bdadfe452f4353351418c615a44b4b6806b099f711e96a75acee751a91362f1844c20caba382eeee5bf96fd83b226301b52ea2e396b60990f1847a6df89beb4b8c866a475ab5d15242f6cd558df8a5db8c6ffe04661f7f77b33949d4e489d6e8a89ffba5192468a61a8a1c599c4d3e9b24c952c1140109e7c51a681a2b624a8069339f10804e71c355b00c978b6ab41480b171fbe6b9b4b5d10df9a024e7f70ac8d4f36730af5ea52e9c951f3c5a15f3f5a6d5727c9fd62c56d5f4a0415761c262f2a39d03a73be5825dd277865d03ab06473d92e55b6614b954eee15267c76902b202aca9fa21816732ac845b031e0ffae6bdb8f55cd1e5e0b120be5bb5bdea6cc62c7cba88ff9af8c26d20d8c8396247320930a70ab6496815f42fc397fd7929351ab88f56858a718f407c12f345fe39d1c7abda4a7c377b8b0fe5ce5ef2c966d4e95f165bd187537bbd81f5b44790779c8276689c06630db418614178b9bce5ed32d0a8e4bc5d9a5a120fbb24749603dfa93a95d2702cbc2acfc321485c4e540eeecf0b783c921696f3626834b26a48f53c0c0cd483771fc16a66abca16c95e2ad41630eaa77f1779049cb&x5step=2"
        self.driver = webdriver.Chrome()

    def parse_url(self):
        self.driver.get(self.url)

    def slide_code(self):
        self.parse_url()
        action = ActionChains(self.driver)
        source = self.driver.find_element_by_xpath('//*[@id="nc_1_n1z"]')
        action.click_and_hold(source).perform()
        action.reset_actions()
        ranges = get_track(60)
        try:
            for x in ranges:
                action.move_by_offset(xoffset=x + random.randint(1, 3), yoffset=-4).perform()  # 拖动滑块200像素点
                time.sleep(0.01)
            action.reset_actions()
            action.release()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    xx = VerificationHandle()
    xx.slide_code()