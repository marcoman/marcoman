# Workout Picker

The idea is to create an application that manages your workouts.

If we can ask the user for some basic information:

* Your Location
* How much time you have
* What type of workout you want (cardio, HIIT, etc.)

The goal is to then create a list of workouts based on your location.

There is a data-entry requirement, presumably something you and/or a community of people will do.  That is to add details about the location's capabilities:
* Equipment available
* How much space is available

Given an equipment and space availability, you can then be given a list of exercises.  For example, given the items listed below, you can see what is availble:

* Weights - 5 through 50 pounds
  * Curls
  * Squats
  * Overhead presses
  * And so on
* Exercise Bike
  * 5/10/15 minute warmups
  * Cardio training
  * and so on


Therefore, the idea is that if you arrive at a hotel in your favorite city, specify you have 30 minutes for a HIIT workout, you should then see something like this following:

* Set 1
  * Jumping Jacks - 60
  * Squat Jumps - 30
  * Push ups - 20
  * Power Kicks - 30 each side
  * Curls - 15 reps of 25 pounds
* Set 2
  * Jumping Jacks - 60
  * Squat Jumps - 30
  * Push ups - 20
  * Power Kicks - 30 each side
  * Curls - 15 reps of 25 pounds

and so on.


The project example here is an initial version, with many TODOs necessary before we can render a usable application.



# TODOs

* Add the concept of time per exercise
* Refine the user interface to allow different types of exercises
  * Rep-based only (e.g. Jumping Jacks)
  * Rep-based plus weights (e.g. 15 curls with 25 pounds)
  * Time-based (e.g. 60 second plank)
* Extend workouts to include Exercises
* Auto-generate a workout given a list of potential exercises
* Add "Equipment" to a location
  * This means Equipment should be of different types and capabilities.
  * Consider having stock equipment + exercise options for easier user setup
  * Consider adding brand-name equipment and their exercises
* Add the concept of sets - * Add pause time between sets
