from flask import Blueprint, jsonify, request
import boto3
UploadImage_bp = Blueprint('UploadImage_api', __name__, url_prefix='/post-image')


@UploadImage_bp.route('/', methods=['POST'])
def post_images():
    try:
        upload_code1 = request.form['upload_code1']
        upload_code2 = request.form['upload_cose2']
        file = request.files['img_file']
    except Exception as e:
        return jsonify("Nope"), 200

    if(upload_code1 != "KevinLovesAlliesArt" or upload_code2 != "WakesTheMoon"):
        return jsonify("Nope"), 200

    session = boto3.Session(
        aws_access_key_id='AKIAIQQOPOXTHVN37LHA',
        aws_secret_access_key='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',
        region_name='us-east-2'
      )

    s3 = session.client('s3')

    res = s3.put_object(
        ACL='public-read',
        Body=file.stream.read(), 
        Bucket='allies-art-photos', 
        Key=file.filename
    )

    if(res['ResponseMetadata']['HTTPStatusCode'] == 200):
        return jsonify("Success"), 200
    else:
        return jsonify("Nope"), 200

