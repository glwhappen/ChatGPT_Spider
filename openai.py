from DrissionPage import ChromiumPage, ChromiumOptions

from clipboard import ClipboardManager
from tools import get_id_from_url


def init_page():
    # 创建多个配置对象，每个指定不同的端口号和用户文件夹路径
    do1 = ChromiumOptions().set_paths(local_port=9111, user_data_path=r'./data1')
    # 创建多个页面对象
    page = ChromiumPage(addr_or_opts=do1)
    return page


page = init_page()

def ask(content, id=None):
    # print(id, get_id_from_url(page.url))
    tag = None
    if id == None:
        url = f"https://chat.openai.com"
        # page.get(url)
        # page.wait.doc_loaded()
        # page.wait(2)
        # tab_id = page.find_tabs(url=url)
        # print(tab_id)
        # if tab_id:
        #     page.get_tab(tab_id)
        # else:
        tag = page.new_tab(url)
        page.wait.new_tab()
        # print(page.latest_tab)

        # page.get_tab(page.latest_tab)
        page.wait(2)

    elif id != get_id_from_url(page.url):
        # tab_id = page.find_tabs(url=url)
        # print(tab_id)
        # page.get(url)
        # page.wait.doc_loaded()
        # page.wait(2)
        # page.new_tab(url)
        # page.wait.new_tab()
        # page.wait(2)
        url = f"https://chat.openai.com/c/{id}"
        tab_id = page.find_tabs(url=url)
        # print(tab_id)
        tag = page.get_tab(tab_id)

    # if id != None:
    #     url = f"https://chat.openai.com/c/{id}"
    #     tab_id = page.find_tabs(url=url)
    #     print(tab_id)

    clipboard = ClipboardManager("9111")

    #
    tag.ele('#prompt-textarea').wait.displayed()
    tag.ele('#prompt-textarea').input(content)
    tag.ele('#prompt-textarea').next('tag:button').wait.displayed()
    tag.ele('#prompt-textarea').next('tag:button').click()
    # print(parent.html)
    # page.ele('t:button')
    # page.ele('变异体生成').click()
    # data-message-author-role="assistant"
    # items = page.eles('@data-message-author-role=assistant')
    # for item in items:
    #     print(item.text)
    # page.listen.start('/backend-api/conversation')



    # res = page.listen.wait()
    #
    # print(res.url)
    # print(res.response)
    # exit(0)
    # pause_svg = 'M0 2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2z'
    # print("等待输出")
    tag.wait(2)
    tag.ele('#prompt-textarea').next('tag:button').wait.displayed()
    # print("等待完毕")

    content_items = tag.eles('.w-full text-token-text-primary')
    # print(len(content_items))
    last_content = content_items[-1]
    # print(content_items[-1])
    copy_svg = 'M12 3.5C10.8954 3.5 10 4.39543 10 5.5H14C14 4.39543 13.1046 3.5 12 3.5ZM8.53513 3.5C9.22675 2.3044 10.5194 1.5 12 1.5C13.4806 1.5 14.7733 2.3044 15.4649 3.5H17.25C18.9069 3.5 20.25 4.84315 20.25 6.5V18.5C20.25 20.1569 19.1569 21.5 17.25 21.5H6.75C5.09315 21.5 3.75 20.1569 3.75 18.5V6.5C3.75 4.84315 5.09315 3.5 6.75 3.5H8.53513ZM8 5.5H6.75C6.19772 5.5 5.75 5.94772 5.75 6.5V18.5C5.75 19.0523 6.19772 19.5 6.75 19.5H17.25C18.0523 19.5 18.25 19.0523 18.25 18.5V6.5C18.25 5.94772 17.8023 5.5 17.25 5.5H16C16 6.60457 15.1046 7.5 14 7.5H10C8.89543 7.5 8 6.60457 8 5.5Z'
    sound_svg = 'M11 4.9099C11 4.47485 10.4828 4.24734 10.1621 4.54132L6.67572 7.7372C6.49129 7.90626 6.25019 8.00005 6 8.00005H4C3.44772 8.00005 3 8.44776 3 9.00005V15C3 15.5523 3.44772 16 4 16H6C6.25019 16 6.49129 16.0938 6.67572 16.2629L10.1621 19.4588C10.4828 19.7527 11 19.5252 11 19.0902V4.9099ZM8.81069 3.06701C10.4142 1.59714 13 2.73463 13 4.9099V19.0902C13 21.2655 10.4142 22.403 8.81069 20.9331L5.61102 18H4C2.34315 18 1 16.6569 1 15V9.00005C1 7.34319 2.34315 6.00005 4 6.00005H5.61102L8.81069 3.06701ZM20.3166 6.35665C20.8019 6.09313 21.409 6.27296 21.6725 6.75833C22.5191 8.3176 22.9996 10.1042 22.9996 12.0001C22.9996 13.8507 22.5418 15.5974 21.7323 17.1302C21.4744 17.6185 20.8695 17.8054 20.3811 17.5475C19.8927 17.2896 19.7059 16.6846 19.9638 16.1962C20.6249 14.9444 20.9996 13.5175 20.9996 12.0001C20.9996 10.4458 20.6064 8.98627 19.9149 7.71262C19.6514 7.22726 19.8312 6.62017 20.3166 6.35665ZM15.7994 7.90049C16.241 7.5688 16.8679 7.65789 17.1995 8.09947C18.0156 9.18593 18.4996 10.5379 18.4996 12.0001C18.4996 13.3127 18.1094 14.5372 17.4385 15.5604C17.1357 16.0222 16.5158 16.1511 16.0539 15.8483C15.5921 15.5455 15.4632 14.9255 15.766 14.4637C16.2298 13.7564 16.4996 12.9113 16.4996 12.0001C16.4996 10.9859 16.1653 10.0526 15.6004 9.30063C15.2687 8.85905 15.3578 8.23218 15.7994 7.90049Z'

    last_content.ele(f'tag:path@d={sound_svg}').wait.displayed()
    copy_span = last_content.eles(f'tag:path@d={copy_svg}')[-1]
    # print(copy_span)
    copy_span.click()
    tag.wait(0.1)
    content = clipboard.read()
    clipboard.clear()
    return content, get_id_from_url(tag.url)

    # for content_item in content_items:
    #     copy_svg = 'M12 3.5C10.8954 3.5 10 4.39543 10 5.5H14C14 4.39543 13.1046 3.5 12 3.5ZM8.53513 3.5C9.22675 2.3044 10.5194 1.5 12 1.5C13.4806 1.5 14.7733 2.3044 15.4649 3.5H17.25C18.9069 3.5 20.25 4.84315 20.25 6.5V18.5C20.25 20.1569 19.1569 21.5 17.25 21.5H6.75C5.09315 21.5 3.75 20.1569 3.75 18.5V6.5C3.75 4.84315 5.09315 3.5 6.75 3.5H8.53513ZM8 5.5H6.75C6.19772 5.5 5.75 5.94772 5.75 6.5V18.5C5.75 19.0523 6.19772 19.5 6.75 19.5H17.25C18.0523 19.5 18.25 19.0523 18.25 18.5V6.5C18.25 5.94772 17.8023 5.5 17.25 5.5H16C16 6.60457 15.1046 7.5 14 7.5H10C8.89543 7.5 8 6.60457 8 5.5Z'
    #
    #     copy_span = content_item.ele(f'tag:path@d={copy_svg}')
    #     print(copy_span)

if __name__ == '__main__':
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