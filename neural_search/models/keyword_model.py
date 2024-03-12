from pydantic.v1 import BaseModel, Field, Extra

class Keywords(BaseModel):
    keywords: list[str] = Field(description="list of similar keywords regarding to original keyword")

    class Config:
        extra = Extra.forbid