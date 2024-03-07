import json

from DrissionPage import ChromiumPage, ChromiumOptions, WebPage

from clipboard import ClipboardManager
from config import sound_svg, copy_svg, get_headers
from tools import get_id_from_url

def init_page():
    # 创建多个配置对象，每个指定不同的端口号和用户文件夹路径
    do1 = ChromiumOptions().set_paths(local_port=9111, user_data_path=r'./data1')
    # 创建多个页面对象
    page = WebPage(chromium_options=do1)
    return page


page = init_page()
token = None

def del_conversation(id):
    url = f'https://chat.openai.com/backend-api/conversation/{id}'
    payload = json.dumps({
        "is_visible": False
    })
    response = page.session.request("PATCH", url, headers=get_headers(id, token), data=payload)
    print(response.content)

def change_conversation_title(id, title):
    url = f'https://chat.openai.com/backend-api/conversation/{id}'
    payload = json.dumps({
        "title": title
    })
    response = page.session.request("PATCH", url, headers=get_headers(id, token), data=payload)
    print(response.content)

def get_session():
    url = "https://chat.openai.com/api/auth/session"
    page.get(url)
    return page.json

def get_list_and_delete():
    url = "https://chat.openai.com/backend-api/conversations?offset=0&limit=28&order=updated"
    response = page.session.request("GET", url, headers=get_headers(id, token))
    items = response.json()['items']
    for item in items:
        if item['title'] == '脚本自动化询问':
            print(item)
            tmp_id = item['id']
            print(tmp_id, item['title'])
            del_conversation(tmp_id)

def ask(content, id=None):
    # print(id, get_id_from_url(page.url))
    tag = None
    if id == None:
        url = f"https://chat.openai.com"
        tag = page.new_tab(url)
        page.wait.new_tab()
        page.wait(2)

    elif id != get_id_from_url(page.url):
        url = f"https://chat.openai.com/c/{id}"
        tab_id = page.find_tabs(url=url)
        tag = page.get_tab(tab_id)

    clipboard = ClipboardManager()

    # 输入并发送
    tag.ele('#prompt-textarea').input(content)
    tag.ele('#prompt-textarea').next('tag:button').click()

    # 等待页面显示
    tag.wait(2)
    tag.ele('#prompt-textarea').next('tag:button').wait.displayed()

    # 获取对话列表
    content_items = tag.eles('.w-full text-token-text-primary')
    last_content = content_items[-1]

    try:
        last_content.ele(f'tag:path@d={sound_svg}').wait.displayed()
    except Exception as e:
        # print(e)
        content_items = tag.eles('.w-full text-token-text-primary')
        # print(len(content_items))
        last_content = content_items[-1]
    copy_span = last_content.eles(f'tag:path@d={copy_svg}')[-1]
    # print(copy_span)
    copy_span.click()
    tag.wait(0.1)
    content = clipboard.read()
    clipboard.clear()
    if id is None:
        change_conversation_title(get_id_from_url(tag.url), "脚本自动化询问")
    return content, get_id_from_url(tag.url)

if __name__ == '__main__':
    try:
        token = get_session()['accessToken']
    except Exception as e:
        print("自己登录一下")
        page.get('https://chat.openai.com/')
        exit(0)
    # get_list()
    q = '你好'
    print(q)
    content, id = ask(q)
    print(content)

    q = '1+1等于几'
    print(q)
    content, id = ask(q, id)
    print(content)


    q2 = '你现在是猫'
    print(q2)
    content, id2 = ask(q2)
    print(content)

    q = '再+1'
    print(q)
    content, id = ask(q, id)
    print(content)


    q2 = '叫一声'
    print(q2)
    content, id2 = ask(q2, id2)
    print(content)
