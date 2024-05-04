import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer


data = pd.read_csv('Users/sragv/Desktop/employee.csv')

numeric_features = ['job_years', 'hours_per_week', 'telecommute_days_per_week'] 
categorical_features = ['country', 'employment_status', 'job_title', 'education', 'is_manager']  

numeric_transformer = Pipeline(steps=[('imputer', SimpleImputer(strategy='median')), ('scaler', StandardScaler())])
categorical_transformer = Pipeline(steps=[('imputer', SimpleImputer(strategy='most_frequent')),('onehot', OneHotEncoder(handle_unknown='ignore'))])
preprocessor = ColumnTransformer(transformers=[('num', numeric_transformer, numeric_features), ('cat', categorical_transformer, categorical_features)])

model = LinearRegression()
pipeline = Pipeline(steps=[('preprocessor', preprocessor), ('model', model)])

X = data.drop('salary', axis=1)  # assuming 'salary' is the target variable
y = data['salary']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
pipeline.fit(X_train, y_train)
predictions = pipeline.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)

print('Mean Absolute Error:', mae)
print('Mean Square Error:', mse)
