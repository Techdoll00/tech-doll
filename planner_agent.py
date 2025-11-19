# ----------------------------------------------------------------------
# 文件名: planner_agent.py
# 描述: Agent 1 - 负责根据用户偏好和会话记忆生成初步的菜品列表。
# 核心概念: 会话与记忆 (Session & Memory)
# ----------------------------------------------------------------------

# 导入 ADK 和 Gemini 客户端所需的库（实际环境中需要安装）
# from adk.agent import Agent, SessionState
# from adk.memory import InMemorySessionService
# from google import genai 

class MealPlannerAgent(): # 继承自 Agent 基类 (假设)
    
    def __init__(self, name: str, model_name: str):
        # super().__init__(name, model_name)
        self.name = name
        # 核心概念 3: 会话与记忆 - 在实际环境中，这里会实例化记忆服务
        # self.memory_service = InMemorySessionService() 
        
        # 提示词设计 (Context Engineering)
        self.system_prompt = (
            "你是一名专业的膳食规划师。你的职责是根据用户的健康需求和偏好，"
            "生成一个包含 5 个高蛋白、低碳水菜品的初步列表。你必须利用会话记忆"
            "来排除用户明确不吃的食材。不要提供食谱或配料，只输出清晰的菜品名称列表。"
        )

    # Agent 1 不需要工具

    def execute(self, user_query: str, session_data: dict) -> str:
        """
        模拟执行逻辑：从用户请求和记忆中获取上下文，生成菜品列表。
        
        Args:
            user_query: 用户的初始请求。
            session_data: 模拟或实际的会话数据，用于提取用户ID和历史偏好。
        
        Returns:
            初步的菜品列表字符串。
        """
        print(f"[{self.name}] 正在检查用户历史偏好...")
        # 在实际环境中，我们会在这里调用记忆服务来获取历史上下文：
        # relevant_history = self.memory_service.get_context(session_data['user_id'])
        
        # 模拟 LLM 调用，将用户请求和历史偏好发送给 Gemini
        # plan_output = client.models.generate_content(...) 
        
        # 模拟 Agent 1 的输出，作为输入传递给 Agent 2
        initial_plan = "规划列表：高蛋白鸡胸肉沙拉, 素食鹰嘴豆泥卷, 三文鱼配烤芦笋, 烤牛肉蔬菜串, 鸡蛋菠菜饼。"
        return initial_plan
