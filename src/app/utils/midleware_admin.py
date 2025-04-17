from flask_jwt_extended import jwt_required, get_jwt
from flask import jsonify


def admin_required(fn):
    from functools import wraps

    @wraps(fn)
    @jwt_required()
    def wrapper(*args, **kwargs):
        jwt_data = get_jwt()
        if not jwt_data.get("is_admin", False):
            return jsonify({"msg": "Admin access required"}), 403
        return fn(*args, **kwargs)

    return wrapper