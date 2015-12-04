from django.contrib import admin
from .models import DatabaseNeuralNetwork, DatabaseNeuron, DatabaseNeuralConnection


admin.site.register(DatabaseNeuron)
admin.site.register(DatabaseNeuralConnection)
admin.site.register(DatabaseNeuralNetwork)
