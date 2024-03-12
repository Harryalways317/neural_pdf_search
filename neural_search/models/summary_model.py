from pydantic.v1 import BaseModel, Field, Extra

class Summary(BaseModel):
    content: str = Field(description="summary generated for the entire context")

    class Config:
        extra = Extra.forbid