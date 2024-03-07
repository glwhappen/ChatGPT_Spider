import pyperclip
import time

class ClipboardManager:
    def __init__(self, id):
        self.id = id
        # 使用一个复杂的分隔符来区分ID和内容
        self.delimiter = ":=+x+:=:"

    def write(self, content, sync=False):
        if sync is False:
            pyperclip.copy(content)
        else:
            formatted_content = f"{self.id}{self.delimiter}{content}"
            while True:
                current_content:str = pyperclip.paste()
                # 检查剪切板是否空或者是否包含当前ID的内容
                if current_content.find(self.delimiter) == -1 or current_content.startswith(f"{self.id}{self.delimiter}"):
                    pyperclip.copy(formatted_content)
                    break
                else:
                    print("其他剪切板正在操作，内容：", current_content)
                    # 如果检测到其他ID的信息，等待1秒钟再次检查
                    time.sleep(1)

    def read(self, sync=False):
        if sync is False:
            current_content: str = pyperclip.paste()
            return current_content
        else:
            while True:
                current_content:str = pyperclip.paste()
                # 检查剪切板是否空或者是否包含当前ID的内容
                if current_content.startswith(f"{self.id}{self.delimiter}"):
                    if current_content.startswith(f"{self.id}{self.delimiter}"):
                        # 从剪切板内容中提取实际内容
                        return current_content.split(self.delimiter, 1)[1]
                else:
                    print("其他剪切板正在操作，内容：", current_content)
                    # 如果检测到其他ID的信息，等待1秒钟再次检查
                    time.sleep(1)


    def clear(self, sync=False):
        if sync is False:
            pyperclip.copy("")  # 清空剪切板
        else:
            while True:
                current_content:str = pyperclip.paste()
                # 检查剪切板是否空或者是否包含当前ID的内容
                if current_content.find(self.delimiter) == -1 or current_content.startswith(f"{self.id}{self.delimiter}"):
                    pyperclip.copy("")  # 清空剪切板
                    break
                else:
                    print("clear 其他剪切板正在操作，内容：", current_content)
                    # 如果检测到其他ID的信息，等待1秒钟再次检查
                    time.sleep(1)

# 示例使用
if __name__ == "__main__":
    content = "Hello, World!"
    clipboard = ClipboardManager("123")

    clipboard.write(content)
    print("Clipboard content after writing:", clipboard.read())
    clipboard.clear()
    # print("Clipboard content after clearing:", clipboard.read())
