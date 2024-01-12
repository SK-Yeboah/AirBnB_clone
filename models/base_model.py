#!/usr/bin/python3

from datetime import datetime
import uuid

class BaseModel:
    """
    BaseModel class defines common attributes and methods for other classes.

    Public instance attributes:
    - id: string - Assigned a UUID when an instance is created.
    - created_at: datetime - Assigned with the current datetime when an instance is created.
    - updated_at: datetime - Assigned with the current datetime when an instance is created,
      and updated every time the object is modified.

    Public instance methods:
    - __str__: Returns a formatted string representation of the instance.
    - save(self): Updates the public instance attribute 'updated_at' with the current datetime.
    - to_dict(self): Returns a dictionary containing all keys/values of __dict__ of the instance.
      Additionally, adds '__class__' with the class name and converts 'created_at' and 'updated_at'
      to string objects in ISO format.

    Usage:
    my_model = BaseModel()
    my_model.save()
    my_model_json = my_model.to_dict()
    print(my_model)
    print(my_model_json)
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize instance attributes

        Args:
            *args: Unused positional arguments.
            **kwargs: Dictionary containing attribute names and values for recreation.
        """
        from models import storage
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            # Populate instance  attributes from dictionary representation
            if '__class__' in kwargs:
                del kwargs["__class__"]
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    if isinstance(value, str):
                        setattr(self, key, datetime.strptime(value, date_format))
                    else:
                        setattr(self, key, value)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        if not kwargs:
            storage.new(self)
    
    def __str__(self):
        """Return a formated string representation of the instance"""
        return "[{}], ({}), {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """Update the 'updated_at' attribute with the current datetime"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()
        
    def to_dict(self):
        """
        Return dictionary representation of the object
        
        Returns:
        dict: A dictionary the contains all key/values of __dict__ of the instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict