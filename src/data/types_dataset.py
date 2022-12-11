import numpy as np
import pandas as pd

types_train = {
    "tag_id": np.int32,
    "post_id": np.int32,
    "product_id": np.int32,
    "user_id": np.int32,
    "date_tag": np.datetime64,
    "color": np.int8,
    "click_count": np.int16,
    "product_info": "object",
    "description": "object",
    "brand_name": "object",
    "date_joined": np.datetime64,
    "country": "category",
}
