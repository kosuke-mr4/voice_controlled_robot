# from setuptools import setup
# from catkin_pkg.python_setup import generate_distutils_setup

# setup_args = generate_distutils_setup(
#     packages=['voice_controlled_robot'],
#     package_dir={'': 'voice_controlled_robot/src'}
# )

# setup(**setup_args)

from setuptools import setup, find_packages

setup(
    name='voice_controlled_robot',
    version='0.0.0',  # バージョンを変更
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'rospy',
        'std_msgs',
        'geometry_msgs',
        'sensor_msgs',
    ],
    include_package_data=True,
    description='A voice controlled robot package for ROS',
    author='murakami-k',
    author_email='murakami-k@todo.todo',
    license='TODO',
    zip_safe=False,
)

