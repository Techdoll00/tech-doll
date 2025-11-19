# ----------------------------------------------------------------------
# ⚠️ 注意：此代码为展示项目架构和核心概念的骨架，未包含完整的ADK配置和API Key设置。
# ----------------------------------------------------------------------

# 假设我们导入 ADK (Agent Development Kit) 和 Gemini SDK
# from adk.agent import Agent, SessionState
# from adk.tool import GoogleSearchTool
# from adk.memory import InMemorySessionService
# from google import genai
# import os

# # 配置 - 假设这是在 Notebook setup 阶段完成的
# GEMINI_MODEL = "gemini-2.5-flash"
# # client = genai.Client(api_key=os.getenv("GEMINI_API_KEY")) 

# --- 1. 定义工具 ---
# 在 ADK 中，GoogleSearchTool 是内置工具，可以直接添加到 Agent 中。
# 这里我们仅作引用说明。

# --- 2. 定义 Agent 1：膳食规划师 (Planner Agent) ---
class MealPlannerAgent(): # 继承自 Agent 基类
    
    def __init__(self, name: str, model_name: str):
        # super().__init__(name, model_name)
        self.name = name
        
        # 核心概念 3: 会话与记忆
        # self.memory_service = InMemorySessionService() 
        
        # 提示词设计 (Context Engineering)
        self.system_prompt = (
            "你是一名专业的膳食规划师。你的职责是根据用户的健康需求和偏好，"
            "生成一个包含 5 个高蛋白、低碳水菜品的初步列表。你必须利用会话记忆"
            "来排除用户明确不吃的食材。不要提供食谱或配料，只输出清晰的菜品名称列表。"
        )

    def execute(self, user_query: str, session_data: dict) -> str:
        """
        模拟执行逻辑：从用户请求和记忆中获取上下文，生成菜品列表。
        """
        print(f"[{self.name}] 正在检查用户历史偏好...")
        # relevant_history = self.memory_service.get_context(session_data['user_id'])
        
        # 模拟 LLM 调用
        # plan_output = client.models.generate_content(...) 
        
        # 模拟 Agent 1 的输出，作为 Agent 2 的输入
        return "规划列表：高蛋白鸡胸肉沙拉, 素食鹰嘴豆泥卷, 三文鱼配烤芦笋, 烤牛肉蔬菜串, 鸡蛋菠菜饼。"
