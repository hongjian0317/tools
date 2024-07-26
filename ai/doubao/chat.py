from openai import OpenAI
import configparser
import os

class DobaoChat:
    content = '你是豆包，是由字节跳动开发的 AI 人工智能助手'
    api_key=''
    model=''
    base_url=''
    """
    初始化函数。
    Args:
        无。
    Returns:
        无返回值。
    """
    def __init__(self):
        list=self.get_config()
        self.api_key=list[0]
        self.model=list[1]
        self.base_url=list[2]
        pass

    """
    与OpenAI的聊天模型进行交互，生成对指定问题的回答。
    Args:
        question (str, optional): 提问的问题，默认为""。
    Returns:
        None. 该函数直接打印出聊天模型生成的回答。
    Raises:
        无直接异常抛出，但在API调用失败时会打印错误信息。
    """
    def chat(self, question='你好'):
        client = OpenAI(
            api_key=self.api_key,
            base_url="https://ark.cn-beijing.volces.com/api/v3",
        )

        try:
            completion = client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.content},
                    {"role": "user", "content": question},
                ],
                stream=True
            )

            for chunk in completion:
                if not chunk.choices:
                    continue
                print(chunk.choices[0].delta.content, end="")
        except Exception as e:
            print(f"OpenAI API调用失败: {e}")

    """
    从配置文件中获取API密钥。
    Args:
        无参数。
    Returns:
        str: 从配置文件中读取到的API密钥，如果读取失败则返回None。
    Raises:
        无异常抛出，但会在读取失败时打印错误信息。
    """
    def get_config(self):
        config_path = os.environ.get('CONFIG_INI_PATH', 'ai/config.ini')
        config = configparser.ConfigParser()
        config.read(config_path)
        try:
            return [config.get('doubao', 'apikey'),config.get('doubao', 'model'),config.get('doubao', 'url')]
        except (configparser.NoSectionError, configparser.NoOptionError) as e:
            print(f"配置文件读取失败: {e}")
            return None

# 创建实例并调用chat方法
chat = DobaoChat()
chat.chat('请写一篇关于人工智能的论文')

