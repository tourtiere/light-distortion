
# Light distortion

Distort big images with low memory needs.

A [libvips](https://github.com/libvips/libvips) reimplementation of ImageMagick's multi-points distortion method: [shepard's algorithm](https://legacy.imagemagick.org/Usage/distorts/#shepards) ([source code](https://github.com/ImageMagick/ImageMagick/blob/2747ccfc1044fc3da6d32ff1ebbca5e926fcf602/MagickCore/distort.c#L2817-L2848)).

## Usage

```
python3 light-distortion.py <INPUT_FILE> <OUTPUT_FILE> <POINTS>
```
Example:
```
python3 light-distortion.py koala.gif output.gif "30,11 20,11  48,29 58,29"
```
| input	 | output| 
|--------------|--------------------------|
| ![koala](https://user-images.githubusercontent.com/56520994/122707124-5bc31080-d227-11eb-9c4a-21de0912e03d.gif)      | ![output](https://user-images.githubusercontent.com/56520994/122707256-a6448d00-d227-11eb-8181-f12a1bafa451.gif) |

Corresponding ImageMagick command:
```
convert koala.gif -distort Shepards '30,11 20,11  48,29 58,29' output.gif
```


## Benchmark
Tested image: png of 129 MB and 5 random distortion couples

|             | ImageMagick	 | Pyvips (light-distortion)| 
|-------------|--------------|--------------------------|
| peak memory | **4058** MB  | **160** MB                   |
| time        | 64 seconds   | 41 seconds               |
