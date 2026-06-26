import logging
from typing import Dict, Any
from services.openai_client import get_completion

class EditorAgent:
    def edit_section(self, section_name: str, current_text: str, user_instruction: str) -> str:
        prompt = f"""
        You are an editor. Rewrite the following {section_name} section based on the user's instruction.

        Current section:
        {current_text}

        User instruction: {user_instruction}

        Return only the revised section.
        """
        response = get_completion(prompt, temperature=0.4)
        return response