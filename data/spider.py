import csv
import random
import time
import requests


headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "priority": "u=1, i",
    "referer": "https://www.douyin.com/search/%E9%A3%9E%E9%A9%B0%E4%BA%BA%E7%94%9F3?aid=d03880c5-54ac-49fa-b23c-d75ed892ccd1&type=general",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"147\", \"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"147\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "uifid": "3b6adaced0a588dab6f51c731af48a99e86229cd7fa27db4535ff73b415f88b56a30fb214a7c25b3f1f3772b6bf2149e9767940a424b252d539cc4feff8e041df6fcb80346cc1fa291b87b07bc40c2986080ea8f1ed851b8e41cfa0b1b5e74097be6447003d3998d1fe1f240d0a814c37c71badd6bb2ad904431e6b9aa29fb92162f13924374ed55a627f0d5106d7bca3e9c5285bd3895e73714c3cd4b664709",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0"
}
cookies = {
    "hevc_supported": "true",
    "enter_pc_once": "1",
    "s_v_web_id": "verify_mnv5veu5_5PBqHYTo_T8AX_4Fmh_9Qlf_E5Ntd4rEcrPh",
    "WebUgChannelId": "%2230001%22",
    "passport_csrf_token": "f642025f01977363a83043310d163a5a",
    "passport_csrf_token_default": "f642025f01977363a83043310d163a5a",
    "bd_ticket_guard_client_web_domain": "2",
    "is_staff_user": "false",
    "has_biz_token": "false",
    "__security_server_data_status": "1",
    "SEARCH_RESULT_LIST_TYPE": "%22single%22",
    "SEARCH_UN_LOGIN_PV_CURR_DAY": "%7B%22date%22%3A1775962147119%2C%22count%22%3A1%7D",
    "passport_mfa_token": "CjeBlCLlbgGLgFmIhbky7VOpYfaPIRxRNvSeSA7pOvmKGsvYC3bCjehetWGhbnE%2BbAtGxf0oz5goGkoKPAAAAAAAAAAAAABQS2L6IY7Q%2FNhJ%2B8vEkZyzOcw3WthQuUp2K5%2FKU7geXSj0oyvlFhHBzG813apTvuWhvBD5zI4OGPax0WwgAiIBAz8WqN0%3D",
    "d_ticket": "31822370b1157c730f066c1eec42914e51dce",
    "n_mh": "_fAGE5XQM6r4w3chHef33Aj73j_njyyw78S1SapDpEM",
    "passport_auth_status": "fc340df71e1f8a0f418e3ad80e81b900%2Cafacb02c922c73535f2f90b55c8f42a7",
    "passport_auth_status_ss": "fc340df71e1f8a0f418e3ad80e81b900%2Cafacb02c922c73535f2f90b55c8f42a7",
    "SelfTabRedDotControl": "%5B%5D",
    "passport_assist_user": "CkFio_8krRjAWSvmWOZa-JtDxLC_JiZfPuAchCjp-LJ_xZ5Mz87mYUDf3BPGCG_DwCmJTVEgggl2pWE8AKpzyClhChpKCjwAAAAAAAAAAAAAUEvzQITUaCh2uKcgFb_YVjMWU92cOVX46PYhtzH8V952b3CSYF2y6ogUPhbEaloRrj4QzM-ODhiJr9ZUIAEiAQMy_fsp",
    "sid_guard": "501d7b619e8cff4e05699701bcede547%7C1775981810%7C5184000%7CThu%2C+11-Jun-2026+08%3A16%3A50+GMT",
    "uid_tt": "3f303686cb6efbb00ecfdae68e21efe1",
    "uid_tt_ss": "3f303686cb6efbb00ecfdae68e21efe1",
    "sid_tt": "501d7b619e8cff4e05699701bcede547",
    "sessionid": "501d7b619e8cff4e05699701bcede547",
    "sessionid_ss": "501d7b619e8cff4e05699701bcede547",
    "session_tlb_tag": "sttt%7C13%7CUB17YZ6M_04FaZcBvO3lR__________0kgYqrSjE6jfKH_XbsUm4st5zvUEqJgNWLKY1saNn08M%3D",
    "sid_ucp_v1": "1.0.0-KGIxZTkyYTUwODc0ZGYzOWRmNDlmYTc3M2VhYmI3NDg3M2Q4MTVkNTMKIQipvODPu83KBxDyqe3OBhjvMSAMMIe_7q0GOAdA9AdIBBoCbHEiIDUwMWQ3YjYxOWU4Y2ZmNGUwNTY5OTcwMWJjZWRlNTQ3",
    "ssid_ucp_v1": "1.0.0-KGIxZTkyYTUwODc0ZGYzOWRmNDlmYTc3M2VhYmI3NDg3M2Q4MTVkNTMKIQipvODPu83KBxDyqe3OBhjvMSAMMIe_7q0GOAdA9AdIBBoCbHEiIDUwMWQ3YjYxOWU4Y2ZmNGUwNTY5OTcwMWJjZWRlNTQ3",
    "_bd_ticket_crypt_cookie": "94426e11d65d227f619c19016d56a0b3",
    "__security_mc_1_s_sdk_sign_data_key_web_protect": "fb03d618-49c9-9130",
    "__security_mc_1_s_sdk_cert_key": "7be9eb11-4aae-be09",
    "__security_mc_1_s_sdk_crypt_sdk": "c25d8d34-496a-81bc",
    "login_time": "1775981811436",
    "UIFID_TEMP": "3b6adaced0a588dab6f51c731af48a99e86229cd7fa27db4535ff73b415f88b56a30fb214a7c25b3f1f3772b6bf2149ee913d0b5053cb904a44625cf5044cdb31fe379d4dce5c95ec4b776ff47557826",
    "douyin.com": "",
    "xg_device_score": "7.78551698226827",
    "device_web_cpu_core": "16",
    "device_web_memory_size": "16",
    "architecture": "amd64",
    "is_support_rtm_web_ts": "1",
    "dy_swidth": "1707",
    "dy_sheight": "1067",
    "is_dash_user": "1",
    "strategyABtestKey": "%221777283145.561%22",
    "fpk1": "U2FsdGVkX1+roaBSVlYPy2GKZTZzyZfgo1HsTMhfsv6zudAbkx1ZPJCi7b6owB7eNACCJ3h4KitZ8FYydCz4QQ==",
    "fpk2": "4238b62bcd3c1a9c24ccf656e6ace824",
    "ttwid": "1%7C_0voxDrC8LopIp8q4Z-gnlVRs3gaohP76LlE00n1W9Q%7C1777283143%7C722fe69ef6496af6d2b552b92db2ad11aa7b9b2bafa6abcea2e116b2c5646d1b",
    "publish_badge_show_info": "%220%2C0%2C0%2C1777283148238%22",
    "UIFID": "3b6adaced0a588dab6f51c731af48a99e86229cd7fa27db4535ff73b415f88b56a30fb214a7c25b3f1f3772b6bf2149e9767940a424b252d539cc4feff8e041df6fcb80346cc1fa291b87b07bc40c2986080ea8f1ed851b8e41cfa0b1b5e74097be6447003d3998d1fe1f240d0a814c37c71badd6bb2ad904431e6b9aa29fb92162f13924374ed55a627f0d5106d7bca3e9c5285bd3895e73714c3cd4b664709",
    "volume_info": "%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A1%7D",
    "playRecommendGuideTagCount": "1",
    "totalRecommendGuideTagCount": "1",
    "stream_player_status_params": "%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22",
    "csrf_session_id": "aa49570540c06b6617f898b572da5dac",
    "download_guide": "%223%2F20260427%2F0%22",
    "__ac_nonce": "069ef4083006f6699d619",
    "__ac_signature": "_02B4Z6wo00f01zrJwcgAAIDDtIS3.W-OGZ866cVAAKdnqugeaHW46YzmBrxC-za1-raF6ZqtMbOkw7e1eo-a1eatMaXGuxSnkvVbcNoH1Hp3wTO.gv1gisEAzY7tKiI9eTGhLam9TT4q4gP430",
    "stream_recommend_feed_params": "%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1707%2C%5C%22screen_height%5C%22%3A1067%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A16%2C%5C%22device_memory%5C%22%3A16%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A100%7D%22",
    "sdk_source_info": "7e276470716a68645a606960273f276364697660272927676c715a6d6069756077273f276364697660272927666d776a68605a607d71606b766c6a6b5a7666776c7571273f275e58272927666a6b766a69605a696c6061273f27636469766027292762696a6764695a7364776c6467696076273f275e582729277672715a646971273f2763646976602729277f6b5a666475273f2763646976602729276d6a6e5a6b6a716c273f2763646976602729276c6b6f5a7f6367273f27636469766027292771273f27333135303436323d3732323234272927676c715a75776a716a666a69273f2763646976602778",
    "bit_env": "gGA34CTGMl3fD911qZtkjOuR3FLgexOhwp72mLMsSnrMgqbcYPWFP9grz0s7cmo3GB0qRlL6bmtjd6rn14IkVJYVrv41i2snalMMzHkCnyocnbH2r6QD8Woyq2ufQgemX2RscyPlJc_KhZDC4e03c3gaXnjN2qO_wavUm6mWkb2qgXllwbOhI1sndHDki7Wzqu0ZDMOQ6uFtX94D0mrM3eUv3m4F0bZ45s1pi6yqTY3zTlujBRMaqGoda-GamBDwPGx_SWw5Acjppj4CmCkAXyz53Mi0JLi2oflBSQafbyQWDibmYgmEAvg_Teqjolb9VaPi1n6EUAJ20ZX34X-hPD2PytbwOdDDnQkn04SmoNBFnPI1A7SvrHJUT53CoLBQweyZHEraU6O1OSnVELP7FFe8Y9ntzAezWrezrzw326YqSQkKfFFHyK26GLjyQ5t2J21DwPbfqDEn2IoDUFH9TVNpt2SF1c_IWDrh5Vvwe43db0QW3sey2HnVj8jwJsoOU1Jw9vtzsQrS0_7lM1_C7vbNpGewqjn3Aq383_wbWA0%3D",
    "gulu_source_res": "eyJwX2luIjoiYzA3ZDQzMmJmM2E3YmU5Mjc0ZjBmODA2OGQwZjQ3N2M1Y2I2Mzc2NjNlZTdhOTBiMjlhZWNjZWE3YzQxMjgxYSJ9",
    "passport_auth_mix_state": "5c2r7r4ujmq1r7jwlzum6mh81xxryjpy",
    "IsDouyinActive": "true",
    "bd_ticket_guard_client_data": "eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCT1V4ZGUranQ2dlVvQ0paVWlPMmRnUzhuQ2lDZ1VaODV4a3I1RkNjVkErNmZaSTdqL1grRmZVa3ZuVVo3UmwrTDdRTHhIL2JLbVJiZmNSTmN0ckMwUDQ9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D",
    "FOLLOW_LIVE_POINT_INFO": "%22MS4wLjABAAAA5pT6SHGp43tlqb8Zwy0EuLjjdLMpBylk2MeYNyEXI-s-V8Sppt0V-Cg-JSfFhV53%2F1777305600000%2F0%2F0%2F1777288118490%22",
    "FOLLOW_NUMBER_YELLOW_POINT_INFO": "%22MS4wLjABAAAA5pT6SHGp43tlqb8Zwy0EuLjjdLMpBylk2MeYNyEXI-s-V8Sppt0V-Cg-JSfFhV53%2F1777305600000%2F0%2F1777287518490%2F0%22",
    "home_can_add_dy_2_desktop": "%221%22",
    "biz_trace_id": "c26d1ed3",
    "bd_ticket_guard_client_data_v2": "eyJyZWVfcHVibGljX2tleSI6IkJPVXhkZStqdDZ2VW9DSlpVaU8yZGdTOG5DaUNnVVo4NXhrcjVGQ2NWQSs2ZlpJN2ovWCtGZlVrdm5VWjdSbCtMN1FMeEgvYkttUmJmY1JOY3RyQzBQND0iLCJ0c19zaWduIjoidHMuMi4yNGYyZDMzNWNiZmI2MDFmMGNhYmYwZDc1ZmM1YzJkMzMxMGQwYjFkMjA3NThiNWRmN2VkYjY5NzY4ZjU1NWU2YzRmYmU4N2QyMzE5Y2YwNTMxODYyNGNlZGExNDkxMWNhNDA2ZGVkYmViZWRkYjJlMzBmY2U4ZDRmYTAyNTc1ZCIsInJlcV9jb250ZW50Ijoic2VjX3RzIiwicmVxX3NpZ24iOiIrWk1BKzRDUmVPRXdXUXhhdTUrVWVrUHg4clpXYnFaWnlGcGNnN2xaRXBZPSIsInNlY190cyI6IiMwcDgxNWw5S3ZmQmtUNWxyK3hQM1M2UkN2cE92SjRPdnJYSXRCRGxYQTVoZVN0YUd0dGZ1T3RVNklhZ2wifQ%3D%3D",
    "odin_tt": "548b9ce1634424f8e4bfcf17b1072451d570d1e43d7d906f8f62e6072ba0cbe126181997103d8612a3beab6b317753329602b05f6bab2ae52047918c551b6c84"
}
url = "https://www.douyin.com/aweme/v1/web/search/item/"

