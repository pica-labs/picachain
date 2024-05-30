from typing import Any, Union

from picachain.pydantic import BaseModel


class Document(BaseModel):
    content: Union[str, Any]
    metadata: dict
