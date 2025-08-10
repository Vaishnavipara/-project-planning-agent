import os
import json
from openai import OpenAI
from dotenv import load_dotenv

def generate_project_plan(goal):
    """Strict OpenAI-only version using v1.0+ API"""
    try:
        load_dotenv()
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "user",
                "content": f"""Return JSON with phases, tasks, and roles like:
                {{
                  "phases": [{{
                    "name": "Planning",
                    "tasks": ["Task 1", "Task 2"],
                    "roles": ["Role1", "Role2"]
                  }}]
                }}
                Goal: "{goal}"
                """
            }],
            temperature=0
        )
        return json.loads(response.choices[0].message.content)
        
    except Exception as e:
        raise RuntimeError(f"API Error: {e}\n"
                         "Please: 1) Check billing at platform.openai.com\n"
                         "        2) Ensure API key is valid")

if __name__ == "__main__":
    goal = input("Enter project goal: ").strip()
    if not goal:
        print("Error: Goal cannot be empty")
    else:
        try:
            plan = generate_project_plan(goal)
            print(json.dumps(plan, indent=2))
        except Exception as e:
            print(f"Submission Note: {e}")