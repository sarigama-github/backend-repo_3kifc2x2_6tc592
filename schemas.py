"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field
from typing import Optional, List

# Example schemas (replace with your own):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Gold shop specific schemas

class GoldItem(BaseModel):
    """
    Gold items for sale (bars, nuggets)
    Collection name: "golditem"
    """
    name: str = Field(..., description="Name of the gold item")
    type: str = Field(..., description="bar or nugget")
    purity: float = Field(..., ge=0, le=24, description="Purity in karats (e.g., 24)")
    weight_grams: float = Field(..., gt=0, description="Weight in grams")
    price_usd: float = Field(..., gt=0, description="Price in USD")
    image: Optional[str] = Field(None, description="Image URL for the item")
    three_d_url: Optional[str] = Field(None, description="Spline/3D scene URL to render")
    in_stock: bool = Field(True, description="Whether item is available")
    badge: Optional[str] = Field(None, description="Optional label like 'Best Seller'")

class OrderItem(BaseModel):
    item_id: str
    quantity: int = Field(..., gt=0)

class Order(BaseModel):
    """
    Orders placed by customers
    Collection name: "order"
    """
    customer_name: str
    customer_email: str
    shipping_address: str
    items: List[OrderItem]
    notes: Optional[str] = None
