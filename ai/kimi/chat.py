from openai import OpenAI
import configparser
import os

class KimiChat:
    temperature = 0.3
    content = '你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。'
    
    def __init__(self, temperature=0.3):
        self.temperature = temperature
    
    def chat(self, question):
        api_key = self.get_api_key()
        if not api_key:
            return "配置文件读取失败，无法获取API密钥"
        client = OpenAI(
            api_key=self.get_api_key(),
            base_url="https://api.moonshot.cn/v1",
        )
        try:
            completion = client.chat.completions.create(
                model="moonshot-v1-8k",
                messages=[
                    {"role": "system", "content": self.content},
                    {"role": "user", "content": question}
                ],
                temperature=self.temperature,
                stream=True,
            )
        except Exception as e:
            print(f"OpenAI API调用失败: {e}")
            return None
        
        for chunk in completion:
            delta = chunk.choices[0].delta
            if delta.content:
                print(delta.content, end="")
            else:
                print("OpenAI API调用失败")

        return None
    def get_api_key(self):
        # 使用环境变量或默认路径来获取配置文件
        config_path = os.environ.get('CONFIG_INI_PATH', '/Users/zhanghongjian/work/code/tools/python/ai/config.ini')
        config = configparser.ConfigParser()
        config.read(config_path)
        try:
            return config.get('kimi', 'apikey')
        except (configparser.NoSectionError, configparser.NoOptionError) as e:
            print(f"配置文件读取失败: {e}")
            return None

kimichat = KimiChat()
ansk = kimichat.chat("请写一篇关于人工智能的论文")