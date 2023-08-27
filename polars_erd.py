import polars as pl
import patito as pt
from erdantic import erd
from erdantic.exceptions import UnknownFieldError
from erdantic.pydantic import PydanticModel
from patito.pydantic import ModelMetaclass
from erdantic.erd import Edge
from typing import Literal, Optional


def create_pydantic_model(models: list[ModelMetaclass]) -> list[PydanticModel]:
    pydantic_models = [erd.adapt_model(model) for model in models]
    return pydantic_models

def create_erd_edges(
    source_models: list, source_fields: list[str], target_models: list
) -> list[Edge]:
    source_models = create_pydantic_model(source_models)
    target_models = create_pydantic_model(target_models)

    edges = []
    for source, source_field, target in zip(
        source_models, source_fields, target_models
    ):
        for field in source.fields:
            if field.name == source_field:
                edges.append(Edge(source=source, source_field=field, target=target))

    return edges
