import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
}


def ban():
    """
    涨停池
    :return:data_list
    """
    url = "https://x-quote.cls.cn/quote/index/up_down_analysis?app=CailianpressWeb&os=web&rever=1&sv=7.5.5&token=lMcwgq90IuGhL510ZnCEQ33Ntrbav14z1017500&type=up_pool&uid=1017500&way=last_px&sign=8ec1fb97cdaeb700df212e2f6bbac6c8"
    resp = requests.get(url, headers=headers)

    data_list = []
    for i in resp.json()['data']:
        secu_code = i['secu_code']
        secu_name = i['secu_name']
        last_px = i['last_px']
        change = "+{:.2f}".format(i['change'] * 100) + '%'
        limit_up_days = i['limit_up_days']
        up_reason = i['up_reason']
        time_t = i['time']
        # 把数据保存到列表，大列表套N个小列表，这样好取数据，不能全部都追加到一个列表里，那样数据就乱了 没法取了
        data_list.append([secu_code, secu_name, last_px, change, limit_up_days, up_reason, time_t])
    return data_list


def l_ban():
    """
    连板池
    :return:data_list
    """
    url = "https://x-quote.cls.cn/quote/index/up_down_analysis?app=CailianpressWeb&os=web&rever=1&sv=7.5.5&token=lMcwgq90IuGhL510ZnCEQ33Ntrbav14z1017500&type=continuous_up_pool&uid=1017500&way=last_px&sign=a9675cb60901dd492cbb010d637163a6"
    resp = requests.get(url, headers=headers)

    data_list = []
    for i in resp.json()['data']:
        secu_code = i['secu_code']
        secu_name = i['secu_name']
        last_px = i['last_px']
        change = "+{:.2f}".format(i['change'] * 100) + '%'
        limit_up_days = i['limit_up_days']
        up_reason = i['up_reason']
        time_t = i['time']
        # 把数据保存到列表，大列表套N个小列表，这样好取数据，不能全部都追加到一个列表里，那样数据就乱了 没法取了
        data_list.append([secu_code, secu_name, last_px, change, limit_up_days, up_reason, time_t])
    return data_list


def z_ban():
    """
    炸板池
    :return:data_list
    """
    url = "https://x-quote.cls.cn/quote/index/up_down_analysis?app=CailianpressWeb&os=web&rever=1&sv=7.5.5&token=lMcwgq90IuGhL510ZnCEQ33Ntrbav14z1017500&type=up_open_pool&uid=1017500&way=last_px&sign=7a5a9f67f49cf817f72d8e13fc30beea"
    resp = requests.get(url, headers=headers)

    data_list = []
    for i in resp.json()['data']:
        secu_code = i['secu_code']
        secu_name = i['secu_name']
        last_px = i['last_px']
        change = "{:.2f}".format(i['change'] * 100) + '%'
        if '-' not in change:  # 如果不是跌 那就是涨 添加个 + 号
            change = "+{:.2f}".format(i['change'] * 100) + '%'
        up_reason = i['up_reason']
        time_t = i['time']
        # 把数据保存到列表，大列表套N个小列表，这样好取数据，不能全部都追加到一个列表里，那样数据就乱了 没法取了
        data_list.append([secu_code, secu_name, last_px, change, up_reason, time_t])
    return data_list


def d_ban():
    """
    跌停池
    :return:data_list
    """
    url = "https://x-quote.cls.cn/quote/index/up_down_analysis?app=CailianpressWeb&os=web&rever=1&sv=7.5.5&token=lMcwgq90IuGhL510ZnCEQ33Ntrbav14z1017500&type=down_pool&uid=1017500&way=last_px&sign=19d513ef206f9863c488b4f1377818ee"
    resp = requests.get(url, headers=headers)

    data_list = []
    for i in resp.json()['data']:
        secu_code = i['secu_code']
        secu_name = i['secu_name']
        last_px = i['last_px']
        change = "{:.2f}".format(i['change'] * 100) + '%'
        up_reason = i['up_reason']
        time_t = i['time']
        # 把数据保存到列表，大列表套N个小列表，这样好取数据，不能全部都追加到一个列表里，那样数据就乱了 没法取了
        data_list.append([secu_code, secu_name, last_px, change, up_reason, time_t])
    return data_list
