copy_svg = 'M12 3.5C10.8954 3.5 10 4.39543 10 5.5H14C14 4.39543 13.1046 3.5 12 3.5ZM8.53513 3.5C9.22675 2.3044 10.5194 1.5 12 1.5C13.4806 1.5 14.7733 2.3044 15.4649 3.5H17.25C18.9069 3.5 20.25 4.84315 20.25 6.5V18.5C20.25 20.1569 19.1569 21.5 17.25 21.5H6.75C5.09315 21.5 3.75 20.1569 3.75 18.5V6.5C3.75 4.84315 5.09315 3.5 6.75 3.5H8.53513ZM8 5.5H6.75C6.19772 5.5 5.75 5.94772 5.75 6.5V18.5C5.75 19.0523 6.19772 19.5 6.75 19.5H17.25C18.0523 19.5 18.25 19.0523 18.25 18.5V6.5C18.25 5.94772 17.8023 5.5 17.25 5.5H16C16 6.60457 15.1046 7.5 14 7.5H10C8.89543 7.5 8 6.60457 8 5.5Z'
sound_svg = 'M11 4.9099C11 4.47485 10.4828 4.24734 10.1621 4.54132L6.67572 7.7372C6.49129 7.90626 6.25019 8.00005 6 8.00005H4C3.44772 8.00005 3 8.44776 3 9.00005V15C3 15.5523 3.44772 16 4 16H6C6.25019 16 6.49129 16.0938 6.67572 16.2629L10.1621 19.4588C10.4828 19.7527 11 19.5252 11 19.0902V4.9099ZM8.81069 3.06701C10.4142 1.59714 13 2.73463 13 4.9099V19.0902C13 21.2655 10.4142 22.403 8.81069 20.9331L5.61102 18H4C2.34315 18 1 16.6569 1 15V9.00005C1 7.34319 2.34315 6.00005 4 6.00005H5.61102L8.81069 3.06701ZM20.3166 6.35665C20.8019 6.09313 21.409 6.27296 21.6725 6.75833C22.5191 8.3176 22.9996 10.1042 22.9996 12.0001C22.9996 13.8507 22.5418 15.5974 21.7323 17.1302C21.4744 17.6185 20.8695 17.8054 20.3811 17.5475C19.8927 17.2896 19.7059 16.6846 19.9638 16.1962C20.6249 14.9444 20.9996 13.5175 20.9996 12.0001C20.9996 10.4458 20.6064 8.98627 19.9149 7.71262C19.6514 7.22726 19.8312 6.62017 20.3166 6.35665ZM15.7994 7.90049C16.241 7.5688 16.8679 7.65789 17.1995 8.09947C18.0156 9.18593 18.4996 10.5379 18.4996 12.0001C18.4996 13.3127 18.1094 14.5372 17.4385 15.5604C17.1357 16.0222 16.5158 16.1511 16.0539 15.8483C15.5921 15.5455 15.4632 14.9255 15.766 14.4637C16.2298 13.7564 16.4996 12.9113 16.4996 12.0001C16.4996 10.9859 16.1653 10.0526 15.6004 9.30063C15.2687 8.85905 15.3578 8.23218 15.7994 7.90049Z'

