import csv
import execjs
import pandas as pd
import requests
import urllib.parse
import time

headers = {
    'cookie':'hevc_supported=true; fpk1=U2FsdGVkX1/Qc5XsPhjmX+O9jAbxYW/bQT479ISDquaNsQiXdtEqUpyyhI8ojkGfBAxKva9iqiQmNmb0ZPBJUg==; fpk2=a565ccc5e7018c4ec7bec64e38db2966; UIFID=c3109cf8eab4507640f022360c5ce002c7035d0857c7085fdeb180d1661fca19b903e404ceaa5f19ae486d988a27c9595e2cfd750edf8f33fbb21a3777ba3c547c90c2508d0b577d1e5d34f02568f46336394e1daafc3863034e9e4b5e9999a015753742e89c0f97f46ed7bf47408f8a33d58e54c53d9f9ec029ed18dab7a8f556bf13e98c589dc0095badec4682f9d5b6d6c061f8334c189a3e8b3452b001fe; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A1%7D; enter_pc_once=1; s_v_web_id=verify_mnv5veu5_5PBqHYTo_T8AX_4Fmh_9Qlf_E5Ntd4rEcrPh; dy_swidth=1707; dy_sheight=1067; WebUgChannelId=%2230001%22; strategyABtestKey=%221775961922.809%22; passport_csrf_token=f642025f01977363a83043310d163a5a; passport_csrf_token_default=f642025f01977363a83043310d163a5a; bd_ticket_guard_client_web_domain=2; is_staff_user=false; has_biz_token=false; __security_server_data_status=1; publish_badge_show_info=%220%2C0%2C0%2C1775961980315%22; DiscoverFeedExposedAd=%7B%7D; is_dash_user=1; SEARCH_RESULT_LIST_TYPE=%22single%22; SEARCH_UN_LOGIN_PV_CURR_DAY=%7B%22date%22%3A1775962147119%2C%22count%22%3A1%7D; passport_mfa_token=CjeBlCLlbgGLgFmIhbky7VOpYfaPIRxRNvSeSA7pOvmKGsvYC3bCjehetWGhbnE%2BbAtGxf0oz5goGkoKPAAAAAAAAAAAAABQS2L6IY7Q%2FNhJ%2B8vEkZyzOcw3WthQuUp2K5%2FKU7geXSj0oyvlFhHBzG813apTvuWhvBD5zI4OGPax0WwgAiIBAz8WqN0%3D; d_ticket=31822370b1157c730f066c1eec42914e51dce; n_mh=_fAGE5XQM6r4w3chHef33Aj73j_njyyw78S1SapDpEM; passport_auth_status=fc340df71e1f8a0f418e3ad80e81b900%2Cafacb02c922c73535f2f90b55c8f42a7; passport_auth_status_ss=fc340df71e1f8a0f418e3ad80e81b900%2Cafacb02c922c73535f2f90b55c8f42a7; SelfTabRedDotControl=%5B%5D; douyin.com; xg_device_score=7.78551698226827; device_web_cpu_core=16; device_web_memory_size=8; architecture=amd64; passport_assist_user=CkFio_8krRjAWSvmWOZa-JtDxLC_JiZfPuAchCjp-LJ_xZ5Mz87mYUDf3BPGCG_DwCmJTVEgggl2pWE8AKpzyClhChpKCjwAAAAAAAAAAAAAUEvzQITUaCh2uKcgFb_YVjMWU92cOVX46PYhtzH8V952b3CSYF2y6ogUPhbEaloRrj4QzM-ODhiJr9ZUIAEiAQMy_fsp; sid_guard=501d7b619e8cff4e05699701bcede547%7C1775981810%7C5184000%7CThu%2C+11-Jun-2026+08%3A16%3A50+GMT; uid_tt=3f303686cb6efbb00ecfdae68e21efe1; uid_tt_ss=3f303686cb6efbb00ecfdae68e21efe1; sid_tt=501d7b619e8cff4e05699701bcede547; sessionid=501d7b619e8cff4e05699701bcede547; sessionid_ss=501d7b619e8cff4e05699701bcede547; session_tlb_tag=sttt%7C13%7CUB17YZ6M_04FaZcBvO3lR__________0kgYqrSjE6jfKH_XbsUm4st5zvUEqJgNWLKY1saNn08M%3D; sid_ucp_v1=1.0.0-KGIxZTkyYTUwODc0ZGYzOWRmNDlmYTc3M2VhYmI3NDg3M2Q4MTVkNTMKIQipvODPu83KBxDyqe3OBhjvMSAMMIe_7q0GOAdA9AdIBBoCbHEiIDUwMWQ3YjYxOWU4Y2ZmNGUwNTY5OTcwMWJjZWRlNTQ3; ssid_ucp_v1=1.0.0-KGIxZTkyYTUwODc0ZGYzOWRmNDlmYTc3M2VhYmI3NDg3M2Q4MTVkNTMKIQipvODPu83KBxDyqe3OBhjvMSAMMIe_7q0GOAdA9AdIBBoCbHEiIDUwMWQ3YjYxOWU4Y2ZmNGUwNTY5OTcwMWJjZWRlNTQ3; _bd_ticket_crypt_cookie=94426e11d65d227f619c19016d56a0b3; __security_mc_1_s_sdk_sign_data_key_web_protect=fb03d618-49c9-9130; __security_mc_1_s_sdk_cert_key=7be9eb11-4aae-be09; __security_mc_1_s_sdk_crypt_sdk=c25d8d34-496a-81bc; login_time=1775981811436; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1707%2C%5C%22screen_height%5C%22%3A1067%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A16%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A100%7D%22; ttwid=1%7C_0voxDrC8LopIp8q4Z-gnlVRs3gaohP76LlE00n1W9Q%7C1775981816%7Cf17a328fd4c4e6e9a64911ce64a2ecaa451c0284c368d04ed7a14ee4fcff8098; download_guide=%223%2F20260412%2F0%22; __ac_signature=_02B4Z6wo00f0177yfNwAAIDDML8K6MfRVh--0nhAAIZvegcr9mhJZbeA449mHLpfZI4S1dokS2Ea1950zLyLTrxTaW6a7je5eSmPHGh9-.CkpRNu9qFOIBXOTuFfYoeRCbupaf3WDo2evdJyd2; csrf_session_id=b3616008a20f2542b3661a42ce25c6b1; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCT1V4ZGUranQ2dlVvQ0paVWlPMmRnUzhuQ2lDZ1VaODV4a3I1RkNjVkErNmZaSTdqL1grRmZVa3ZuVVo3UmwrTDdRTHhIL2JLbVJiZmNSTmN0ckMwUDQ9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; home_can_add_dy_2_desktop=%221%22; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAA5pT6SHGp43tlqb8Zwy0EuLjjdLMpBylk2MeYNyEXI-s-V8Sppt0V-Cg-JSfFhV53%2F1776009600000%2F0%2F1775992907855%2F0%22; biz_trace_id=bf5877c3; IsDouyinActive=true; sdk_source_info=7e276470716a68645a606960273f276364697660272927676c715a6d6069756077273f276364697660272927666d776a68605a607d71606b766c6a6b5a7666776c7571273f275e58272927666a6b766a69605a696c6061273f27636469766027292762696a6764695a7364776c6467696076273f275e582729277672715a646971273f2763646976602729277f6b5a666475273f2763646976602729276d6a6e5a6b6a716c273f2763646976602729276c6b6f5a7f6367273f27636469766027292771273f273d3d3031313533333533323234272927676c715a75776a716a666a69273f27717770602778; bit_env=bEv9bJnlLxur5rSe70qU-8DIfU_8fQU1Cvc7L6sOwBXhGNg9bEYvOAoE9sWmdINGLLfAe-KyfUUXKIkHME1isbv0D42vkJYwdF5zgyYuzNfblVH-pINkiEetHsEjsk8F36B6QtpyQKOfjK8rPNu_AipwnUqOy-iO67tG9sZ4sCHhYVuM4EwcUIXtwQcT4OybTJMg9R3LxOeQM1Qlepi_n4sOO_RelByxKMqss5M3Eadx1JJx5JYvDZ8ffQDifShcsSH2W20q-rIkjyVg9xmjT9vsc5RUHFXEa1n2Z3le5WoMRGOPG4Z69fZi43nPXOUZkjo21zY1pO2pvN5d0NRAW6MOOIVW83rju8V6trHmMdNZQ7TAfEiFtqTQQ-zKrsLfAHSIIpjpoanxDOgUc6szv_t_obC3mz0jV_W6C9D9PK4wcxdZ9l7nWsAjotju7sv1A_olTUTtcFGlBKm5wtYZ2SAAzNbIBNN4LvoWQYjpxfLsvChhzbyNVdihI391Amwk2o0vaGmVylw2Hkc_0IDuLEB50PkbKXFTbJhvqsFpXbo%3D; gulu_source_res=eyJwX2luIjoiZWQ4OTJkZTQxNGQ4NGI4MzgwNWEwYjA4MDY3MTA0MzU4MTFlNGFjOGQyYzEwZjAxMjZiMTJiYjAzYTEyZDlkNCJ9; passport_auth_mix_state=8mqk8hd37gcxri7buobowupwtb77yq00m2cs2q8q89flfg3i; bd_ticket_guard_client_data_v2=eyJyZWVfcHVibGljX2tleSI6IkJPVXhkZStqdDZ2VW9DSlpVaU8yZGdTOG5DaUNnVVo4NXhrcjVGQ2NWQSs2ZlpJN2ovWCtGZlVrdm5VWjdSbCtMN1FMeEgvYkttUmJmY1JOY3RyQzBQND0iLCJ0c19zaWduIjoidHMuMi4yNGYyZDMzNWNiZmI2MDFmMGNhYmYwZDc1ZmM1YzJkMzMxMGQwYjFkMjA3NThiNWRmN2VkYjY5NzY4ZjU1NWU2YzRmYmU4N2QyMzE5Y2YwNTMxODYyNGNlZGExNDkxMWNhNDA2ZGVkYmViZWRkYjJlMzBmY2U4ZDRmYTAyNTc1ZCIsInJlcV9jb250ZW50Ijoic2VjX3RzIiwicmVxX3NpZ24iOiJlMHN6STJEa09JQ1R3RTY4WGJBRnN6U0w0b1hqa0hyTEdUVXZzQlF6NTRFPSIsInNlY190cyI6IiNIY3RtOEFvMXFxUS9zdTBsN0NLWktzbTBydlZ0L3IxbzlWaUNFdVh2VWw0Z3k3UG4rbDhWa01CSnRKdmgifQ%3D%3D; odin_tt=9f925b61f384b07f7fa641554f9362c505925e2aeca8d63bfdd9bd08fae9136e0767e54871b13c3029c394e276c62498654efe8a8ed992cfbac741bb9f70507d',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0',
    'accept':'application/json, text/plain, */*'

}

def get_time(ctime):
    time_local = time.localtime(ctime)

    time_format = time.strftime("%Y-%m-%d", time_local)

    return str(time_format)


def get_json(aweme_id, cursor):
    url = f"https://www.douyin.com/aweme/v1/web/comment/list/?aid=6383&aweme_id={aweme_id}&count=20&cursor={cursor}"

    query = urllib.parse.urlparse(url).query
    a_bogus = execjs.compile(open('XB.js').read()).call('sign', query, headers.get('user-agent'))
    video_url = url + '&X-Bogus=' + a_bogus
    time.sleep(1)

    response = requests.get(video_url, headers=headers)

    return response.json()


def parseData(feed, aweme_id):
    ip_label = feed.get('ip_label','')
    try:
        username = feed['user']['nickname']
    except:
        username = '暂无用户名'

    comment_dict = {
        '用户id': feed['user']['uid'],
        '用户名': username,
        '评论时间': get_time(feed['create_time']),
        'IP地址': ip_label,
        '评论内容': feed.get('text',''),
        '点赞数量': feed.get('digg_count',''),
        'aweme_id': aweme_id
    }
    print(comment_dict)
    writer.writerow(comment_dict)

def spider_comment(aweme_id):
    cursor = 0
    page = 1
    while True:

        response = get_json(aweme_id, cursor)
        try:
            if response['comments'] is None:
                break

            feeds = response['comments']
            for feed in feeds:
                parseData(feed, aweme_id)
                break
            if response['has_more'] == 0:
                break
            cursor += 20

            page += 1
            if page > 20:
                break
        except Exception as e:
            print(f'爬取失败，错误：{e}')
            continue

if __name__ == '__main__':
    header = ['用户id', '用户名', '评论时间', 'IP地址', '评论内容', '点赞数量', 'aweme_id']
    f = open('comment_data.csv', 'a', encoding='utf-8', newline='')
    writer = csv.DictWriter(f, header)
    writer.writeheader()
    df = pd.read_csv('data.csv')
    for index, row in df.iterrows():
        spider_comment(row['视频id'])