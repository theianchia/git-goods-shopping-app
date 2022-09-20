from flask import Flask, request, jsonify
from flask_cors import CORS
import order_controller

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
  return 'Order connected'


@app.route('/get-all-orders')
def get_all_orders():
  return jsonify(order_controller.get_all_orders())


@app.route('/get-orders-by-email', methods=['POST'])
def get_orders_by_email():
  data = request.get_json()
  email = data['email']

  res = order_controller.get_orders_by_email(email)
  return res["Items"]


@app.route('/add-order', methods=['POST'])
def add_order():
  data = request.get_json()
  email = data['email']
  items_dict = data['items']

  res = order_controller.add_order(email, items_dict)
  if res["ResponseMetadata"]["HTTPStatusCode"] == 200:
    return jsonify(
      {
        "code": res["ResponseMetadata"]["HTTPStatusCode"],
        "message": "Order has been added successfully"
      }
    ), 200

  return jsonify(
    {
      "code": res["ResponseMetadata"]["HTTPStatusCode"],
      "message": "Bad request"
    }
  ), res["ResponseMetadata"]["HTTPStatusCode"]


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5002, debug=True)
