# -*- coding: utf-8 -*-


## Log Reg

class LogReg:
  def __init__(self):
    self.n_iter=1000
    self.weights=None
    self.bias=None
    self.lr=0.001
  def sigmoid(self,z):
    return 1/(1+np.exp(-z))
  def fit(self,X,y):
    n_samples,n_features=X.shape
    self.weights=np.zeros(n_features)
    self.bias=0

    for _ in range(self.n_iter):
      linear=np.dot(X,self.weights)+self.bias
      y_pred=self.sigmoid(linear)

      dw=1/n_samples*np.dot(X.T,(y_pred-y))
      dl=1/n_samples*np.sum(y_pred-y)

      self.weights-=self.lr*dw
      self.bias-=self.lr*dl

  def predict(self,X):
    linear=np.dot(X,self.weights)+self.bias
    y_prob=self.sigmoid(linear)
    y_pred=(y_prob>=0.3).astype(int)
    return y_pred


if __name__=='__main__':
  model=LogReg()
  X_train=np.array([[1],[2],[7]])
  y_train=np.array([1,1,0])

  model.fit(X_train,y_train)
  print(model.predict(np.array([6])))



