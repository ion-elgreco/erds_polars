import polars as pl
import patito as pt
from erdantic import erd
from polars_erd import create_pydantic_model, create_erd_edges

class Product(pt.Model):
    product_id: int = pt.Field(dtype=pl.Int32)
    name: Optional[str]
    temperature_zone: Literal["dry", "cold", "frozen"]
    demand_percentage: float

class Sales(pt.Model):
    sales_id: int
    product_id: list[int] = pt.Field(dtype=pl.Int32)
    quantity: int
    price: float

models = create_pydantic_model([Product, Sales])
edges = create_erd_edges(
    source_models=[Sales], source_fields=["product_id"], target_models=[Product]
)

erd.EntityRelationshipDiagram(
    models=models, edges=edges
)
