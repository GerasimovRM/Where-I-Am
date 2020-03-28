from flask_restful import reqparse


class VirtualUser:
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('nickname', required=True)
        self.parser.add_argument('first_name', required=True)
        self.parser.add_argument('middle_name')
        self.parser.add_argument('last_name', required=True)
        self.parser.add_argument('email', required=True)
        self.parser.add_argument('unhashed_password', required=True)