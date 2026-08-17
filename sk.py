from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

model=LinearRegression()
model2=LogisticRegression()
X = [
    [1],
    [2],
    [2.5],
    [3],
    [3.5],
    [4],
    [4.5],
    [5],
    [6],
    [7],
    [8],
    [9]
]

# Result
# 0 = Fail
# 1 = Pass
Y = [
    0,
    0,
    0,
    0,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1
]
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=1)
model2.fit(X_train,Y_train)
prediction=model2.predict(X_test)
print("actual:",Y_test)
print("prediction:",prediction)
probability=model2.predict_proba(X_test)
print("probability:",probability)
accuracy=model2.score(X_test,Y_test)
print("accuracy:",accuracy)
new_student = [[4.2]]

prediction = model2.predict(new_student)
probability = model2.predict_proba(new_student)

print("Prediction:", prediction)
print("Probability:", probability)

# //linear regression
# x = [
#     [850, 2, 1, 15, 12.5, 1],
#     [1100, 2, 2, 10, 10.2, 1],
#     [1250, 3, 2, 8, 9.5, 1],
#     [1400, 3, 2, 12, 8.1, 1],
#     [1550, 3, 3, 6, 7.2, 2],
#     [1700, 3, 2, 9, 6.8, 2],
#     [1850, 4, 3, 5, 6.1, 2],
#     [2000, 4, 3, 7, 5.5, 2],
#     [2150, 4, 3, 4, 5.0, 2],
#     [2300, 4, 4, 6, 4.6, 2],
#     [2450, 4, 3, 3, 4.1, 2],
#     [2600, 5, 4, 5, 3.8, 2],
#     [2750, 5, 4, 2, 3.2, 3],
#     [2900, 5, 4, 4, 2.9, 3],
#     [3100, 5, 5, 3, 2.5, 3],
#     [3300, 5, 4, 2, 2.1, 3],
#     [3500, 6, 5, 1, 1.8, 3],
#     [3700, 6, 5, 3, 1.5, 3],
#     [4000, 6, 5, 2, 1.2, 4],
#     [4300, 7, 6, 1, 0.8, 4]
# ]

# y = [
#     48,
#     58,
#     67,
#     73,
#     85,
#     91,
#     105,
#     112,
#     121,
#     132,
#     141,
#     153,
#     165,
#     174,
#     190,
#     202,
#     218,
#     231,
#     250,
#     275
# ]
# x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=1)
# model.fit(x,y)
# pre=model.predict(x_test)
# print("actual:",y_test)
# print("prediction:",pre)
# a=[]
# for i in range(len(y_test)):
#     print(y_test[i]-pre[i])
#     a.append((pre[i]-y_test[i])*(pre[i]-y_test[i]))
# print("mean squared error is:",sum(a)/len(a))
# r2=r2_score(y_test,pre)
# print("R2 score is:",r2)
