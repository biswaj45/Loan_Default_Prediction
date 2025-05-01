# import pickle
# from flask import Flask, render_template, app, request, url_for, jsonify
# import numpy as np
# import pandas as pd
# from data_preprocessing import FullLoanPreprocessor

# app = Flask(__name__)
# catboost_model = pickle.load(open('catboost_model_version_1.pkl', 'rb'))
# scalar = pickle.load(open('data_scaling_latest.pkl', 'rb'))
# preprocessor = pickle.load(open('data_preprocessing.pkl', 'rb'))

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/predict_api', methods=['POST'])


# def predict_api():
#     data = request.json['data']
#     print(data)
#     #print(np.array(list(data.values())).reshape(1, -1))
#     #new_tran_data = scalar.fit_transform(np.array(list(data.values())).reshape(1, -1))
#     df = pd.DataFrame([data])
#     processed_data = preprocessor.transform(df)
#     new_tran_data = scalar.transform(processed_data)
#     output = catboost_model.predict(new_tran_data)
#     print(output[0])
#     if output[0] == 1:
#         prediction = 'Y'
#     else:
#         prediction = 'N'
#     return jsonify(prediction)


# if __name__ == '__main__':
#     app.run(debug=True)


# import pickle
# from flask import Flask, render_template, request, url_for, jsonify
# import numpy as np
# import pandas as pd
# from data_preprocessing import FullLoanPreprocessor
# from data_validation import LoanApplication  
# from pydantic import ValidationError

# app = Flask(__name__)
# catboost_model = pickle.load(open('catboost_model_version_1.pkl', 'rb'))
# scalar = pickle.load(open('data_scaling_latest.pkl', 'rb'))
# preprocessor = pickle.load(open('data_preprocessing.pkl', 'rb'))

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/predict_api', methods=['POST'])
# def predict_api():
#     try:
#         # Validate the incoming data using Pydantic
#         raw_data = request.json['data']
#         validated_data = LoanApplication(**raw_data).model_dump()  # .model_dump() to convert to dict
#     except ValidationError as e:
#         return jsonify({"error": e.errors()}), 400

#     # Convert to DataFrame
#     df = pd.DataFrame([validated_data])

#     # Preprocess and predict
#     processed_data = preprocessor.transform(df)
#     new_tran_data = scalar.transform(processed_data)
#     output = catboost_model.predict(new_tran_data)

#     prediction = 'Y' if output[0] == 1 else 'N'
#     return jsonify(prediction=prediction)

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Validate the incoming data using Pydantic
#         raw_data = request.form.to_dict()
#         validated_data = LoanApplication(**raw_data).model_dump()  # .model_dump() to convert to dict
#          # Convert to DataFrame
#         df = pd.DataFrame([validated_data])

#         # Preprocess and predict
#         processed_data = preprocessor.transform(df)
#         new_tran_data = scalar.transform(processed_data)
#         output = catboost_model.predict(new_tran_data)
#         prediction = 'Yes' if output[0] == 1 else 'No'
#         return render_template('home.html', prediction_text="The Default Prediction is : {}".format(prediction))

#     except ValidationError as e:
#         return render_template('home.html', prediction="Invalid input data", error=e.errors())

#     # Convert to DataFrame
#     df = pd.DataFrame([validated_data])

#     # Preprocess and predict
#     processed_data = preprocessor.transform(df)
#     new_tran_data = scalar.transform(processed_data)
#     output = catboost_model.predict(new_tran_data)

#     prediction = 'Y' if output[0] == 1 else 'N'
#     return render_template('home.html', prediction=prediction)

# if __name__ == '__main__':
#     app.run(debug=True)


import pickle
from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
from data_preprocessing import FullLoanPreprocessor
from data_validation import LoanApplication
from pydantic import ValidationError

app = Flask(__name__)
catboost_model = pickle.load(open('catboost_model_version_1.pkl', 'rb'))
scalar = pickle.load(open('data_scaling_latest.pkl', 'rb'))
preprocessor = pickle.load(open('data_preprocessing_v3.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    try:
        raw_data = request.json['data']
        validated_data = LoanApplication(**raw_data).model_dump()
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

    df = pd.DataFrame([validated_data])
    processed_data = preprocessor.transform(df)
    new_tran_data = scalar.transform(processed_data)
    output = catboost_model.predict(new_tran_data)
    prediction = 'Y' if output[0] == 1 else 'N'
    return jsonify(prediction=prediction)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        raw_data = request.form.to_dict()
        # Convert all numeric fields manually to float/int
        for key in raw_data:
            try:
                if '.' in raw_data[key]:
                    raw_data[key] = round(float(raw_data[key]), 6)
                else:
                    raw_data[key] = int(raw_data[key])
            except ValueError:
                pass  # Keep string values as is

        validated_data = LoanApplication(**raw_data).model_dump()
        df = pd.DataFrame([validated_data])
        processed_data = preprocessor.transform(df)
        new_tran_data = scalar.transform(processed_data)
        output = catboost_model.predict(new_tran_data)
        prediction = 'Yes' if output[0] == 1 else 'No'
        return render_template('home.html', prediction_text=f"The Default Prediction is: {prediction}")

    except ValidationError as e:
        return render_template('home.html', prediction_text="Invalid input data", error=e.errors())

if __name__ == '__main__':
    app.run(debug=True)

