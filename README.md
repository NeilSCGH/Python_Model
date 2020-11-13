# Python Model

Simple model for python class
```
Usage: python main.py -f firstname [-l lastname] 
                      [-a age] [-adult] [-h]

Options:
   -f firstname First name.
   -l lastname  (Optional) Last name, default: "Doe".
   -a age       (Optional) Age.
   -adult       (Optional) Check is the person is adult.
                Require -a.
   -h           (Optional) Print this help.
```

## Example
```
python main.py -f Neil -a 5 

Running !
Neil Doe is 5 years old
```
```
python main.py -f Neil -a 50 -adult

Running !
Neil Doe is 50 years old
Neil Doe is adult
```