import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
import pickle



# d_frame = pd.read_csv(r'app/parsing_files/1C_banking_comments.csv')
d_frame = pd.read_csv(r'app/result_dataset.csv')

# Drop rows with NaN values in 'comment_text' column
d_frame = d_frame.dropna(subset=['comment_text'])

X_train, X_test, y_train, y_test = train_test_split(d_frame['comment_text'], d_frame['comment_type'], test_size=0.2,
                                                    random_state=42)
sgd_ppl_clf = Pipeline([('tfidf', TfidfVectorizer()),('sgd_clf', SGDClassifier(random_state=42))])
sgd_ppl_clf.fit(X_train, y_train)
predicted_sgd = sgd_ppl_clf.predict(X_test)
# print(predicted_sgd)
# predicted_kneighbors = knb_ppl_clf.predict(X_test)
print(metrics.classification_report(predicted_sgd, y_test, zero_division=True))
print("ddddddddd")
# print(metrics.accuracy_score(predicted_sgd, y_test))
print(metrics.accuracy_score(predicted_sgd, y_test))





# сохранение модели
filename = 'app/text_classifier/finalized_model.sav'
pickle.dump(sgd_ppl_clf, open(filename, 'wb'))
print('сохранено')