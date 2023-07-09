# rosmodelgen

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![repo size](https://img.shields.io/github/repo-size/takuya-ki/rosmodelgen)

Tools to generate model files used for ROS.

## Dependency

- Python3
  - numpy>=1.21.6
  - open3d>=0.16.0

## Installation

```bash
git clone https://github.com/takuya-ki/rosmodelgen.git --depth 1
cd rosmodelgen; mkdir -p meshes/visual meshes/collision
pip install -r requirements.txt
```

## Usage

### Generate a collision model in meshes/collistion with an original model in meshes/visual

```bash
python3 src/gen_collision.py
```

### Flip normals

1. Open a stl file with MeshLab
2. Click [Normals, Curvantures and Orientation]-[Invert Faces Orientation] from Filters menu
3. Check Force Flip and Click Apply

### Reduce faces

1. Open a stl file with MeshLab
2. Click [Remeshing, Simplification and Reconstruction]-[Simplification: Quadric Edge Collapse Decimation] from Filters menu
3. Change current Target number of faces to 5000 ~ 10000

## Author / Contributor

[Takuya Kiyokawa](https://takuya-ki.github.io/)

## License

This software is released under the MIT License, see [LICENSE](./LICENSE).
