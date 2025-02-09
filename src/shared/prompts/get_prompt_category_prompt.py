from shared.constants.prompts import PROMPT_CATEGORIES

def get_prompt_category_prompt(prompt: str) -> str:
    return f'''
You are a categorizer assistant.
Please categorize following prompt in one of these categories: {', '.join(PROMPT_CATEGORIES)}.
As a response return only one category name.
No interpunction, no comments, no thought process.
<prompt>{prompt}</prompt>
'''.strip()