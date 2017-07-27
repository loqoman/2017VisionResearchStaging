# Py_Vision
Repository to store temp. vision code before integration with 2017-Steamworks

## Reflective Tape

In past FRC game there has allways been reflective tape around key game feild elements. Currently 'Shiny_tape' is the program for looking at reflective tape and identifying it. It is currrently very rough, and will require proper integration for next year's game.The Code is ment to be run with a Ninvidea Jetson, using a camera with a ring of LED's around it. Couple things that can be changed:

* Currently filters by rectangle orientation(Between -100 and -80 with 9 O'clock being 0) .
* Intensity of the Blur.
* Intensity of the White filter.

Things that are not yet done, that will need to be done *At some point*:

* Sucuessful output (Either in JSON, or just some float values).
* Way to output those values from the Jetson (PWM, USB, ect).
