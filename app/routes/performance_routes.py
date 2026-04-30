from flask import Blueprint, request, jsonify

performance_routes = Blueprint('performance_routes', __name__)

# In-memory storage for performance metrics and configurations
performance_metrics = []
weight_configurations = {}

@performance_routes.route('/metrics', methods=['POST'])
def record_metric():
    data = request.json
    # Validate and record performance metric
    performance_metrics.append(data)
    return jsonify({'message': 'Metric recorded successfully!'}), 201

@performance_routes.route('/metrics', methods=['GET'])
def get_metrics():
    return jsonify(performance_metrics), 200

@performance_routes.route('/score', methods=['GET'])
def calculate_score():
    # Calculate a score based on recorded metrics (add your scoring logic here)
    score = sum(metric.get('value', 0) for metric in performance_metrics)
    return jsonify({'score': score}), 200

@performance_routes.route('/weights', methods=['PUT'])
def update_weights():
    data = request.json
    # Update weight configurations
    weight_configurations.update(data)
    return jsonify({'message': 'Weights updated successfully!'}), 200

@performance_routes.route('/weights', methods=['GET'])
def get_weights():
    return jsonify(weight_configurations), 200
