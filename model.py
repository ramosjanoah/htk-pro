from keras.models import Sequential
from keras.layers import Dense
import feature_extract
def main():

	model = Sequential()
	model.add(Dense(input_dim=1208, units=2))
	model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
	print(model['has'])
	model.fit(x_train, y_train, epochs=5)


if __name__ == "__main__":
	main()