def get_time(ctime):
    time_local = time.localtime(ctime)

    time_format = time.strftime("%Y-%m-%d", time_local)

    return str(time_format)


def get_json(keyword, offset, count):
    params = {
        "device_platform": "webapp",
        "aid": "6383",
        "channel": "channel_pc_web",
        "search_channel": "aweme_general",
        "enable_history": "1",
        "filter_selected": "{\"sort_type\":\"1\",\"publish_time\":\"0\"}",
        "keyword": keyword,
        "search_source": "tab_search",
        "query_correct_type": "1",
        "is_filter_search": "1",
        "from_group_id": "",
        "disable_rs": "0",
        "offset": offset,
        "count": count,
        "need_filter_settings": "0",
        "list_type": "single",
        "pc_search_top_1_params": "{\"enable_ai_search_top_1\":1}",
        "search_id": "20260427185849F7EF456DC2797ADD889D",
        "update_version_code": "170400",
        "pc_client_type": "1",
        "pc_libra_divert": "Windows",
        "support_h265": "1",
        "support_dash": "1",
        "cpu_core_num": "16",
        "version_code": "190600",
        "version_name": "19.6.0",
        "cookie_enabled": "true",
        "screen_width": "1707",
        "screen_height": "1067",
        "browser_language": "zh-CN",
        "browser_platform": "Win32",
        "browser_name": "Edge",
        "browser_version": "147.0.0.0",
        "browser_online": "true",
        "engine_name": "Blink",
        "engine_version": "147.0.0.0",
        "os_name": "Windows",
        "os_version": "10",
        "device_memory": "16",
        "platform": "PC",
        "downlink": "10",
        "effective_type": "4g",
        "round_trip_time": "0",
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    print(response.text)
    print(response)
    return response.json()

def parseData(response):
    global video_dict

    # 1. 处理视频时长（duration 通常是毫秒，需除以 1000）
    duration_ms = response.get('video', {}).get('duration', 0)
    minutes = duration_ms // 1000 // 60
    seconds = (duration_ms // 1000) % 60

    # 2. 获取时间戳（create_time 才是时间）
    create_time = response.get('create_time', 0)

    video_dict = {
        '用户名': response.get('author', {}).get('nickname', '未知用户').strip(),
        '粉丝数量': response.get('author', {}).get('follower_count', 0),
        '视频描述': response.get('desc', ''),
        '视频id': response.get('aweme_id', ''),
        '发表时间': get_time(int(create_time)),
        '视频时长': "{:02d}:{:02d}".format(minutes, seconds),
        '点赞数量': response.get('statistics', {}).get('digg_count', 0),
        '收藏数量': response.get('statistics', {}).get('collect_count', 0),
        '评论数量': response.get('statistics', {}).get('comment_count', 0),
        '分享数量': response.get('statistics', {}).get('share_count', 0),
        '下载数量': response.get('statistics', {}).get('download_count', 0),
    }

    print(video_dict)
    writer.writerow(video_dict)

def search(keyword):
    offset = 0
    count = 16
    while True:
        response = get_json(keyword, offset, count)

        # 1. 安全检查：确保获取到了 data 且 data 是列表
        if not response or 'data' not in response or response['data'] is None:
            print("未获取到数据，可能触发了验证码或搜索结束。")
            break

        feeds = response['data']
        for feed in feeds:
            # 2. 关键修复：只有当 'aweme_info' 在 feed 中时，才调用解析函数
            if 'aweme_info' in feed:
                parseData(feed['aweme_info'])
            else:
                # 跳过非视频数据（如：搜索建议、广告、百科等）
                print("跳过非视频条目...")
                continue

        # 3. 检查是否还有更多数据
        # 抖音的 has_more 有时在根目录，有时在 data 级，建议根据 response 结构调整
        has_more = response.get('has_more', 0)
        if has_more == 0:
            print("所有视频采集完毕。")
            break

        offset += count


if __name__ == "__main__":
    # keyword = input('')

    header = ['用户名','粉丝数量','视频描述','视频id','发表时间','视频时长','点赞数量','收藏数量','评论数量','分享数量','下载数量']
    f = open('data.csv', 'a', encoding='utf-8', newline='')
    writer = csv.DictWriter(f, header)
    writer.writeheader()
    keyword = '飞驰人生3'
    search(keyword)


