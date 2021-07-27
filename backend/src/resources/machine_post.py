from flask_restful import Resorce, reqparse
from models.machine_post import MachinePostModel
from models.machine import MachineModel
from sqlalchemy.exc import SQLAlchemyError

class MachinePost(Resorce):
  parser = reqparse.RequestParser()
  parser.add_argument('title', type=str, required=True, help='This field is required.')
  parser.add_argument('content', type=str, required=True, help='This field is required.')
  parser.add_argument('author', type=str, required=True, help='This field is required.')
  parser.add_argument('machine_id', type=int, required=True, help='This field is required.')

  def get(self, _id):
    post = MachinePostModel.find_by_id(_id)

    if post:
      return post.json(), 200

    return {'message': 'Machine_Post not found.'}, 400


  class MachinePosts(Resorce):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, required=True, help='This field is required.')
    parser.add_argument('content', type=str, required=True, help='This field is required.')
    parser.add_argument('author', type=str, required=True, help='This field is required.')
    parser.add_argument('machine_id', type=int, required=True, help='This field is required.')

    def get(self):
      return {'machine_posts': [post.json() for post in MachinePostModel.query.all()]}

    def post(self):
      data = MachinePost.parser.parse_args()

      post = MachinePostModel(**data)
      try:
        post.save_to_db()

      except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return error, 500
      
      return post.json()