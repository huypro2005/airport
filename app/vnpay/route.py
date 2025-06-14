from flask import Blueprint, request, jsonify
from app.vnpay.vnpay import VNPAY
from datetime import datetime
import uuid
import os
from dotenv import load_dotenv

load_dotenv()
VNPAY_BLUEPRINT = Blueprint('vnpay', __name__)

'''
{
    "price": 100000,
    "order_id": "1234567890"
}

'''
# Link: http://localhost:5000/api/vnpay/create_payment
@VNPAY_BLUEPRINT.route('/vnpay/create_payment', methods=['POST'])
def create_payment():
    data = request.json
    price = data.get('price')
    order_id = data.get('order_id')
    if not price:
        return jsonify({'error': 'Price is required'}), 400
    if not order_id:
        order_id = str(uuid.uuid4())    
    if not price:
        return jsonify({'error': 'Price is required'}), 400
    try:
        vnpay = VNPAY()
        vnpay.requestData['vnp_Version'] = '2.1.0'
        vnpay.requestData['vnp_Command'] = 'pay'
        vnpay.requestData['vnp_TmnCode'] = os.getenv('VNPAY_TMN_CODE')
        vnpay.requestData['vnp_Amount'] = int(price) * 100
        vnpay.requestData['vnp_CurrCode'] = 'VND'
        vnpay.requestData['vnp_TxnRef'] = order_id
        vnpay.requestData['vnp_OrderInfo'] = 'Payment for order'
        vnpay.requestData['vnp_OrderType'] = 'other'
        vnpay.requestData['vnp_Locale'] = 'vn'
        # vnpay.requestData['vnp_BankCode'] = ''
        vnpay.requestData['vnp_CreateDate'] = datetime.now().strftime('%Y%m%d%H%M%S')  # 20150410063022
        print(request.remote_addr)
        vnpay.requestData['vnp_IpAddr'] = request.remote_addr
        print("vnp_IpAddr: ", vnpay.requestData['vnp_IpAddr'])
        vnpay.requestData['vnp_ReturnUrl'] = os.getenv('VNPAY_RETURN_URL')
        vnpay_payment_url = vnpay.get_payment_url(os.getenv('VNPAY_PAYMENT_URL'), os.getenv('VNPAY_HASH_SECRET_KEY'))
        print("vnpay_payment_url: ", vnpay_payment_url)
        return jsonify({'payment_url': vnpay_payment_url, 'status': 'success'})
    except Exception as e:
        return jsonify({'error': str(e), 'status': 'fail'}), 500
    

# Link: http://localhost:5000/api/vnpay/payment_return

@VNPAY_BLUEPRINT.route('/payment_return', methods=['GET'])
def payment_return():
    inputData = request.args
    print("inputData: ", inputData)
    if inputData:
        vnpay = VNPAY()
        vnpay.responseData = inputData.to_dict()
        order_id = inputData['vnp_TxnRef']
        amount = int(inputData['vnp_Amount']) / 100
        order_desc = inputData['vnp_OrderInfo']
        vnp_TransactionNo = inputData['vnp_TransactionNo']
        vnp_ResponseCode = inputData['vnp_ResponseCode']
        vnp_TmnCode = inputData['vnp_TmnCode']
        vnp_PayDate = inputData['vnp_PayDate']
        vnp_BankCode = inputData['vnp_BankCode']
        vnp_CardType = inputData['vnp_CardType']
        if vnpay.validate_response(os.getenv('VNPAY_HASH_SECRET_KEY')):
            if vnp_ResponseCode == "00":
                return jsonify({"title": "Kết quả thanh toán",
                            "result": "Thành công", "order_id": order_id,
                            "amount": amount,
                            "order_desc": order_desc,
                            "vnp_TransactionNo": vnp_TransactionNo,
                            "vnp_ResponseCode": vnp_ResponseCode,
                            "status": "success"})
            else:
                return jsonify({"title": "Kết quả thanh toán",
                            "result": "Lỗi", "order_id": order_id,
                            "amount": amount,
                            "order_desc": order_desc,
                            "vnp_TransactionNo": vnp_TransactionNo,
                            "vnp_ResponseCode": vnp_ResponseCode,
                            "status": "fail"})
        else:
            return jsonify({"title": "Kết quả thanh toán", "result": "Lỗi", "order_id": order_id, "amount": amount,
                           "order_desc": order_desc, "vnp_TransactionNo": vnp_TransactionNo,
                        "vnp_ResponseCode": vnp_ResponseCode, "msg": "Sai checksum",
                           "status": "fail"})
    else:
        return jsonify({"title": "Không có dữ liệu", "result": "",
                        "status": "fail"})