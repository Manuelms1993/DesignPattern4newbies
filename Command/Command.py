
# Manuel Montero

"""
Encapsulate a request as an object, thereby letting you parameterize
clients with different requests, queue or log requests, and support
undoable operations.
"""

import abc, six

class Invoker:

    def __init__(self):
        self._commands = []

    def store_command(self, command):
        self._commands.append(command)

    def execute_commands(self):
        for command in self._commands:
            command.execute()

@six.add_metaclass(abc.ABCMeta)  
class CommandInterface:

    def __init__(self, receiver):
        self._receiver = receiver

    @abc.abstractmethod
    def execute(self):
        pass


class Command(CommandInterface):

    def execute(self):
        self._receiver.action()


class Receiver:
	
		__text = None
		
		def __init__(self, text):
			self.__text = text
			
		def action(self):
			print(self.__text)


class Encapsulate:
	
	__invoker = None
	
	def __init__(self, texts):
		self.__invoker = Invoker()
		for text in texts:
			receiver = Receiver(text)
			command = Command(receiver)
			self.__invoker.store_command(command)

	def execute_commands(self):
		self.__invoker.execute_commands()
        

encapsulateCommands = Encapsulate(["My name ", "is", "Manuel"])
encapsulateCommands.execute_commands()


