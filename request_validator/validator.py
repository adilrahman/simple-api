from flask_restx import fields


def get_ping_body_validator(api):
    ping_body_validator = api.model(
        "Ping",
        {
            "data": fields.String(required=True),
        },
    )

    return ping_body_validator  
