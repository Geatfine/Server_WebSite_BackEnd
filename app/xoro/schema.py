from marshmallow import Schema, fields

class GitHubRepoSchema(Schema):
    id = fields,Int(requiered=True)
    repo_name = fields.Str()
    full_name = fields.Str()
    description = fields.Str()

class XoroSchema(GitHubRepoSchema):
    user_id = fields.Email(requiered=True)

