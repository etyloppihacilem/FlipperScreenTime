FlipperScreenTime
=================

Use your Flipper zero to set a screen time password you don't know using an automatically generated BadUSB script !

Useful when you're unable to control your phone usage. Simply send the CODE.txt generated to a friend and delete any occurence of the generated code from your reach.

Of course, you're not supposed to open any generated file as then contain the code.

# Usage

```
python3 screencode.py
```

This will generate a `script.txt` and a `CODE.txt` file, both containing the same code.

Televerse `script.txt` to the BadUSB folder on your flipper zero, connect the BadUSB app to your phone using bluetooth.

The script will write the code twice, waiting for a button press to enter the code a second time. (Because a code confirmation is asked when you set the code)
