from flask_marshmallow import Marshmallow
# import app
from vesuvius import ma
# Product Schema
# ma = Marshmallow(app)


class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'qty')


# Init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
