from flask import Blueprint, jsonify, request
import boto3
LoadImages_bp = Blueprint('LoadImages_api', __name__, url_prefix='/get-images')


@LoadImages_bp.route('/', methods=['GET'])
def get_images():
    files = []
    
    session = boto3.Session(
        aws_access_key_id='AKIAIQQOPOXTHVN37LHA',
        aws_secret_access_key='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',
        region_name='us-east-2'
      )

    s3 = session.client('s3')

    object_listing = s3.list_objects_v2(Bucket='allies-art-photos')
    for o in object_listing['Contents']:
      files.append("https://allies-art-photos.s3.us-east-2.amazonaws.com/"+o['Key'])

    return jsonify(files), 200

