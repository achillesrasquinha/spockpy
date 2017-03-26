sudo apt-get clean
sudo apt-get autoremove
sudo apt-get autoclean

sudo apt-get update
sudo apt-get upgrade

echo 'Installing developer tools.'
sudo apt-get install build-essential cmake pkg-config

echo 'Installing image libraries.'
sudo apt-get install libjpeg8-dev libtiff5-dev libjasper-dev libpng12-dev

echo 'Installing video libraries.'
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev

echo 'Installing GUI libraries.'
sudo apt-get install libgtk-3-dev

echo 'Installing FORTRAN for optimized build.'
sudo apt-get install libatlas-base-dev gfortran

echo 'Installing Python 2.7 and 3.5 development packages.'
sudo apt-get install python2.7-dev python3.5-dev

echo 'Creating a tmp directory to work on.'
mkdir tmp && cd tmp

echo 'Downloading OpenCV 3.2.0.'
wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.2.0.zip
echo 'Unzipping OpenCV.'
unzip opencv.zip

echo 'Downloading opencv_contrib 3.2.0.'
wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.2.0.zip
echo 'Unzipping opencv_contrib.'
unzip opencv_contrib.zip

cd ./opencv-3.2.0
echo 'Creating a build directory.'
mkdir build && cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D INSTALL_C_EXAMPLES=OFF \
    -D OPENCV_EXTRA_MODULES_PATH=~./../opencv_contrib-3.2.0/modules \
    -D PYTHON_EXECUTABLE=~/usr/bin/python3 \
    -D BUILD_EXAMPLES=ON ..

echo 'Building OpenCV.'
make -j4

echo 'Installing OpenCV'
sudo make install
sudo ldconfig