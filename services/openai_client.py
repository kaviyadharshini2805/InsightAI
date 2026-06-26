import os
import openai
import logging

logger = logging.getLogger(__name__)

# ── Environment variables ────────────────────────────────
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
PLAN_MODEL = os.getenv("OPENAI_PLAN_MODEL", DEFAULT_MODEL)

# ── Lazy client initialisation ──────────────────────────
_client = None

def get_client():
    global _client
    if _client is None:
        if not OPENAI_API_KEY:
            raise ValueError(
                "OPENAI_API_KEY is not set. Please set it in your .env file "
                "or as an environment variable."
            )
        _client = openai.OpenAI(api_key=OPENAI_API_KEY)
    return _client

def get_completion(
    prompt: str,
    temperature: float = 0.7,
    max_tokens: int = 1500,
    use_plan_model: bool = False
) -> str:
    """
    Get a completion from OpenAI.
    """
    model = PLAN_MODEL if use_plan_model else DEFAULT_MODEL
    try:
        client = get_client()
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        logger.error(f"OpenAI API error (model={model}): {e}")
        return f"Error generating response: {e}"