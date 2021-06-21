# Light distortion

Reimplements shepard's algorithm from ImageMagick to libvips "mapim" command and saves a lot of resource.

## Usage

```
python3 light-distortion <INPUT_FILE> <OUTPUT_FILE> <POINTS>
```

```
python3 light-distortion koala.gif stretched.gif "30,11 20,11  48,29 58,29"
```


## Benchmark
tested image: png of 129 MB and 5 random distortion couples

|             | ImageMagick	 | Pyvips (light-distortion)| 
|-------------|--------------|--------------------------|
| peak memory | 4058 MB      | 160 MB                   |
| time        | 64 seconds   | 41 seconds               |