def get_headers(id, token):
    headers = {
        'authority': 'chat.openai.com',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'authorization': f'Bearer {token}',
        'content-type': 'application/json',
        # 'cookie': 'oai-did=daa6a260-2311-45fc-9c94-1e7828d0b1ea; cf_clearance=dmFxGyg_U68rOmsErnGu5JEs9dJxvvbC6YtAqqChEMA-1709800279-1.0.1.1-022D04CuAcw1iZNfO8VCjXWmMNRDvWcqhZOmKHAGj4oev0YIDpELwSK9Akcj2zijKyjHJozW5Ct1EbtlrS05tQ; ajs_user_id=daa6a260-2311-45fc-9c94-1e7828d0b1ea; ajs_anonymous_id=eb2f2131-54e6-4f57-9f2a-433461c1dd2f; intercom-device-id-dgkjq2bp=f33f01bd-c750-4458-acbd-4f226475c19f; __cflb=0H28vVfF4aAyg2hkHEuhVVUPGkAFmYvk7pquuh6LfLZ; __cf_bm=QJG85a295GBX67agl8OiRyXLzWQbgz9tR2Qs8zkKNS8-1709815905-1.0.1.1-ZOcX4L3FKNLtpTPsp1U_1RDaFs__0M945DdkBbZ4atxgJtbPim7x0ufI_CBeZdmHBQ0wfnRJGGrcwJTWutRi9g; __Host-next-auth.csrf-token=6ee0f7601517c1ec3534cc4fbf768b637677ca7cb782af31e8e4dad35c5fe755%7C343cb779e78a2720b2be4b5201b8361d9c0e44ebbe34c48d2d2b6eac9c704aad; _cfuvid=Xirw_gDv1z9dNNgtU5DqZp_SQfjYy0wn5WNdrMi6JgI-1709816051415-0.0.1.1-604800000; _uasid="Z0FBQUFBQmw2YnNpbXlBWEFEZkc4c2JGeU9uTGxNX2VXR1lHSFNvUlhoYmxqcmdrZ3hXVE03YWlkZXNhLURSNGV5b3VVY0tSek92WmJfZnlOMHllZnRZNkhSVGFYN0liRXVCSEpycjE3SHJwWmN1UkJEU3RPYkRTakpyazlZeDg3dHVBN2ozUXZsZVNadVpLOXpGbDNZalhWQV90aDNDRHVJcTg2eWZ0VzVVTkhiSFRBWGtfXzlUalp4a1JnMkx0V0lsMEhrS2o0cWRkcGFYMnhvYjVGRU9BZlFjdDJPeTlnTDZsdWNYUkI4YVVIMTN2SVktVm1fWjVyVlpYeHJTUWpGWUtYUEhUblVuWmM0T1lVdjZiV2JLTmR6RGxyWUpueHhmX05oQU1jcFZULXNXNkJ1VU1FX3JuOVg0Sno4ZUlnMXJpV25KWFhHVUgzaURoLW5tQnZQMllvMmk3Sm04S01BPT0="; _umsid="Z0FBQUFBQmw2YnNpTUlqMXpVd0NtcGpWUVA0OFJNSUMyeS1yYVVzNm1uNkxJNkR2OFJuVEdCOXBZa2REZlpCWjNremV3UEQ1dzdoams3UWZTSUJKVWlzeTVuZ3d5dDVMTlNiT1hxeDduVENtYjdQMXRsN05EUktZNUhrWFpQc1NXZUJqc2RvRk9NMzh1MkRuWERTV2VhZmF1RUZ0LTJnVjJNZDFqeFlGQXV6YkI5YVN6aWFjSmJIRnpjd0NVRFRTM2VycDFTNkl6OG5HckRKa21GdjRTbGxNQ2x5VXI2U2c3eFBfaUh0VHl0c2M2MEJuSmwtNFVoMD0="; __Secure-next-auth.callback-url=https%3A%2F%2Fchat.openai.com; __Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..k4_px6kFWbRg0iR-.mEPbxCsMm7DoAwzvnScX_g8feVgffwzlw_vijJXw_w6p4yB7NSM8OHa36mVPCJ6r76562FmhDfvotfBrnQ7EJ3S8ZVWUsVu8XO6QvAEOYX3ElZ500ITIGcYAWrOXUeA5ryM5Vr_pg24LZ98o739ba1xb2FrGhcjw-2NfL7yAR_j9QRJOAEvMPSdS5Zly6wn-9w_sxAXI6jzmBX3Vm1xW27W4N9C2cjIvf6ZbqgDAVEkUHIrsrs0jRd0gJxpGUgjU5T_0x7mH_9AlFu8atGf7Kj7QCWfCMPaTAvTOiJ2TO5lQp0UPcLJND8GuHsd16T6TDqQCeyMsRuBY7E6ZtUmr7yaLvnhqfRcrQjLo3-0kX6MgWsRuGiGwlS2AUBYJAo2fjC_sNsMkPL_mxNJLODTvvwEcbePIiVFtYeSFhvM515rDHBGrGg84InwZu1E6TMxHmmn5KbdNtdLVF1asQ3TBra4VXbMxEuyudQQwuSDStPodQmS-1G4zQeFVoAjWc4A9lwohz4DT49qOKebv2i2fOJCV-1HWCpkG5kDtrj8oYtJ-h-yEfYdV-fMIHqPyBVw9y8DNXtduA-qcUZAUbRQZyUCyYsRC7GvkFopZgDZfcj0ZAAEsLgnLY98KaMRTlDUIZwn9vpWw5TVAwolO7pZNebBjeFfNgO3W47Ai2qO_58WxPqJx8VJQjG0ecLvzXDeVLm62MoxDZ7so1FJDlYOLtKZNZZL4HZO8H9PmQx9qKy3E4K_kZDwfFQKVQzlhohCw5M6wNkPjEm91yneicGOi2CmifuAJ8lmV36PD5FieADWv5OsKBJlCE71BRaCxychNCbgou0GZt93v4lVMV3VxvGadJF7dINmkFXy2ChC68-h-YuhPTXOQNiSYtc7_wRlJm5r6jH_GpUjxyhGFcAN7BgwvnoeI_2jGgdR232_ZrRxcm7ra6tT2qBqfziRhCONmPC9HHgMDn6tr-Ghh4an02c2iYukKaqL1vJjU9FbZaEgJurlgZ7d5YmO4qV-r4RynWqJxgbxd6mnZbOZZWvjgGc7zbtvDzHToCLESAocJueLR8xAl2KX1rtMVVs_kEwhPT3X1BSFQscXw7l22EunKXN4rxxxa2sGGcr05u3uhvnc5QalDHF95JJuyLeHXHUFmQtfYTzgL5_ZiisoRmc75Zlb5Bb7pwSZy2n_Pl68abgyuKYuhlYq6zuPvkaDCDYsulAqvgzkqZtExGgYAN8aYEAUIcYj6LLLOLRF4T8z6B36gEVKZ9OM5jEElDjAMDIV36JuMwBZjP26DSP27hMCOALDNnVcFepTWJYbJtkwjWSvobkSgkKXcLkxkBk4RlChgN7Rav7FlEOL_m1EhUGxxIvetNh2XAGThIHV5P82I5hXNVZU8SyrCcJwa-xBx3hf8ZTyJIHcgRywRVVrKdvHIpMKA7ozujyKDHwA2sqnTBkqoz5M_TqMCXDigGJTgQrKivnR_sjLSn0MmdENHs7Ph0IqQK3kXof06RKT1YtJBSpibz-Us1OEnWwm2hhKNgq2Jty4OLb8waYzqjx7PXpIowFvrPznkKLBW8CyD6ms4XPy8Ha6RNzhzVGGAPY8xW05AWQOCj9M2A-RmcTCpaJwEvZE88sXHav8JUV7lT5HSEMOvxtanWMtp6mIfXFEH3ME-VNSlHnJe_OS73uP5AQZ8Kj28rlvpkjlkpHPKmx7pffm0etlz4Ps-Fo6kNiRItvxt1qPcv-2_4b_cOJ8NAT7RcSF-bKgncxCyrw-zzHcho1uaTMIOdfpoivv2nIIFeKI-oxeZnfVTNbD2LadPfD_-Y5SGDVPL3iIXpqbjhlyD_0y4YS99vgHcHF-_bBg8-lhibifwJMq9pBOp7QPBPdGu3xMzMjrSUzA5d7b-yKdNUhT6eBQXn4jEtkD-N5lf0iQjRFODS5Y9nYpAgeB-9DVt-trJt-h8mQQTf9ciO69wtVKd_4sXM80gVZAxH9EymOuPDBLAuIamo_6_9ptRQ09oESHv4CfVpXK3FYzOrlpfn8oodk0dlIMGNpY7DNaIus4I2_72BhGG4btYy5WKyRBxt-vaDy_45dCe9vvp21gbVZRsXAxBgrHV1_hhCZRMuaA8HoQPly3iYgE40eqd_eegJspkgvHpJVoJDRhdPn-eBTSTpVYJMXRua0nZKEU-xY1CZjmt_W0ubmH0XJK_bQqyJzu2QHVfa5fVgA6LueKlm56DsC1A0ymPMsNjZmSys8E3Ji-KjH7l3CSkx-yuhDXBm99jzh0nPwnYOGbHVz1uLy_Vfek2wOwt8MwK7YkIAlBSurX10fhgdgB6gFvhkiY1Iwvffr0BJi14RxVTdFUy6jKb_c-2pFil6zxImKfhBVmUpCdyNO8rzJv4SfQIROQ8DJUk5ceX1_I92z33b6SPUAcXqaR40jqlgWK55aHEPxfZzbB7lCOxcIxh3bPqWm6BHUrTkRit4ttdDwujQ8LCOLs5ZdjaXjd9C3L2fy6_8xGDTMTjocOWcQ954lpjSSEqALv5g8DJA6B19vbHPoF5uJLTqj6qpW2E0OJAkzsioftFQX0Sq0o5qoQvDeB3CpY85aKymXl8vxXbTJUMwkY1MMiOpo5k8WJUVjTIUt67JYtTgNdJs-qu94jz-WLOPW6g4or8VnwAt3UDAb9Isu87N4TCLxNyuD-tiWevHj0TlgSYFTZzzy6GXd3b289KIQLBgbCMGAwtTF8w26cRMSYabs4o7AVDSl2LRMPbREJNzj2etTSBSkDIG-oRO15-JeSeBNuNTLh6l2nom4gEDIV8vlDQUlvNSH-Vv7FgdNfr-l2u0R8pn8-8YdBKgK6nAoPR96eN6hWYzluGQglxAnVYcnUjvPknyrMk9uvT3Fq8xKwjXbYvrsvUwLHE5dg8-bNqrEMQtohtPez22y6T9Hkvx-CLeP96oCEvlGzT.9hixKeDLuGRor89OwEcpEg; _puid=user-tp7gJezPvHomPYAbYs4pSHwe:1709816675-yXoX%2FJIEY%2BkKMvrYvKm8UMBqfjzMrx0xJ9%2FdBy7RJWA%3D; intercom-session-dgkjq2bp=dnhJejk4Zzl3cy9RZHpkMkpxU0pUSGlxM0orRjhYdnBQU0R6bThjOERvanhUUEVUNnZwSnZTT2tYWHZTb2ZMVC0tWDFyZ3FrQlR1d0E1TVJtUFBpS0lsZz09--75ffd17be762bcec08f8a86cd6390287d4a039a4; _dd_s=rum=0&expire=1709817622568',
        # 'oai-device-id': 'daa6a260-2311-45fc-9c94-1e7828d0b1ea',
        'oai-language': 'en-US',
        'origin': 'https://chat.openai.com',
        'referer': f'https://chat.openai.com/c/{id}',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    return headers