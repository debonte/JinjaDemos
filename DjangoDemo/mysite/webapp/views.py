from django.shortcuts import render

from .models import Person

class Cat:
    def __init__(self, name: str, age: int, colors: list[str]):
        self.name = name
        """Name of the cat."""
        
        self.age = age
        """Age in years."""

        self.colors = colors
        """List of colors the cat has."""

cats = [Cat("Mittens", 10, ["black", "white"]), Cat("Max", 8, ["gray"]), Cat("Watson", 1, ["black", "white"]), Cat("Sherlock", 1, ["gray", "white"])]

def index(request):
    person = Person()
    person.save()
    # At runtime objects is a django.db.models.manager.Manager
    # get_or_create is bound method QuerySet.get_or_create of <django.db.models.manager.Manager object
    Person.objects.get_or_create()
    return render(request, "webapp/item.html", {
                                                   "id": id, 
                                                   "cats": cats, 
                                                   "dogOpinion2": "annoying!" 
                                               })