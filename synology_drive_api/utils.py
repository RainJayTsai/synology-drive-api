import urllib.parse

try:
    import simplejson as json
except:
    import json


def get_local_ip_by_quick_connect_id(q_id):
    """
    # if nas local ip changed, get ip according to quick_connect
    # see https://quickconnect.to/
    :param q_id: QuickConnect ID
    :return:
    """
    from selenium import webdriver
    url = f"https://{q_id}.quickconnect.to/"
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.get(url)
    driver.implicitly_wait(20)
    cookie = driver.get_cookies()
    dict1 = cookie[2]
    value1 = dict1['value']
    return value1.split('ipv4.')[1].split('.wan')[0]


def form_urlencoded(data: dict) -> str:
    """
    Generate urlencoded data for body data
    :param data: ready for post data
    :return: return form data
    """
    data_list = []
    for key, value in data.items():
        value_encode = urllib.parse.quote(json.dumps(value), safe='') if not isinstance(value, str) else value
        # [key, '=', value_encode]
        data_list.append(f"{key}={value_encode}")
    urlencoded_data = '&'.join(data_list)
    return urlencoded_data


def concat_drive_path(dest_path: str, end_point: str, default_folder: str = 'mydrive') -> str:
    """
    Generate file path
    :param dest_path: parent path
    :param end_point: file_name or folder_name
    :param default_folder: if dest_path is None, use your drive home folder instead
    :return:
    """
    if dest_path is None:
        display_path = f"/{default_folder}/{end_point}"
    elif dest_path.startswith('id'):
        display_path = f"{dest_path}/folder_name"
    else:
        # add start position /
        dest_path = f"/{dest_path}" if not dest_path.startswith('/') else dest_path
        # add end position /
        dest_path = f"{dest_path}/" if not dest_path.endswith('/') else dest_path
        display_path = f"{dest_path}{end_point}"
    return display_path
