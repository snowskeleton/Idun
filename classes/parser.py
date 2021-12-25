from flask import Flask
from flask_restful import Resource, Api, reqparse


def parseThis(thing):
    parser = reqparse.RequestParser()
    parser.add_argument('serialNumber', required=False, type=str)
    parser.add_argument('modelNumber', required=False, type=str)
    parser.add_argument('assetTag', required=False, type=str)
    parser.add_argument('customer', required=False, type=str)
    args = parser.parse_args()
    return args
