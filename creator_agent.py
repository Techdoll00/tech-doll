# ----------------------------------------------------------------------
# 文件名: creator_agent.py
# 描述: Agent 2 - 负责接收菜品列表，调用工具查找细节，并格式化输出购物清单。
# 核心概念: 工具 (Tool)
# ----------------------------------------------------------------------

# 导入 ADK 和 Google Search 工具所需的库
# from adk.agent import Agent, SessionState
# from adk.tool import GoogleSearchTool 
# from google import genai 

class RecipeCreatorAgent(): # 继承自 Agent 基类 (假设)

    def __init__(self, name: str, model_name: str):
        # super().__init__(name, model_name)
        self.name = name
        
        # 核心概念 2: 工具 - 在实际环境中，这里会添加 Google Search 工具
        # self.add_tool(GoogleSearchTool()) 
        
        self.system_prompt = (
            "你是一个执行型代理。你的输入是一个菜品名称列表。你的职责是调用 Google Search Tool"
            "来查找每个菜品的详细配料，然后将所有配料整合，生成一个统一的、Markdown 格式的'食材采购清单'。"
            "最后，附上每个菜品的简单食谱。你的输出必须结构清晰，方便用户阅读。"
        )

    def execute(self, plan_input: str) -> str:
        """
        模拟执行逻辑：解析输入，调用工具，格式化输出。
        
        Args:
            plan_input: Agent 1 的输出（菜品列表）。
            
        Returns:
            最终格式化的购物清单和食谱。
        """
        # plan_input 是 Agent 1 的输出 (菜品列表)
        print(f"[{self.name}] 正在解析计划并调用 Google Search 工具查找食谱...")
        
        # 核心概念 2: 工具使用 - 模拟调用工具的逻辑
        # dishes = plan_input.replace("规划列表：", "").split(", ")
        # for dish in dishes:
        #     search_result = self.tool.execute(f"详细的 {dish} 食谱和配料")
        #     # ... 收集和整理配料
            
        # 模拟最终格式化输出，这是代理最终向用户呈现的价值
        final_output = (
            "\n"
            "## ✅ 最终输出：智能美食计划\n"
            "\n"
            "### 🛒 食材采购清单 (统一整理)\n"
            "| 食材 | 单位/数量 | 备注 |\n"
            "| :--- | :--- | :--- |\n"
            "| 鸡胸肉 | 500 克 | 高蛋白！|\n"
            "| 鹰嘴豆 | 1 罐 | 素食选项 |\n"
            "| 三文鱼排 | 3 块 | |\n"
            "| 芦笋 | 1 捆 | |\n"
            "\n"
            "### 🍽️ 详细食谱\n"
            "#### 高蛋白鸡胸肉沙拉\n"
            "**配料:** 鸡胸肉、生菜、番茄、橄榄油...\n"
            "**步骤:** (基于工具搜索结果的步骤)\n"
        )
        return final_output
