from openai import BaseModel


class OpenAISettings(BaseModel):

    model: str
    api_key: str
    temperature: float
