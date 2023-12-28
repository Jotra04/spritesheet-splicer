# spritesheet-splicer

A python CLI tool designed to splice spritesheets into seperate frames or animated images

## Usage

Setup:

```sh
python -m venv ENV
source ENV/bin/activate
pip install -r requirements.txt
```

Run:

```sh
python .\splice.py -i example-spritesheet.png -o example-animation.gif -r 2 -c 5 -f 8
```

## Results

From the spritesheet `example-spritesheet.png`

![img](example-spritesheet.png)

To the animation `example-animation.gif`

![img](example-animation.gif)

## Supported filetypes

+ Animations: .gif, .webp
+ Frames: All other filetypes supported by pillow
