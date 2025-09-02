from openai import AsyncOpenAI


class OpenAIClient:
    """Simple client for OpenAI API interactions."""


    def __init__(self, api_key: str, system_prompt: str, model: str = "gpt-3.5-turbo"):
        self._client = AsyncOpenAI(api_key=api_key)
        self._system_prompt = system_prompt
        self._model = model

    async def generate_summary(self, text: str) -> str:
        """Generate summary using OpenAI API."""

        response = await self._client.chat.completions.create(
            model=self._model,
            messages=[
                {"role": "system", "content": self._system_prompt},
                {
                    "role": "user",
                    "content": (
                        f"Please provide a comprehensive summary of the"
                        f" following document:\n\n{text}"
                    )
                    },
                ],
            temperature=0.2,
            )

        return response.choices[0].message.content