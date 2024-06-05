# # inputs = [12, 2, 23.4, "mALE", 'No', 'southeats']
# # input_names = ['Age', 'Children Number', 'BMI', 'Gender','Smoker','Region']

# # dr = {input_names[i]: inputs[i]  for i in range(len(inputs))}

# # print(dr)

# from src.pipeline.prediction_pipeline import PredictionPipeline

# # 19	female	27.9	0	yes	southwest	16884.92
# # 18	male	33.8	1	no	southeast	1725.55
# single_data_point = {
#     'region': ['northwest'],
#     'sex': ['male'],
#     'smoker': ['no'],
#     'age': [32],
#     'bmi': [28.9]
# }

# data_point = [single_data_point, 0]
# pred_pipeline = PredictionPipeline()
# predicted_val = pred_pipeline.prediction(data_point)

# print(predicted_val)


