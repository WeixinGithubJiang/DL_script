class NetworkBuild_base(object):

	def __init__(self, task, input_shape, output_shape, pre_train, net_name, customized_model):
		self.task = task
		self.input_shape = input_shape
		self.output_shape = output_shape
		self.pre_train = pre_train
		self.net_name = net_name
		self.model = customized_model

	def BuildNet(self):
		if self.task == "classification":
			if self.pre_train:
				self.LoadModel()
			else:
				pass


		if self.task == "regression":
			pass

	def LoadModel(self):
		if self.net_name == "VGG16":
			from keras.applications.vgg16 import VGG16
			self.model = VGG16(weights='imagenet', include_top=False,
				input_shape=self.input_shape,classes=self.output_shape)

		if self.net_name == "VGG19":
			from keras.applications.vgg16 import VGG19
			self.model = VGG19(weights='imagenet', include_top=False,
				input_shape=self.input_shape,classes=self.output_shape)

		if self.net_name == "ResNet50":
			from keras.applications.resnet50 import ResNet50
			self.model = ResNet50(weights='imagenet', include_top=False,
				input_shape=self.input_shape,classes=self.output_shape)
