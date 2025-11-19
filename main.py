# ----------------------------------------------------------------------
# 文件名: main.py
# 描述: 负责实例化和编排序列多智能体系统。
# 核心概念: 多智能体系统 (Multi-Agent System)
# ----------------------------------------------------------------------

# 导入所需的代理类（从当前目录导入）
from planner_agent import MealPlannerAgent
from creator_agent import RecipeCreatorAgent

# 导入 Gemini 客户端所需的库
# from google import genai
# import os

# 配置（用于演示的模拟配置）
GEMINI_MODEL = "gemini-2.5-flash"
# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY")) # 实际环境中需要配置API Key

def run_agent_sequence(user_query: str):
    """
    核心概念 1: 序列代理编排 (Sequential Multi-Agent System)
    定义了 Agent 1 和 Agent 2 的执行顺序。
    """
    
    # 1. 初始化代理
    planner = MealPlannerAgent("PlannerAgent", GEMINI_MODEL)
    creator = RecipeCreatorAgent("CreatorAgent", GEMINI_MODEL)
    
    # 模拟会话数据（用于演示记忆的使用）
    session_data = {'user_id': 'user_001', 'query_id': 'q_1', 'user_history': '用户不吃猪肉。'}
    
    # --- Step 1: 规划 (Agent 1) ---
    print(f"\n用户请求: {user_query}")
    print("\n--- 1. 膳食规划 (Agent 1) 启动 ---")
    
    # Agent 1 执行，并返回初步计划
    plan_output = planner.execute(user_query, session_data)
    
    print("-" * 30)
    print(f"Agent 1 输出的初步计划:\n{plan_output}")
    print("-" * 30)
    
    # --- Step 2: 执行和格式化 (Agent 2) ---
    print("\n--- 2. 食谱与清单创建 (Agent 2) 启动 ---")
    
    # Agent 2 执行，将 Agent 1 的输出作为输入
    final_result = creator.execute(plan_output)
    
    print("-" * 30)
    print("✨ 任务完成：请查看最终结果")
    print(final_result)
    print("-" * 30)

if __name__ == "__main__":
    # 测试用例，体现记忆和约束
    test_query = "我想为下周工作日规划晚餐。我正在健身，所以需要高蛋白、低碳水，而且我不吃猪肉。这次的菜品要简单快捷。"

    run_agent_sequence(test_query)
