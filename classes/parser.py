from flask import Flask
from flask_restful import reqparse


class Parser():
    def parseThis(thing):
        parser = reqparse.RequestParser()
        parser.add_argument('serialNumber', required=False, type=str)
        parser.add_argument('modelNumber', required=False, type=str)
        parser.add_argument('assetTag', required=False, type=str)
        parser.add_argument('customer', required=False, type=str)
        args = parser.parse_args()
        return args
    

    def partsParse(thing):
        parser = reqparse.RequestParser()
        parser.add_argument('_id', required=True, type=int)
        parser.add_argument('parts', required=True, type=list)
        return parser.parse_args()